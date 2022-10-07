# Week 4: Homework

# Step 1: Output (at least) the top 10 principal components
	(bash) plink --vcf genotypes.vcf --pca 10
	#OUTPUT: eigenvals and eigenvecs and nosex
	
	# Plotting first two components:
	import sys
	import numpy as np
	import matplotlib.pyplot as plt  
	# Using the eigenvector - gives the first 10 values. So for each row, we are going to select the third (2) and fourth (4) values to plot. Wow, figuring it out!! :,^)

	eigenvec = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["Sample", "Sample", "PCA1", "PCA2", "PCA3", "PCA4", "PCA5", "PCA6", "PCA7", "PCA8", "PCA9", "PCA10"])
	eigenval = np.genfromtxt("plink.eigenval")

	#CHECK:print(eigenvec)
	## Plot PCA1 versus PCA2

	fig, ax = plt.subplots(nrows=1)
	##ax is the subplot
	ax.scatter(eigenvec["PCA1"], eigenvec["PCA2"], label = "Comp. PCA1 to PCA2")
	ax.set_ylabel("PCA2")
	ax.set_xlabel("PCA1")
	ax.legend()
	#CHECK:
	plt.show()
	#LOOKS GREAT OMG :,^) Figuring it out all by myself!
	

# Step 2: Pulling out allelic frequencies and making a histogram plot
	(bash) plink --vcf genotypes.vcf --freq
	##OUTPUT: plink.frq
	
	##Plotting allelic frequencies

	allelic_freq = np.genfromtxt("plink.frq", dtype = [int, str, str, str, float, int], encoding = None, names = ["Chr", "SNP", "A1", "A2", "MAF", "NCHR0BS"])
	#CHECK: 
	#print(allelic_freq["MAF"])
	#Plotting from 0 to 300

	ax.hist(allelic_freq["MAF"])
	ax.set_ylabel("Frequency")
	ax.set_xlabel("Allelic frequency")
	#plt.show()
	#CHECK: 
	#looks great! Wow, did it again on a roll B)

	plt.savefig("Allelic_frequencies")

# Step 3: Plink
	#(bash) plink --vcf genotypes.vcf --pheno CB1908_IC50.txt --pca 10 --allow-no-sex --assoc 
	#(bash) plink --vcf genotypes.vcf --pheno GS451_IC50.txt --pca 10 --allow-no-sex --assoc
	
# Step 4: Manhattan plotting
	association = np.genfromtxt("plink.qassoc", dtype = [int, str, int, str, float, float, float, float, float], encoding = None, names = ["Chr", "SNP", "BP", "NMISS", "BETA", "SE", "R2", "T", "P"])

	y = -np.log10(association["P"])
	x = np.arange(0, len(association["BP"]))

	ax.scatter(x, y, label = "P-values")
	ax.set_ylabel("-log10(P-value)")
	ax.set_xlabel("SNVs across chromosomes")
	plt.show()


# Step 5: Color coding
	fig, ax = plt.subplots(nrows=1)
	association = np.genfromtxt("plink.qassoc", dtype = [int, str, int, str, float, float, float, float, float], encoding = None, names = ["Chr", "SNP", "BP", "NMISS", "BETA", "SE", "R2", "T", "P"])
	pvalue = association["P"]
	y = -np.log10(association["P"])
	x = np.arange(0, len(association["BP"]))
	threshold = 10e-5
	cols = []
	for i in pvalue:
	    if i < threshold:
	        cols.append("magenta")
	    else:
	        cols.append("cyan")
        
	ax.scatter(x, y, label = "P-values", c=cols)
	ax.set_ylabel("-log10(P-value)")
	ax.set_xlabel("SNVs across chromosomes")
	plt.show()
	
	fig, ax = plt.subplots(nrows=1)
	association = np.genfromtxt("qassoc.CB1908", dtype = [int, str, int, str, float, float, float, float, float], encoding = None, names = ["Chr", "SNP", "BP", "NMISS", "BETA", "SE", "R2", "T", "P"])
	pvalue = association["P"]
	y = -np.log10(association["P"])
	x = np.arange(0, len(association["BP"]))
	threshold = 10e-5
	cols = []
	for i in pvalue:
	    if i < threshold:
	        cols.append("magenta")
	    else:
	        cols.append("cyan")
        
	ax.scatter(x, y, label = "P-values", c=cols)
	ax.set_ylabel("-log10(P-value)")
	ax.set_xlabel("SNVs across chromosomes")
	#plt.show()
	plt.savefig("association-pval-CB1908")
	
# Step 6: For the top associated SNP, visualize the effect size 


	# Looking at CB1908
	# print(association)
	min = np.argmin(pvalue)
	#print(min) = 188404

	print(association[min][1])
	# rs10876043


	parsed_vcf = parse_vcf("genotypes.vcf")[1:]
	snv = rs10876043

	# samples = genotypes[:,9]
	genotypes = parsed_vcf[]

	rs_index = []
	for row in parsed_vcf:
	    if row[2] == 'rs10876043':
	        rs_index.append(row)
    
	print(rs_index)
	##OMFG I GOT IT ON MY OWN. Understanding syntax now!! Only took me an hour :,^) but progress!!

	homdom = []
	het = []
	homrecess = []
	counter0 = 0
	counter1 = 0
	counter2 = 0
	counter3 = 0

	for i in rs_index:
	    if i == './.':
	        counter0 =+ 1
	        continue
	    elif i == '0/0':
	        counter1 =+ 1
	        homrecess.append()
	    elif i == '0/1' and i == '1/0':
	        counter2 =+ 1
	        het.append()
	    elif i == '1/1':
	        counter3 =+ 1
	        homdom.append()
	    # else:
	#         continue
	print(homdom)        
	print(counter)