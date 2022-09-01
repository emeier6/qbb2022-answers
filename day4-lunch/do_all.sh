#!/bin/bash

VCF=$1
GTF=$2

if [[ ! -f "$VCF" || ! -f "$GTF" ]]
then
    echo ".vcf file ('$VCF') or .gtf file ('$GTF') not found"
    exit
fi

echo "*** Creating .bed files for features of interest"
bash subset_regions.sh $GTF

echo "*** Subsetting .vcf for each feature"
for TYPE in *.bed
do
    echo "--- Subsetting $TYPE.vcf"
    bedtools sort -i $TYPE | bedtools merge | awk '{total+=$3-$2} END{print "    + Covering " total " bp"}'
    bedtools intersect -u -header -a $VCF -b $TYPE > $TYPE.vcf
done

echo "*** Plotting AC for each .vcf"
for SUBSET in *.vcf
do
    echo "--- Plotting AC for $SUBSET"
    python plot_vcf_ac.py $SUBSET
done

