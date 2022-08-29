# QBB2022 repository

# QBB2022 - Day 1 - Lunch Exercises Submission

 1. I’m excited to learn how to work with and organize files in large data sets!>.
	 
 2. B) wc exons.chr21.bed #Number of exons: 13652 (lines)
 		wc genes.ch21.bed #Number of genes: 219 (lines)
		Mean = number of exons/number of genes
		Mean = 13653 / 219
		Mean = 62.3424657534
 2. C) Medium:
	#I would first sort by the exon position:
	sort -k 2 exon.chr21.bed 
	 #and then find the number of repeated values at a certain position: 
	 sort -k 2 exon.chr21.bed | uniq -c
	 #and then sort by unique values
	 sort -k 2 exons.chr21.bed | uniq -c | sort
 	#you can either reverse the list to have the highest number sorted at the top, or select for the highest number values
	#the median number values is 42 for chr21: 414335836, 41437014, 41439693
	

3. A) Make a copy of the new file into the day1-lunch directory:
	cp ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed .
	
	B) How many regions classified for each state:
	cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq -c
	Output:
	305 1
	  17 10
	  17 11
	  30 12
	  62 13
	 228 14
	 992 15
	 678 2
	  79 3
	 377 4
	 808 5
	 148 6
	1050 7
	 156 8
	 654 9
	
	15 regions of the geneome (column 2), and different numbers of repetitions
	
	C) First column describes the largest part of the genome, and that is that region 7 has the most unique values at 1050. Make another column that represents the basepair length for each of the start and stop regions of each of the 15 regions of the genome. Next, sorting by high to low of the new basepair length column, we could relate the largest bp length to the region, which would tell us which reason has the largest size and therefore genome fraction. 
	
 4. A) Make a copy of the new file into the day1-lunch directory:
 	cp ~/data/metadata_and_txt_files/integrated_call_samples.panel .
	B) How many samples are in each of the pop(ulations) of the AFR super_pop(ulation)?
	head integrated_call_samples.panel #visualize the number of headers and which columns they representd
	grep AFR integrated_call_samples.panel | cut -f 2 | sort | uniq -c
	#grep is the search function for AFR in column 3
	#cut looks at the different subpopulations of AFR in column 2
	#we then sort that to group the column 2 subpopulations
	#we then look at the unique number of individuals per subpopulations (of the AFR population)
	
	123 ACB
	 112 ASW
	 173 ESN
	 180 GWD
	 122 LWK
	 128 MSL
	 206 YRI
	

	C) 
	cut -f 3 integrated_call_samples.panel | sort | uniq -c 
	#allows us to sort by the 3rd column (super population) and then sort by the second column (population)
	#last uniq -c value tells us number of populations in the super population
	1044 AFR
	 535 AMR
	 673 EAS
	 670 EUR
	 661 SAS
	   1 super_pop
	 
	 ANSWER: For the AFR population, we have 1044 populations.
	 
5. 	A) cd
		cp ~/data/   /random_snippet.vcf
	 B) less -S random_snippet.vcf
		 #Go over to the right and look at the column information. First column is the notes,
		 #second column is filter, and so on to the info, format and HG000XX lines
			
	C)	 