#!/bin/bash

# Создадим папку для выходных данных
mkdir output

# Проведем контроль качества видов
fastqc ecoli.fastq --outdir output
mv ./output/ecoli_fastqc.html ./output/qcreport.html

# Проиндексируем референсную последовательность
bwa index -p ./output/ecoli.fna ecoli.fna

# Построим выравнивание прочтений и референса в формате sam
bwa mem ./output/ecoli.fna ecoli.fastq > ./output/alignments.sam

# Конвертируем формат sam в bam
samtools view -b ./output/alignments.sam -o ./output/alignments.bam

# Построим оценку
samtools flagstat ./output/alignments.bam > ./output/flagstat.txt

# Получим результат оценивания при помощи скрипта
result=$(python3 quality_evaluation.py ./output/flagstat.txt)

# Выведем результат
echo "Качество выравнивания: $result"

if [ "$result" == "OK" ]
then
  # Отсортируем полученное выравнивание
  samtools sort -o ./output/alignments.sorted.bam ./output/alignments.bam
  # Проведем коллинг генетических вариантов
  freebayes -f ecoli.fna ./output/alignments.sorted.bam > ./output/result.vcf
  # Завершаем работу
  echo "Finished"
fi
