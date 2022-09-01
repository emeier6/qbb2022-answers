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
	1. Portion of do_all.sh output (not script) that reports how many bp each feature covers
	
	