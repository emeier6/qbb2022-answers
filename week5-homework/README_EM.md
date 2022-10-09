# Step 1: Filtering reads

	# Files: D2_Sox2_R1.bam   |   D2_Sox2_R2.bam  |   D2_Sox2_R1_input.bam    |   D2_Sox2_R1_input.bam

	# samtools view -b -q 10 D2_Sox2_R1.bam > q10_D2_Sox2_R1.bam
	# samtools view -b -q 10 D2_Sox2_R1_input.bam > q10_D2_Sox2_R1_input.bam
	# samtools view -b -q 10 D2_Sox2_R2.bam > q10_D2_Sox2_R2.bam
	# samtools view -b -q 10 D2_Sox2_R2_input.bam > q10_D2_Sox2_R2_input.bam
	



# Step 2: Calling peaks
	## Directory R1 for R1 and Input
	## Directory R2 for R2 and Input
	#Chromosome length: chr17	94987271 for -c
	# -B
	# Whether or not to save extended fragment pileup, and local lambda tracks (two files) at every bp into a bedGraph file. DEFAULT: False
	
	# macs2 callpeak -t q10_D2_Sox2_R1.bam -c q10_D2_Sox2_R1_input.bam -g 94987271 --outdir R1 -B
	
	# macs2 callpeak -t q10_D2_Sox2_R2.bam -c q10_D2_Sox2_R2_input.bam -g 94987271 --outdir R2 -B


# Step 3: Intersecting peaks
	# NA_peaks.narrowPeak    contains the peak in BED format
	# _treat_pileup.bdg and control_lambda.bdg  include chromosome, start and stop position, and the normalized number of reads covering the bases in that range 
	# bedtools intersect -a R1/NA_peaks.narrowPeak -b R2/NA_peaks.narrowPeak -bed > input_peaks
	


# Step 4: Colocalization of Sox2 and Klf4
	# wc -l input_peaks
	# #OUTPUT: 593
	
	#Combined sox and KLF4 intersections at chromosome 17:
	bedtools intersect -a input_peaks -b D2_Klf4_peaks.bed|wc -bed > KLF4_combined_peaks.bed
	
	#OUTPUT: 40     400    2751
	#40 total peaks
	
	# wc -l D2_Klf4_peaks.bed
	# #OUTPUT = 60
	
	#Percentage = 40 / 60 = ~66.666%

# Step 5: Plot
	#Bedgraph scaling: 3 graphs:
	# D0_H3K27ac_treat.bdg, D2_H3K27ac_treat.bdg, D2_Klf4_treat.bdg
	# Scaling:
	python scale_bdg.py R1/NA_treat_pileup.bdg scaled_R1_NA_treat_pileup.bdg
	python scale_bdg.py R1/NA_control_lambda.bdg scaled_R1_NA_control_lambda.bdg
	python scale_bdg.py R2/NA_treat_pileup.bdg scaled__R2_NA_treat_pileup.bdg
	python scale_bdg.py R2/NA_control_lambda.bdg scaled__R2_NA_control_lambda.bdg
	
	# Cropping:
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_R1_NA_treat_pileup.bdg > cropped_scaled_R1_NA_treat_pileup.bdg
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_R1_NA_control_lambda.bdg > cropped_scaled_R1_NA_control_lambda.bdg
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled__R2_NA_treat_pileup.bdg > cropped_scaled__R2_NA_treat_pileup.bdg
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled__R2_NA_control_lambda.bdg > cropped_scaled__R2_NA_control_lambda.bdg
	
	
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D0_H3K27ac_treat.bdg > cropped_scaled_D0_H3K27ac_treat.bdg
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D2_Klf4_treat.bdg > cropped_scaled_D2_Klf4_treat.bdg
	awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' scaled_D2_H3K27ac_treat.bdg > cropped_scaled_D2_H3K27ac_treat.bdg
	
	# Plotting:
	# R2_x =
	# for each position in the x part of the dictionary, we will split by period, assign the left part as X, the right part as a Y, and plot those values individually
	# Test run
	# cropped_scaled__R2_NA_treat_pileup.bdgx
	R2_treat = bdg_loader.load_data("cropped_scaled__R2_NA_treat_pileup.bdg")
	# print(R2_treat)
	# R2_treat = exec(open("bdg_loader.py").read("cropped_scaled__R2_NA_treat_pileup.bdg"))
	# This is a dictionary:
	R2_x = R2_treat['X']
	R2_y = R2_treat['Y']
	
	# cropped_scaled_D0_H3K27ac_treat.bdg
	Day0_H3K27ac = bdg_loader.load_data("cropped_scaled_D0_H3K27ac_treat.bdg")
	D0_K3K_x = Day0_H3K27ac['X']
	D0_K3K_y = Day0_H3K27ac['Y']
	
	# cropped_scaled_D2_H3K27ac_treat.bdg
	Day2_H3K27ac = bdg_loader.load_data("cropped_scaled_D2_H3K27ac_treat.bdg")
	D2_K3K_x = Day2_H3K27ac['X']
	D2_K3K_y = Day2_H3K27ac['Y']
	
	# cropped_scaled_D2_Klf4_treat.bdg
	Klf4 = bdg_loader.load_data("cropped_scaled_D2_Klf4_treat.bdg")
	Klf4_x = Klf4['X']
	Klf4_y = Klf4['Y']
	
	# Axis plottin
	fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, ncols=1)
	#
	ax0.bar(R2_x, R2_y, width = 100, color = 'red')
	ax0.set_xlabel("Position")
	ax0.set_ylabel("Reads")
	ax0.set_title("Sox2 R2 treat pileup")
	#
	ax1.bar(Klf4_x, Klf4_y, width = 100, color = 'orange')
	ax1.set_xlabel("Position")
	ax1.set_ylabel("Reads")
	ax1.set_title("Klf4")
	#
	ax2.bar(D0_K3K_x, D0_K3K_y, width = 100, color = 'green')
	ax2.set_xlabel("Position")
	ax2.set_ylabel("Reads")
	ax2.set_title("Day 0 H2K27ax")
	#
	ax3.bar(D2_K3K_x, D2_K3K_y, width = 100, color = 'blue')
	ax3.set_xlabel("Position")
	ax3.set_ylabel("Reads")
	ax3.set_title("Day 2 H2K27ax")
	
	plt.tight_layout()
	# plt.show()
	
	plt.savefig("track_figure.png")
	plt.close(fig)
	
# Part 2. Motif discovery using 
	#sort intersected by the 5th column 
	#sort by 5th column, and then do the awk command to compile the first 300
	sort -k 5,5rn input_peaks | head -300 | awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > formatted_intersect
	#in the fasta file, align with the formatted intersect compiled file to output as this motif mouse
	samtools faidx mm10.fa -r formatted_intersect > motif_disc_mouse
	
	
	# conda activate meme
	# conda install -c conda-forge openmpi=4.1.4 -y
	meme-chip -maxw 7 motif_disc_mouse 
	
	# conda deactivate

# Part 3. Motif identification
	
	cp ~/Downloads/motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme .
	
	tomtom memechip_out/combined.meme HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
	cd tomtom_output
	wc -l tomtom.tsv
	# OUTPUT: 164
	open tomtom.html
	- 2 motifs for Klf4
	- 2 motifs for Sox2
	
	grep "KLF4" tomtom.tsv > KLF4
		1	KLF4_MOUSE.H11MO.0.A	6	2.46197e-06	0.00130731	0.00140557	GGGTGGG	TGGAGTGGGTGTGGC	+
		2	KLF4_MOUSE.H11MO.0.A	2	6.58596e-07	0.000349714	0.000169664	CCCACCC	GCCACACCCACTCCA	-
	
	grep "SOX2" tomtom.tsv > SOX2
		3	SOX2_MOUSE.H11MO.1.A	3	4.32116e-08	2.29453e-05	4.48184e-05	CTTTGTT	TTCCTTTGTTCTG	+
		3	SOX2_MOUSE.H11MO.0.A	2	9.04075e-06	0.00480064	0.00156282	CTTTGTT	TCCTTTGTTATGCAAA	+