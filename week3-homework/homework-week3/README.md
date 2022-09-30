# README.md Assignment Week #3


Purpose: Align sacCer3 (UCSC genome browse) aks R64-1-1 (NCBI Assembly archive) to a WT wine yeast sample from a winery.


Later: git add --force <yourvcfilename.vcf>



# Step 1: Indexing the sacCer3.fa genome with index
	bwa index savCer3.fa
	
# Step 2: Align with bwa mem: DO 10 TIMES for EACH fastq file
	# with -R: @RG\tID:Sample1\tSM:Sample1

	#WRITING::

	'''A01_09.fastq'''
	# Checking function
	bwa mem -t 4 -R "@RG\tID:A01_09\tSM:A01_09" -o A01_09.sam sacCer3.fa A01_09.fastq

	'''A01_11.fastq'''
	bwa mem -t 4 -R "@RG\tID:A01_11\tSM:A01_11" -o A01_11.sam sacCer3.fa A01_11.sam

	'''A01_23.fastq'''
	bwa mem -t 4 -R "@RG\tID:A01_23\tSM:A01_23" -o A01_23.sam sacCer3.fa A01_23.fastq 

	'''A01_24.fastq'''
	bwa mem -t 4 -R "@RG\tID:A01_24\tSM:A01_24" -o A01_24.sam sacCer3.fa A01_24.fastq

	'''A01_27.fastq'''
	bwa mem -t 4 -R "@RG\tID:A01_27\tSM:A01_27" -o A01_27.sam sacCer3.fa A01_27.fastq

	'''A01_31.fastq'''
	bwa mem -t 4 -R "@RG\tID:A01_31\tSM:A01_31" -o A01_31.sam sacCer3.fa A01_31.fastq

	'''A01_35.fastq'''
	bwa mem -t 4 -R "@RG\tID:A01_35\tSM:A01_35" -o A01_35.sam sacCer3.fa A01_35.fastq

	'''A01_39.fastq'''
	bwa mem -t 4 -R "@RG\tID:A01_39\tSM:A01_39" -o A01_39.sam sacCer3.fa A01_39.fastq

	'''A01_62.fastq'''
	bwa mem -t 4 -R "@RG\tID:A01_62\tSM:A01_62" -o A01_62.sam sacCer3.fa A01_62.fastq

	'''A01_63.fastq'''
	bwa mem -t 4 -R "@RG\tID:A01_63\tSM:A01_63" -o A01_63.sam sacCer3.fa A01_63.fastq


# Step 3a: Create a sorted bam file with samtools sort, for input to variant callers
	# samtools sort -@ 4 -O bam -o SRR16356854.bam SRR16356854.sam

		## to sort from sam to bam -@ 4 to tell number of CPUs to use here
		## -O for output format
		## -q is ...
		## bam wanted output, then from the sam file

		'''A01_09.fastq'''
		samtools sort -@ 4 -O bam -o A01_09.bam A01_09.sam

		'''A01_11.fastq'''
		samtools sort -@ 4 -O bam -o A01_11.bam A01_11.sam

		'''A01_23.fastq'''
		samtools sort -@ 4 -O bam -o A01_23.bam A01_23.sam

		'''A01_24.fastq'''
		samtools sort -@ 4 -O bam -o A01_24.bam A01_24.sam

		'''A01_27.fastq'''
		samtools sort -@ 4 -O bam -o A01_27.bam A01_27.sam

		'''A01_31.fastq'''
		samtools sort -@ 4 -O bam -o A01_31.bam A01_31.sam

		'''A01_35.fastq'''
		samtools sort -@ 4 -O bam -o A01_35.bam A01_35.sam

		'''A01_39.fastq'''
		samtools sort -@ 4 -O bam -o A01_39.bam A01_39.sam

		'''A01_62.fastq'''
		samtools sort -@ 4 -O bam -o A01_62.bam A01_62.sam

		'''A01_63.fastq'''
		samtools sort -@ 4 -O bam -o A01_63.bam A01_63.sam
		
# Step 3b: Indexing the bam files
	for SAMPLE in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
	do
		samtools index ${SAMPLE}.bam
	done

# Step 4: With freebayes
	#Code attempt 1: did not work for output vcf file (too short)
	# freebayes -f sacCer3.fa -p 32 --genotype-qualities -l A01_09.bam A01_11.bam A01_23.bam A01_24.bam A01_27.bam A01_31.bam A01_35.bam A01_39.bam A01_62.bam A01_63.bam > yeast2.vcf
	#Why not work? Needs the -L to denote a list of bam files (not lowercase as above), and also needs the ploidy to be set to 1 to denote that it is only haploid for yeast! Thanks Steph!
	
	#Code attempt 2: Successful!
	freebayes -f sacCer3.fa -p 1 --genotype-qualities *.bam > yeast2.vcf
	#otherwise, should run fine, and saving as yeast2.vcf

# Step 5: Filter variants based on genotype quality using vcffilter
	#Adding in filters with the vcf file for QUAL > 20 which means removes any sites with estimated probability of not being polymorphic less than phred 20 (aka 0.01), or probability of polymorphism > 0.99.
	#From the link: https://github.com/freebayes/freebayes

	vcffilter -f "QUAL > 20" yeast2.vcf > Yeast_filter_results.vcf
		

# Step 6: Decompose complex haplotypes using vcfallelicprimitives
	#vcfallelicprimitives converts stdin or given VCF file to tab-delimited format
	#0 : Success | not 0 : Failure
	#-g is keep genotype where the genotype-level annotations when decomposing should be saved
	#-k is keep information at allele-level notations

	vcfallelicprimitives -k -g Yeast_filter_results.vcf > decompose_filter_yeast.vcf


# Step 7: Variant effect prediction with snpeff ann
	conda install snpeff=5.0 -y
	snpeff download R64-1-1.99
	#snpeff --help
	#Annotating vcf file with genetic variants:
	snpeff ann R64-1-1.99 decompose_filter_yeast.vcf > annotated_yeast.vcf
	

# Step 8: Exploratory data analysis through plotting
	import sys
	import numpy as np
	import matplotlib.pyplot as plt

	from vcfParser import *

	parsed_vcf = parse_vcf("annotated_yeast.vcf")[1:]


	quality = [row[5] for row in parsed_vcf]



	read_depth = [row[7]["DP"] for row in parsed_vcf]



	allele_frequency = [row[7]["AF"] for row in parsed_vcf]



	variant_prediction = []
	for row in parsed_vcf:
	    parsedANN = row[7]["ANN"].split("|")
    
	    variant_prediction.append(parsedANN[7])

	# x=[list(i) for i in enumerate(variant_prediction)]
	# print(len(x))


	#print(countList(variant_prediction))
	# [row[7]["ANN"] for row in parsed_vcf]
	# print(variant_predition)
	# print(variant_prediction)

	# ############ Adding for loops
	# fig, ax = plt.subplots()
	fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, ncols=1)

	ax0.hist(read_depth)
	ax0.set_xlabel("Read depth")
	ax0.set_ylabel("Frequency")

	ax1.hist(quality)
	ax1.set_xlabel("Quality")
	ax1.set_ylabel("Frequency")

	ax2.hist(allele_frequency)
	ax2.set_xlabel("Allele frequency")
	ax2.set_ylabel("Frequency")

	print(set(variant_prediction))
	uniques = list(set(variant_prediction))

	counts = [variant_prediction.count(value) for value in uniques[1:]]
	  # = set(variant_prediction)

	ax3.bar(uniques[1:], counts)
	ax3.set_xlabel("Variant prediction")
	ax3.set_ylabel("Count")
	#
	plt.tight_layout()
	#plt.show()


	plt.savefig("image.png")
	plt.close(fig)