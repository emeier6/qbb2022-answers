#Make a copy of code and input data
cd
git clone https://github.com/bxlab/cmdb-plot-vcfs
cd cmdb-plot-vcfs
cp ~/data/vcf_files/random_snippet.vcf .
cp ~/data/gtf_files/gencode.v41.annotation.gtf.gz .
gunzip *.gz
	#NOW AS: gencode.v41.annotation.gtf

#Create a new conda environment with required software
conda create --name day4-lunch
conda activate day4-lunch
conda install bedtools matplotlib

	conda deactivate
    	#go back to base terminal
	conda activate day4-lunch
		#go into day4-lunch terminal
#Run workflow
bash do_all.sh random_snippet.vcf gencode.v41.annotation.gtf
