# Step 0: 
	curl -OL https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/metagenomics/extra_data/metagenomics_data.tgz
	tar -xzvf metagenomics_data.tgz
	
	metagenomics_data:
	step0_givendata: (Forward and Reverse Reads)
			SRR492183
			SRR492186
			SRR492188
			SRR492189
			SRR492190
			SRR492193
			SRR492194
			SRR492197
	step3_givendata:
		Bins
		
	step4_givendata:
		Genomic bins to the transcripts of interest
		
	
# Step 1A: Install Krona-Tools
	git clone https://github.com/marbl/Krona.git
	cd Krona/KronaTools/
	sudo ./install.pl

# Step 1B: Parse the KRAKEN output to convert it to a Krona-Tools compatible format
	python scriptname.py KRAKEN_sample_input_file.kraken sample_name
	python working.py KRAKEN_sample_input_file.kraken sample_name
	
	python working.py metagenomics_data/step0_givendata/KRAKEN/SRR492183.kraken SRR492183
	python working.py metagenomics_data/step0_givendata/KRAKEN/SRR492186.kraken SRR492186
	python working.py metagenomics_data/step0_givendata/KRAKEN/SRR492188.kraken SRR492188
	python working.py metagenomics_data/step0_givendata/KRAKEN/SRR492189.kraken SRR492189
	python working.py metagenomics_data/step0_givendata/KRAKEN/SRR492190.kraken SRR492190
	python working.py metagenomics_data/step0_givendata/KRAKEN/SRR492193.kraken SRR492193
	python working.py metagenomics_data/step0_givendata/KRAKEN/SRR492194.kraken SRR492194
	python working.py metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197
	

# Step 1C: Use Krona-tools
	ktImportText -q ~/qbb2022-answers/week14-homework/SRR492183_krona.txt ~/qbb2022-answers/week14-homework/SRR492186_krona.txt ~/qbb2022-answers/week14-homework/SRR492188_krona.txt ~/qbb2022-answers/week14-homework/SRR492189_krona.txt ~/qbb2022-answers/week14-homework/SRR492190_krona.txt ~/qbb2022-answers/week14-homework/SRR492193_krona.txt ~/qbb2022-answers/week14-homework/SRR492194_krona.txt ~/qbb2022-answers/week14-homework/SRR492197_krona.txtktImportText -q ~/qbb2022-answers/week14-homework/SRR492183_krona.txt ~/qbb2022-answers/week14-homework/SRR492186_krona.txt ~/qbb2022-answers/week14-homework/SRR492188_krona.txt ~/qbb2022-answers/week14-homework/SRR492189_krona.txt ~/qbb2022-answers/week14-homework/SRR492190_krona.txt ~/qbb2022-answers/week14-homework/SRR492193_krona.txt ~/qbb2022-answers/week14-homework/SRR492194_krona.txt ~/qbb2022-answers/week14-homework/SRR492197_krona.txt
	ktImportText -q SRR492186_krona.txt -o SRR492186.html
	ktImportText -q SRR492183_krona.txt -o SRR492183.html
	ktImportText -q SRR492189_krona.txt -o SRR492189.html
	ktImportText -q SRR492190_krona.txt -o SRR492190.html
	ktImportText -q SRR492193_krona.txt -o SRR492193.html
	ktImportText -q SRR492194_krona.txt -o SRR492194.html
	ktImportText -q SRR492197_krona.txt -o SRR492197.html
	
	Question 1: In your README, briefly comment on the trends you see in the gut microbiota throughout the first week.
	
	open SRR492186.html
	#Mostly E. faecalis, very little staph, and no actinobacteria
	open SRR492183.html
	#Lots of bacteria, predominantly Enterococcus faecalis for all, some actinobacteria, and some staphyloccocus epedermis. Some with smaller and slightly different amounts of bacteria, but generally all the same. 
	open SRR492189.html
	#Mostly the same as '86.
	open SRR492190.html
	#No actinobacteria, about 14% staph.
	open SRR492193.html
	#Teeny bit actinobacteria, about 17% staph, and mostly E. faecalis. Similar to '83
	open SRR492194.html
	#Mostly same as '93
	open SRR492197.html
	#HUGE amounts of actinobacteria compared to the others (27%), and 60% E. faecalis (Usially in the 80s-90s). Could be diseased state?
	

# Step 2: Deconvolute the assembled scaffolds into individual genomes (binning)
	Question 2: In your README, comment on what metrics in the contigs could we use to group them together?
	
	Contigs are contiguous fragments of DNA sequence from an incomplete draft genome.
	We have the forward and reverse sequences, which we can use longer sequences to better align to a genome. Short regions can be incorrectly assembled into one contig due to a short region of similar sequence.
	MetaBat2 is cool becauseFor each pair of contigs in a metagenome assembly, MetaBAT calculates their probabilistic distances based on tetranucleotide frequency (TNF) and abundance (i.e., mean base coverage), then the two distances are integrated into one composite distance. 
	All the pairwise distances form a matrix, which then is supplied to a modified k-medoid clustering algorithm to bin contigs iteratively and exhaustively into genome bins.
	So, we can bin by the most probable sequences in a genome assembly. 
	Deriving a distance to discriminate TNFs of different genomes can be calculated with Euclidean distance of the likelihood of inter- and intra-species genomes, doing so for which species we have databases and a regerence genome for. 
	


# Step 2A: Create an index of the assembly
	bwa index assembly.fasta
	

# Step 2B: Use bwa mem to map the reads from each sample to the assembly and samtools sort to create sorted bam output files
	bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492183_1.fastq metagenomics_data/step0_givendata/READS/SRR492183_2.fastq > SRR492183.sam
	bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492186_1.fastq metagenomics_data/step0_givendata/READS/SRR492186_2.fastq > SRR492186.sam
	bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492188_1.fastq metagenomics_data/step0_givendata/READS/SRR492188_2.fastq > SRR492188.sam
	bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492189_1.fastq metagenomics_data/step0_givendata/READS/SRR492189_2.fastq > SRR492189.sam
	bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492190_1.fastq metagenomics_data/step0_givendata/READS/SRR492190_2.fastq > SRR492190.sam
	bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492193_1.fastq metagenomics_data/step0_givendata/READS/SRR492193_2.fastq > SRR492193.sam
	bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492194_1.fastq metagenomics_data/step0_givendata/READS/SRR492194_2.fastq > SRR492194.sam
	bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492197_1.fastq metagenomics_data/step0_givendata/READS/SRR492197_2.fastq > SRR492197.sam
	
	
	samtools sort SRR492183.sam > SRR492183.bam
	samtools sort SRR492186.sam > SRR492186.bam
	samtools sort SRR492188.sam > SRR492188.bam
	samtools sort SRR492189.sam > SRR492189.bam
	samtools sort SRR492190.sam > SRR492190.bam
	samtools sort SRR492193.sam > SRR492193.bam
	samtools sort SRR492194.sam > SRR492194.bam
	samtools sort SRR492197.sam > SRR492197.bam
	

# Step 2C: Repair the metaBAT2 environment
	cp ~/miniconda3/envs/metabat2/lib/libdeflate.so ~/miniconda3/envs/metabat2/lib/libdeflate.0.dylib
	conda activate metabat2
	

# Step 2D: Run metaBAT2
	jgi_summarize_bam_contig_depths --outputDepth 183.txt SRR492183.bam
	jgi_summarize_bam_contig_depths --outputDepth 186.txt SRR492186.bam
	jgi_summarize_bam_contig_depths --outputDepth 188.txt SRR492188.bam
	jgi_summarize_bam_contig_depths --outputDepth 189.txt SRR492189.bam
	jgi_summarize_bam_contig_depths --outputDepth 190.txt SRR492190.bam
	jgi_summarize_bam_contig_depths --outputDepth 193.txt SRR492193.bam
	jgi_summarize_bam_contig_depths --outputDepth 194.txt SRR492194.bam
	jgi_summarize_bam_contig_depths --outputDepth 197.txt SRR492197.bam
	
	metabat2 -i assembly.fasta -a 183.txt -o bins_dir/bins
	metabat2 -i assembly.fasta -a 186.txt -o bins_dir/bins
	metabat2 -i assembly.fasta -a 189.txt -o bins_dir/bins
	metabat2 -i assembly.fasta -a 190.txt -o bins_dir/bins
	metabat2 -i assembly.fasta -a 193.txt -o bins_dir/bins
	metabat2 -i assembly.fasta -a 194.txt -o bins_dir/bins
	metabat2 -i assembly.fasta -a 197.txt -o bins_dir/bins
	
	Question 3A: In your README, answer: How many bins did you get?
	183.txt = 4 bins
	186.txt = 2 bins
	189.txt = 3 bins
	190.txt = 2 bins
	193.txt = 5 bins
	194.txt = 3 bins
	197.txt = 6 bins
	
	6 bins total = max number of bins
	
	Question 3B: In your README, comment on roughly what percentage of the assembly do they represent?
	grep ">" bins.*.fa | cut -d "_" -f 4 | paste -sd+ - | bc
	11965344
	grep -v ">" assembly.fasta | wc
	38708237
	
	Sure, our bins are 11965344 / 38708237, representing about 31% of the genome.
	
	Question 3C: In your README, comment on whether you think the sizes of each bin look about right, based on what you know about the size of prokaryotic genomes?
	grep -v ">" bins.1.fa | wc
	1683638
	#About 1/3rd	
	grep -v ">" bins.2.fa | wc
	1571294
	#About 1/3rd
	grep -v ">" bins.3.fa | wc
	3481100
	#This is much closer to the full genome size!
	grep -v ">" bins.4.fa | wc
	650325
	#Much less than 1/3, about 1/6th.
	grep -v ">" bins.5.fa | wc
	2518245
	#More than half
	grep -v ">" bins.6.fa | wc	
	2260243
	#More than half
	
	Question 3D:In your README, describe how you might estimate how complete and how contaminated each bin is?
	I could individually look at each bin with the grep -v ">" command, and compare each to the assembly.fasta.
	Based on the assembly fasta, the fewer number of regions (size compared to reference fasta), can tell me how corrupt the file is. 
	For instance, the file for bins.4.fa is about 1/6th the genome size of the assembly.fasta, therefore it is highly corrupt. 
	

# Step 3: Predict the taxonomic composition (genus/species) of your putative genomes
	grep NODE_14_length_235766_cov_39.967778 metagenomics_data/step0_givendata/KRAKEN/assembly.kraken
	
	bins.1.fa
	while read p; do grep p asembly.kraken; done < ~/qbb-answers/week14-homework/bin1 | cut -f 2 | sort | uniq -c | sort
	