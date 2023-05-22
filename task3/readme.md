# 💻 Домашнее задание

## Тема
Построение пайплайна получения генетических вариантов

## Ссылки на данные
Загруженное прочтение: https://www.ncbi.nlm.nih.gov/sra/SRX20411742[accn] <br/>
Референсный геном: https://www.ncbi.nlm.nih.gov/assembly/GCF_000005845.2/

## Скрипт на bash с реализованным алгоритмом

## Алгоритм получения генетических вариантов
1. Скачать необоходимые данные
2. Провести контроль качества видов<br/>
  `fastqc ecoli.fastq -> ecoli_fastqc.html`
3. Проиндексировать референсную последовательность<br/>
  `bwa index ecoli.fna -> ecoli.fna.*`
4. Построить выравнивание прочтений и референса в формате sam<br/>
  `bwa mem ecoli.fna ecoli.fastq > alignments.sam -> alignments.sam`
5. Конвертировать формат sam в bam<br/>
  `samtools view -b alignments.sam -o alignments.bam -> alignments.bam`
6. Построить оценку<br/>
  `samtools flagstat alignments.bam > flagstat.txt -> flagstat.txt`
7. Получить результат оценивания при помощи скрипта<br/>
  `./get_percent.sh flagstat.txt`
8. Отсортировать выравнивание<br/>
  `samtools sort -o sorted_alignment.sam alignment.sam ->  sorted_alignment.sam`
