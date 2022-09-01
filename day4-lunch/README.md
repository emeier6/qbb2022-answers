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