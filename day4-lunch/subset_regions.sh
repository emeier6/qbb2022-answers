#!/bin/bash

GTF=$1
CHR=chr21

if [ ! -f $CHR.gtf ]
then
    echo "--- Creating $CHR.gtf"
    grep -w $CHR $GTF > $CHR.gtf
fi

#create protein coding and processing genes, and anything you want to pull out
for TYPE in lncRNA protein_coding processed_pseudogene
do
    echo "--- Creating $TYPE.$CHR.bed"
    grep $TYPE $CHR.gtf | awk 'BEGIN {OFS="\t"}{if ($3=="gene"){print $1, $4-1, $5}}' > $TYPE.$CHR.bed
done

#creating an exons file
#removing priotein coding or lncRNA genes that are not protein encoding (introns)
echo "--- Creating exons.$CHR.bed"
grep "lncRNA" $CHR.gtf | awk 'BEGIN {OFS="\t"}{if ($3=="exon"){print $1, $4-1, $5}}' > exons.$CHR.bed

#python do_all.sh gencode.v41.annotation.gtf 