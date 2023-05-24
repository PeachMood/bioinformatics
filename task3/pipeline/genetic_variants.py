import subprocess
from dagster import Out, Output, job, op

def output_path(file):
    return f'./output/{file}'

@op
def pre_stage(context):
    context.log.info('Создание папки для выходных данных')
    subprocess.Popen(f'mkdir output',  shell=True)

    context.log.info('Сбор данных')
    data = {'ref_file': 'ecoli.fna', 'seq_file': 'ecoli.fastq'}

    return data

@op
def quality_control(context, data):
    context.log.info('Контроль качества видов')
    report_file = output_path('qcreport.html')
    subprocess.run(['fastqc', '-p', data['seq_file'], '--outdir', 'output'])
    subprocess.run(['mv', output_path('ecoli_fastqc.html'), report_file])
    return report_file

@op
def index_reference_sequence(context, data):
    context.log.info('Индексация референсной последовательности')
    index_file = output_path(data['ref_file'])
    subprocess.run(['bwa', 'index', '-p', index_file, data['ref_file']])
    return index_file

@op
def perform_alignment(context, data, index_file):
    context.log.info('Построение выравнивания прочтений и референса в формате sam')
    sam_file = output_path('alignments.sam')
    subprocess.run(['bwa', 'mem', index_file,  data['seq_file']], stdout=open(sam_file, 'w+'))
    return sam_file

@op
def convert_to_bam(context, sam_file):
    context.log.info('Конвертирование формата sam в bam')
    bam_file = output_path('alignments.bam')
    subprocess.run(['samtools', 'view', '-b', sam_file, '-o', bam_file])
    return bam_file

@op
def perform_evaluation(context, bam_file):
    context.log.info('Построение оценки')
    flagstat_file = output_path('flagstat.txt')
    subprocess.call(['samtools', 'flagstat', bam_file], stdout=open(flagstat_file, 'w+'))
    return flagstat_file

@op(out={'ok_result': Out(is_required=False), 'bad_result': Out(is_required=False)})
def parse_evaluation_result(context, flagstat_file):
    context.log.info('Получение результата оценивания при помощи скрипта')
    output = subprocess.run(['python3', 'quality_evaluation.py', flagstat_file], stdout=subprocess.PIPE)

    result = output.stdout.decode().strip()
    context.log.info(result)

    if result == 'OK':
        yield Output(result, 'ok_result')
    else:
        yield Output(result, 'bad_result')

@op
def print_ok_result(context, ok_result):
    context.log.info(f'Качество выравнивания: {ok_result}')
    return ok_result

@op
def print_bad_result(context, bad_result):
    context.log.info(f'Качество выравнивания: {bad_result}')

@op
def sort_alignment(context, ok_result, bam_file):
    context.log.info(f'Cортировка полученного выравнивания')
    sorted_bam_file = output_path('alignments.sorted.bam')
    subprocess.run(['samtools', 'sort', '-o', sorted_bam_file, bam_file])
    return sorted_bam_file

@op
def perform_variant_calling(context, data, sorted_bam_file):
    context.log.info(f'Проведение коллинга генетических вариантов')
    result_file = output_path('result.vcf')
    subprocess.run(['freebayes', '-f', data['ref_file'], sorted_bam_file], stdout=open(result_file, 'w+'))
    context.log.info(f'Finished')
    return result_file

@job()
def genetic_variants():
    data = pre_stage()
    quality_control(data)
    index_file = index_reference_sequence(data)
    sam_file = perform_alignment(data, index_file)
    bam_file = convert_to_bam(sam_file)
    flagstat_file = perform_evaluation(bam_file)
    ok_result, bad_result = parse_evaluation_result(flagstat_file)
    ok_result = print_ok_result(ok_result)
    bad_result = print_bad_result(bad_result)
    sorted_bam_file = sort_alignment(ok_result, bam_file)
    result_file = perform_variant_calling(data, sorted_bam_file)
