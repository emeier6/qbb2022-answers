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