# 💻 Домашнее задание

## Тема
Построение пайплайна получения генетических вариантов

## Ссылки на данные
Загруженное прочтение: https://www.ncbi.nlm.nih.gov/sra/SRX20411742[accn]
Референсный геном: https://www.ncbi.nlm.nih.gov/assembly/GCF_000005845.2/

## Скрипт на bash с реализованным алгоритмом

## Алгоритм получения генетических вариантов
1. Скачать необоходимые данные
2. Провести контроль качества видов
  `fastqc ecoli.fastq -> ecoli_fastqc.html`
3. Проиндексировать референсную последовательность
  `bwa index ecoli.fna -> ecoli.fna.*`
4. Построить выравнивание прочтений и референса в формате sam
  `bwa mem ecoli.fna ecoli.fastq > alignments.sam -> alignments.sam`
5. Конвертировать формат sam в bam
  `samtools view -b alignments.sam -o alignments.bam -> alignments.bam`
6. Построить оценку
  `samtools flagstat alignments.bam > flagstat.txt -> flagstat.txt`
7. Получить результат оценивания при помощи скрипта
  `./get_percent.sh flagstat.txt`
8. Отсортировать выравнивание
  `samtools sort -o sorted_alignment.sam alignment.sam ->  sorted_alignment.sam`
