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
