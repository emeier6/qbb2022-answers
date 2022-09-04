# QBB2022 - Day 1 - Homework Exercises Submission
	#Touch README.md
	#open -a Textmate README.md
	
	#git add README.md exercise1.sh
	#git commit -m "edited script and answers for day 1 hw exercise 1"
	#git push


		#grep -v "#" ~/data/vcf_files/random_snippet.vcf  | awk '{if  ($4 == "C") {print $5}}' | sort | uniq -c

#Exercise 1:
	#GOAL: use the script exercise1.sh in order to find the most common alternate 
	#allele for all of the reference allele bases, not just Cytosine
	
head exercise1.sh


	#!/bin/bash
	#USAGE: bash exercise1.sh input_VCF

for nuc in A C G T
	#do
  echo "Considering " $nuc
  awk '/^#/{next} {if ($4 == $nuc) {print $5}}' $1 | sort | uniq -c
	#done
		#OUTPUT
		#ERROR: awk: illegal field $(), name "nuc"
		#same for each A, C, G, T, but cannot assign nuc in the awk expression

		#Look at the script and compare it to the command we used in the interactive lecture. 
		#Using the usage statement provided at the beginning of the script, try to run the script using ~/data/vcf_files/random_snippet.vcf as the input VCF file.
		#ERROR:
Considering  A
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  C
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  G
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  T
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1


	#!/bin/bash

	#USAGE: bash exercise1.sh input_VCF = 

for nuc in A C G T
do
  #Tried:
  #awk '/^#/{next} {if ($4 == $nuc) {print $5}}' $1 | sort | uniq -c
  #awk 'NR=='$i'{print $1, $2}' temp_file
  ##awk '/^#/{next} {if ($4 == '$nuc') {print $5}}' $1 | sort | uniq -c
  #awk -v i="$i" '/^#/{next} {if (NR==i) {print $1, $2}}' temp_file
  
	#What error message do you see and how will you fix it? 
	#If needed, google part of the error message to see how you can fix the script.
	#Fixed Code:
  awk -v nuc="$nuc" '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c

done

	#Record the output from the working script.
	#OUTPUT:
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G

	#Do the results make sense given what you know about the biology of these bases?
	#I would say yes, because A and G are similar structures, while C and T are similar structures.
	#A and G are more likely to switch compared to A and C or T, and C is more likely to swith with T compared to G and A.
	
	


#Exercise 2:
	#GOAL: What’s the most common alternate allele for a Cytosine reference allele for variants occurring in promoter like regions of the genome?

	#1. ~/data/vcf_files/random_snippet.vcf
	vcffile=/Users/cmdb/data/vcf_files/random_snippet.vcf

	#2. DEFINING PROMOTER-LIKE REGIONS:
	#~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed
	chromHMM=/Users/cmdb/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed

	###bedtools intersect -a $vcffile -b $sorted > intersect_out_ex2.bed

	wc intersect_out_ex2.bed
	#OUTPUT: number of SNVs that intersect with A gene 
	# 9893 25296401 102034267 intersect_out_ex2.bed

	#awk '/^#/{next} {print $4}' ~/data/vcf_files/random_snippet.vcf | sort | uniq -c

	#less ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed 


	###3. Using this segmentation, do promoters appear to be clearly and objectively defined?

		#Defining the promoter region is not clearly defined. They are not defined where they are located, and while they may be a part of trascriptional regulation, the database does not really say what their affects are. 1, 2, 3, 10, 11, 12 are close to the regions of the genes and likely within the promoter regions, however, promoter regions are not always next to the gene of interest, and can be located farther away. 
	
	
	
	grep -Ew '1|2|3|10|11' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort -nk 4 > sortedChmm.bed
	
	sorted=/Users/cmdb/qbb2022-answers/day1-homework/sortedChmm.bed

	bedtools intersect -a $vcffile -b $sorted > intersect_out_ex2_2.bed
	#awk '{if($4 == "1,2,3,10,11")} {(print $4)}' /data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq -c

	for nuc in C
	do
	  echo "Considering " $nuc
	  #awk '/^#/{next} {if ($4 == $nuc) {print $5}}' $1 | sort | uniq -c

	  #awk -v i="$i" '/^#/{next} {if (NR==i) {print $1, $2}}' temp_file
	  awk -v nuc="$nuc" '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c

	  #awk 'NR=='$i'{print $1, $2}' temp_file
	  ##awk '/^#/{next} {if ($4 == '$nuc') {print $5}}' $1 | sort | uniq -c
	done
	
	bash exercise2.sh intersect_out_)ex2_2.bed
	
	Considering  C
	  12 A
	  11 G
	  41 T
	  
	  
#Exercise 3:
	#!/bin/bash
	
	#USAGE: bash exercise3.sh input_VCF
	
	#awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
	#awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
	awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 | sort -k1,1 -k2,2n > variants.bed
	
	sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed

	bedtools closest -a variants.bed -b genes.sorted.bed > doubleysorted.bed 
	#1.Look at the script (exercise3.sh) and paraphrase in your README what you think each line is doing and why it is necessary given the documentation for bedtools closest. 
		#What I think is happening is the the sort tool is grouping different columns to sort and then running the matrix of sorted columns in bedtools. 
	
	
	#2.Using the usage statement provided at the beginning of the script (exercise3.sh), try to run the script using ~/data/vcf_files/random_snippet.vcf as the input VCF file.
	
	#USAGE: bash exercise3.sh ~/data/vcf_files/random_snippet.vcf

	#3. ERROR1: unable to open file or unable to determine types for file variants.bed
		#- Please ensure that your file is TAB delimited (e.g., cat -t FILE).
		#FIXING ERROR1: 
			#awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
			#TO CORRECT: 
			#awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed

	#ERROR2:	
		#- Also ensure that your file has integer chromosome coordinates in the 
	  #expected columns (e.g., cols 2 and 3 for BED).
  
	  #FIXING ERROR2:
	  		#awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
			#TO CORRECT:
			#awk -v OFS='\t' '/^#/{next} {print $1,$2-1, $2}' $1 | sort -k1,1 -k2,2n > variants.bed


			#4. Finally, use the output to answer the following questions. Record the answers and the commands you used to find the answers in your README.
			#How many variants are returned and how many unique genes are returned? How many variants on average are therefore connected to a gene with bedtools closest?
  
		cut -f 7 doubleysorted.bed | sort | uniq -c | wc
  
	  	#	OUTPUT:
	    #	 200     400    2447

	
		wc -l doubleysorted.bed
		#OUTPUT: 10293 doubleysorted.bed 
	
	
#THE END :,^)