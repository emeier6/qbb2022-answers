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
	head bins.1.fa 
	grep ">" bins.1.fa | cut -f 2 | sort | uniq -c | sort | less -S
	#   OUTPUT:
	   1 >NODE_15_length_235270_cov_153.562668
	   1 >NODE_19_length_199764_cov_200.017410
	   1 >NODE_31_length_114355_cov_167.687393
	   1 >NODE_396_length_21162_cov_170.926423
	   1 >NODE_3_length_498518_cov_181.760000
	   1 >NODE_48_length_91091_cov_192.361330
	   1 >NODE_5_length_427301_cov_143.861656
	   1 >NODE_90_length_68573_cov_147.031802
	   
	grep NODE_15_length_235270_cov_153.562668 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin1.1.txt
	   #root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Finegoldia;Finegoldia magna;Finegoldia magna ATCC 29328
	grep NODE_19_length_199764_cov_200.017410 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin1.2.txt
	   #root;cellular organisms;Bacteria;Terrabacteria group
	grep NODE_31_length_114355_cov_167.687393 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin1.3.txt
	   #Streptococcus anginosus;Streptococcus anginosus C238
	grep NODE_396_length_21162_cov_170.926423 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin1.4.txt
	   #root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Clostridia;Clostridiales;Clostridiaceae;Clostridium;Clostridium novyi;Clostridium novyi NT
	grep NODE_3_length_498518_cov_181.760000 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin1.5.txt
	   #root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548
	grep NODE_48_length_91091_cov_192.361330 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin1.6.txt
		#root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Finegoldia;Finegoldia magna;Finegoldia magna ATCC 29328
	grep NODE_5_length_427301_cov_143.861656 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin1.7.txt
	   #root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548
	grep NODE_90_length_68573_cov_147.031802 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin1.8.txt
	   #root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Clostridia;Clostridiales;Clostridiaceae;Clostridium
	   
	
	
	* There must be a faster way to do this... or imma go crazy :^)   
	   
	   
	while read p; do grep p assembly.kraken; done < ~/qbb2022-answers/week14-homework/bins_dir/bins.2.fa | cut -f 2 | sort | uniq -c | sort 
	while read p; do grep p assembly.kraken; done < ~/qbb2022-answers/week14-homework/bins_dir/bins.2.fa | cut -f 2 | uniq -c | sort 
	
	
	I am really tired and the previous code is taking ages to run :( Eventhough that should be a solid grep loop, and I really don't want to go through every single pull from each bin and comment :(((
		
		
	But I am fighting my demons with this for loop so I just might :(
		Alright, we ballin, it has been 15 minutes with the previous while loop code and it still hasnt run so here we go :,|
	
	grep ">" bins.2.fa | cut -f 2 | sort | uniq -c | sort | less -S	
	NOOOOOOOOOOOOOOO WHY ARE THERE SO MANY
	
	uhhh
	 
	 hmm. 
	 
	grep ">" bins.3.fa | cut -f 2 | sort | uniq -c | sort | less -S	
	I am sad and not feeling smart, but there is literally nothing online that can help me. I am dumb. 
	
	grep ">" bins.4.fa | cut -f 2 | sort | uniq -c | sort | less -S	
	Thank GOD there are only 3 :,^)
	#OUtput:
		1 >NODE_108_length_61778_cov_2570.223936
		1 >NODE_10_length_279092_cov_2597.445937
		1 >NODE_8_length_298793_cov_2547.011572
	
	grep NODE_108_length_61778_cov_2570.223936 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin4.1.txt
	#Root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis OG1RF
	grep NODE_10_length_279092_cov_2597.445937 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin4.2.txt
	# root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis D32
	grep NODE_8_length_298793_cov_2547.011572 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin4.3.txt
	# root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis str. Symbioflor 1
	
	grep ">" bins.5.fa | cut -f 2 | sort | uniq -c | sort | less -S	
	#OUTPUT:
	1 >NODE_11_length_278925_cov_118.155370
	1 >NODE_13_length_256100_cov_129.382675
	1 >NODE_17_length_211501_cov_125.925508
	1 >NODE_186_length_42458_cov_125.041955
	1 >NODE_18_length_205318_cov_122.610529
	1 >NODE_208_length_37864_cov_119.516332
	1 >NODE_240_length_34172_cov_118.910836
	1 >NODE_269_length_31863_cov_127.044831
	1 >NODE_4_length_455101_cov_112.371015
	1 >NODE_6_length_320041_cov_123.475336
	1 >NODE_7_length_310076_cov_130.336474
	1 >NODE_9_length_293536_cov_118.600107
	:(((((((
		
	grep ">" bins.6.fa | cut -f 2 | sort | uniq -c | sort | less -S	
	1 >NODE_16_length_219929_cov_2350.909321
	1 >NODE_1_length_1447137_cov_2268.097092
	1 >NODE_2_length_556123_cov_2361.439230
	
	grep NODE_16_length_219929_cov_2350.909321 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin6.1.txt
	# root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis V583
	grep NODE_1_length_1447137_cov_2268.097092 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin6.2.txt
	# root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis OG1RF
	grep NODE_2_length_556123_cov_2361.439230 ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin6.3.txt
	# root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis V583
	
	
	(A) Within your README, record your predictions for each bin?
	Bin 1 is mosly Tissierellia and its subspeciees, and then some clostridia, and streptoccocus anginosus.
	Bin 2
	Bin 3
	Bin 4 is symbiofluor and E. faecalis, of 2 different strains. 
	Bin 5
	Bin 6 All E. faecalis.
	
	Please... i am so tired and this is too much work all because I can't write a while loop in bash without crashing my computer. Why am i so dumbbbbbbb
	Yo.. I can't submit my fa files that I made because I dont have permission??? I just made these omfl
	
	(B) This approach to classification is fast, but not very quantitative. Within your README, propose one method to more robustly infer the taxonomy of a metagenomic bin.
	Is it fast? But maybe looking at 16S signatures from sequenced data, which this is. Nevermind, maybe it is just faster to group them by larger taxonomy (ie: lactic acid or acetic acid bacteria).
	Maybe look at overlapping bins and see what is most prevalent? But that wouldn't be more sensitive. 
	Maybe, just doing the most abundant taxonomy sorting, or something like that. Surely one can do a ML tree of the most likely and abundant sequences and just call it more generally there. 
	
	Idk man, I am tired. Thank yall TAs for carrying us through this semester. I appreciate you all!
	
	