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
#For each bed file in the directory
for TYPE in *.bed
do
	#Telling you that it will be creating a vcf file for the type
    echo "--- Subsetting $TYPE.vcf"
	#This is sorting through the file with awk and doing some calculations
	#Dont want to output the snv twice so do the union to get rid of duplicates with merge
    bedtools sort -i $TYPE | bedtools merge | awk '{total+=$3-$2} END{print "    + Covering " total " bp"}'
    #This line is now making the vcf file to intersect the bedfiles for the overlapping regions
	bedtools intersect -u -header -a $VCF -b $TYPE > $TYPE.vcf
done

echo "*** Plotting AC for each .vcf"
#For each vcf it finds in the directory
for SUBSET in *.vcf
do
	#Tell that you are making a vcf file for each of these
    echo "--- Plotting AC for $SUBSET"
	#New name of the plot and running it in the puthon plot function
    python plot_vcf_ac.py $SUBSET
done

