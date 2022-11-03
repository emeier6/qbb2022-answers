Part 0:

# (bash) conda create -n medaka medaka
# (bash) sudo /usr/bin/xcode-select --install
# (bash) pip install whatshap==1.0
# (bash) conda activate medaka
# (bash) conda deactivate

# (bash) pip install whatshap==1.0
# (bash) cp /Users/cmdb/data/genomes/hg38.fa ./


# (bash) curl https://bx.bio.jhu.edu/data/msauria/cmdb-lab/ont_data.tar.gz --output ont_data.tar.gz
# (bash) tar xzf ont_data.tar.gz

# OUTPUT FILES:
# methylation.bam - your methylation-called reads
# methylation.bam.bai - the index for your bam file
# methylation.bed.gz - a compressed bed file containing methylation sites
# methylation.bed.gz.tbi - the index for the compressed bed file
# regions.bed - a bed file containing the regions that were used to filter the data and that you will be considering in this assignment
# region_genes.bed - a bed file containing genes for chromosomes 11, 14, 15, and 20


Part 1: Call and phase variant for each region
# Reference_fasta, inputs .hdf files, outputs .vcf
# -p for the regions 

# less -S regions.bed
    # chr11   1900000         2800000
    # chr14   100700000       100990000
    # chr15   23600000        25900000
    # chr20   58800000        58912000
# region_genes.bed = all genes with [chr, start, end, ensg, 0or1, +or-]
# phased.vcf contains region_genes.bed of regions.bed (where all these things align)

# calling methylation for specifc reads
# chr:start-end

## chr11:1900000-2800000
## (medaka) medaka_variant -f hg38.fa -i methylation.bam -r chr11:1900000-2800000 -p -t 6 -o chr11_phased
# DONE! And 15 files outputted :^)
#3 Output: chr11_phased


## chr14:100700000-100990000
# (medaka) medaka_variant -f hg38.fa -i methylation.bam -r chr14:100700000-100990000 -p -t 6 -o chr14_phased
## Done! 15 files output into the chr14_phased

## chr15:23600000-25900000
# (medaka) medaka_variant -f hg38.fa -i methylation.bam -r chr15:23600000-25900000 -p -t 6 -o chr15_phased
## Done! 15 files output into the chr15_phased

## chr20:58800000-58912000
# (medaka) medaka_variant -f hg38.fa -i methylation.bam -r chr20:58800000-58912000 -p -t 6 -o chr20_phased
## Done! 15 files output into the chr20_phased


Part 2: Mark reads with the correct haplotype tag

# Now haplotypes with whatshap haplotag for phasing genomic variants using DNA sequencing reads, also called read-based phasing or haplotype assembly
# Haplotypes refers to the two types of variants
# This will use the unphased and phased vcfs, probably needing indexing
# No output .gz file from the phased and unphased vcfs...
# TO FIX, RUNNING: (bash) cp /Users/cmdb/data/genomes/hg38.fa ./

# chr:start:end
# Chr_haplotagged is a BAM file
# chr11_list as a TSV file


# Chr11
# whatshap haplotag -o haplotagged.bam --output-haplotag-list chr11_list --reference ~/qbb2022-answers/week7-homework/hg38.fa round_0_hap_mixed_phased.vcf.gz methylation.bam	
# Done


# Chr14
# whatshap haplotag -o haplotagged.bam --output-haplotag-list chr14_list --reference ~/qbb2022-answers/week7-homework/hg38.fa round_0_hap_mixed_phased.vcf.gz methylation.bam	
# Done

# Chr15
# whatshap haplotag -o haplotagged.bam --output-haplotag-list chr15_list --reference ~/qbb2022-answers/week7-homework/hg38.fa round_0_hap_mixed_phased.vcf.gz methylation.bam	
# Done

# Chr20
# whatshap haplotag -o haplotagged.bam --output-haplotag-list chr20_list --reference ~/qbb2022-answers/week7-homework/hg38.fa round_0_hap_mixed_phased.vcf.gz methylation.bam	
# Done


Part 3: Split reads into two files based on their haplotype

# Haplotype sorting will output a reads.bam file for input here, and a haplotypes tsv
# Use whatshap split to split bam files for each haplotype variant from the generated list for each chromosome
# OUTLINE CODE: whasthap split --output-h1 h1.fastq.gz  --output-h2 h2.fastq.gz reads.bam haplotypes.tsv

# Chr11
# whatshap split --output-h1 chr11_h1.fastq.gz  --output-h2 chr11_h2.fastq.gz haplotagged.bam chr11_list
# Done with outputs as gz files:
# chr11_h1.fastq.gz
# chr11_h2.fastq.gz

# Chr14
# whatshap split --output-h1 chr14_h1.fastq.gz  --output-h2 chr14_h2.fastq.gz haplotagged.bam chr14_list
# Done with outputs as gz files:
# chr14_h1.fastq.gz
# chr14_h2.fastq.gz

# Chr15
# whatshap split --output-h1 chr15_h1.fastq.gz  --output-h2 chr15_h2.fastq.gz haplotagged.bam chr15_list
# chr15_h1.fastq.gz
# chr15_h2.fastq.gz

# Chr20
# whatshap split --output-h1 chr20_h1.fastq.gz  --output-h2 chr20_h2.fastq.gz haplotagged.bam chr20_list
# chr20_h1.fastq.gz
# chr20_h2.fastq.gz



# samtools cat chr11_phased/chr11_h1.fastq.gz chr14_phased/chr14_h1.fastq.gz chr15_phased/chr15_h1.fastq.gz chr20_phased/chr20_h1.fastq.gz -o h1_total.bam 
# samtools index h1_total.bam
# Index OUTPUT: h1_total.bam.bai

# samtools cat chr11_phased/chr11_h2.fastq.gz chr14_phased/chr14_h2.fastq.gz chr15_phased/chr15_h2.fastq.gz chr20_phased/chr20_h2.fastq.gz -o h2_total.bam 
# samtools index h2_total.bam
# Index OUTPUT: h2_total.bam.bai


Part 4: Setting up IGV

# Greating IGV environment and cloning the environment:
# (bash) conda deactivate
# (bash) conda create -n igv gradle openjdk=11 -y
# (bash) conda activate igv
# (bash) git clone https://github.com/igvteam/igv.git

# Building a program:
# Changing into the IGV directory
# (bash) cd igv
# (bash) ./gradlew createDist
# (bash) cd ../


# The NEW IGV Directory: igv/build/IGV-dist/igv.sh
# ln -s ${PWD}/igv/build/IGV-dist/igv.sh ./
# WHY?: if calling or wanting to work with IGV, then can use calling ./igv.sh


Part 5: Configuring IGV for differential methylation
# Vizualize the data 
# Color alignments by->base modification (5mC)




Part 6: Find and plot differentially methylated regions
# Find region of differentially regulated regions
# Load in the BAM files
# ls -lh


# File -> Save Image


Do you expect each region in H1 or H2 to correspond to the same parent of origin (i.e. the same haplotype)? Explain your reasoning.

- The H1 regions should correspond to one of the parents, while the H2 should correspond with the other parent. This is because there differnces in the probability in the base regions being methylated, <50% corresponding to the blue color, and >50% corresponding with red. If H1 and H2 came from the same parent, then they would be the same probability of methylation because of paired sequencis with high CpG repeats. This color scheme notes methylation differences between parents.