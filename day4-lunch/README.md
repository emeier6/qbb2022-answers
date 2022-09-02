1. Make a copy of code and input data

```
cd
git clone https://github.com/bxlab/cmdb-plot-vcfs
cd cmdb-plot-vcfs
cp ~/data/vcf_files/random_snippet.vcf .
cp ~/data/gtf_files/gencode.v41.annotation.gtf.gz .
gunzip *.gz
```

2. Create a new conda environment with required software

```
conda create --name day4-lunch
conda activate day4-lunch
conda install bedtools matplotlib
```

3. Run workflow

```
bash do_all.sh random_snippet.vcf gencode.v41.annotation.gtf
```

#Exercise 1: 
	1. Which portion of do_all.sh output (not script) reports how many bp each feature covers
	
		-The output that reports how many bp each feature covers are the processed pseudogenes?
		-Running this sh code made new bed files, many vcf files, and png files.
		-I believe this refers to the vcf files that this made, of which there are bed, vcf and png files for each:
			exons.chr21
			processed_pseudogene.chr21
			protein_coding.chr21
		-As well as the annotated v41 genecode, and the random_snippet vcf
	2. 
		A) I can open the png files that were generated, and look that the cache files on github are the same as on the github reference cache file.
			-And they do look the same!
		B) There are ways to look at two text files and ask if they are the same, but I am not quite sure as to the coding for that.
			-Actually found a way to ask this in Unix!:
			cmp --silent $old $new || echo "files are different"
			-In this case, the code would read:
				cmp --silent cache/exons.chr21.bed.vcf exons.chr21.bed.vcf || echo "files are different"
				cmp -s cache/processed_pseudogene.chr21.bed.vcf.png processed_pseudogene.chr21.bed.vcf.png || echo "files are different"
			-So this says they are different, but they are the same.
				diff cache/exons.chr21.bed.vcf.png exons.chr21.bed.vcf.png
					-This probs doesnt work with the binary commands
			-Where the | | pipe is saying if they are different, you will echo the statement that they are different
				cmp --silent file1 file2 && echo '### SUCCESS: Files Are Identical! ###' || echo '### WARNING: Files Are Different! ###'
		C) you can also less the bed and vcf file in UNIX and randomly compared in python using the following code
	3.
		-They got some cool gene types here! I know what miRNAs are, but honeslty haven't heard of lncRNAs so I would be interested in just reading more about what that is. 
		-miRNAs are really cool because they serve cell functions that we haven't even really characterized, though we think that we might know they have some gene and even mRNA and protein regulatory wlements.
		-We also have some SICK protein coding mRNAs, so the exon regions that will then be changed into functional proteins. This is fascinating because they will have to undergo post-transcriptional regulation, but also are great to know for gene expression to ask questions about how some gene is expressed in the cell after some change, or how that expression changes over time. 
		-Also, what is the point of a pseudogene if it isn't being post-translationally modified? Like, it's just chillin there, while the other ones are being made into proteins and such. So makes me wonder if it is some sort of way for he cell to buffer from RNA degrading proteins or such... interesting.

#Exercise 2: Changing the code
	1. Improve individual plots e.g. log scale, same y-axis, title
		-Setting a log scale
			ax.set_yscale("log")
	
		-Setting the same y-axis
			ax.set_ylim(0,(1e-2))
				Though I am not sure this is the same for all of them, but here we are lol
				
		-Adding axis titles
			ax.set_ylabel("log of ____")
			ax.set_xlabel("Position")
		
		-Adding main title
			ax.set_title(vcf)
				To set to the name of the vcf file we are inporting, and I am sure you could take out the vcf part. 
				
		-
#Exercise3: Create documentation

	Add documentation for bxlab/cmdb-plot-vcfs in day4-lunch/README.md including:

	Synopsis – <50 words
		#Using the do_all.sh , we are parsing the random_snippet.vcf file to create vcf files and plots for gene types. These plots look at the frequency of the count of alternate alleles compared to the count. 
	Usage – syntax including input file requirements
	#The entire syntax workflow:

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
		GTF=$1
		CHR=chr21
		
		if [ ! -f $CHR.gtf ]
		then
		    echo "--- Creating $CHR.gtf"
		    grep -w $CHR $GTF > $CHR.gtf
		fi
		
		for TYPE in lncRNA protein_coding processed_pseudogene
		do
		    echo "--- Creating $TYPE.$CHR.bed"
		    grep $TYPE $CHR.gtf | awk 'BEGIN {OFS="\t"}{if ($3=="gene"){print $1, $4-1, $5}}' > $TYPE.$CHR.bed
		done
		
		echo "--- Creating exons.$CHR.bed"
		grep "lncRNA" $CHR.gtf | awk 'BEGIN {OFS="\t"}{if ($3=="exon"){print $1, $4-1, $5}}' > exons.$CHR.bed
		

		echo "*** Subsetting .vcf for each feature"
		#For each bed file in the directory
		for TYPE in *.bed
		do
		
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

		import sys
		import numpy as np
		import matplotlib.pyplot as plt
		
		vcf = sys.argv[1]
		fs = open( vcf )
		
		ac = []
		for i, line in enumerate( fs ):
		    if "#" in line:
		        continue
		    fields = line.split()
		    info = fields[7].split(";")
		    ac.append( int(info[0].replace("AC=","")) )
			
		fig, ax = plt.subplots()
		ax.hist( ac, density=True )
		ax.set_yscale("log")
		#ax.set_ylim(1,(1e-2))
		ax.set_ylabel("log(frequency of the alternate alleles count)")
		ax.set_xlabel("AC (Count of alternate alleles in called genotypes)")    
		ax.set_title(vcf)
		
		#plt.show()
		
		fig.savefig( vcf + ".png" ) #we are now making out own plots
		#plt.savefig("lncRNA.chr21.bed.vcf.png")
		#plt.close(fig)
		
		fs.close()

	Dependencies – software requirements
		bash:
		python: 3.9.7
		matplotlib.pyplot: 3.5.1
			#pip show PROGRAM_NAME
		numpy: 1.22.3
	
	
	Description – how it works (bullet points or prose)
	#We require a single input .vcf file to then create a .bed files for features of interest.
		#In this case, we are interested in subsetting the regions by gene types.
	#To subset the regions of the inputted .vcf file by types, we run the subset_regions.sh script.
		#In subset_region.sh, we create a gtf, which we can then search for different gene types and create bed files for each different gene type of interest.
		#We pull out information for the gene type of interest and set the columns to [0], and then
		#we remove non-codon protein regions of our gene types of interest.
	#This output exons.$CHR.bed file is then piped back into do_all.sh .
		#The .bed file for the exons of the gene type of interest is subset into a .vcf file after sorting, merging and intersecting.
		#Lastly, the .vcf file is piped into the python plot_vcf_ac.py
	#In python plot_vcf_ac.py:
		#The file lines are enumerated for "AC", the allele count.
		#The data is plotted in a histogram, which shows the "AC" as the x-axis, and the log of the frequency of the alternate alleles count for the y-axis.
		#This data tells us the count of rare alleles across genotypes
	
	Output – example output
	#For instance, when looking to plot variations in lncRNA exons in chromosome 21, one would change the subset_region to create a bed file searching for lncRNAs, and generate an output as such:
	#This figure can be accessed either in the cmdb-plot-vcfs/cache directory for $TYPE.png
