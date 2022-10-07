#!/usr/bin/env python3

# (bash) plink --vcf genotypes.vcf --pca 10

import sys
import numpy as np
import matplotlib.pyplot as plt  
from vcfParser import *
# from pandas import DataFrame
# from scipy.stats import uniform
# from scipy.stats import randint

# Using the eigenvector - gives the first 10 values. So for each row, we are going to select the third (2) and fourth (4) values to plot. Wow, figuring it out!! :,^)

#
# eigenvec = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["Sample", "Sample", "PCA1", "PCA2", "PCA3", "PCA4", "PCA5", "PCA6", "PCA7", "PCA8", "PCA9", "PCA10"])
#
# eigenval = np.genfromtxt("plink.eigenval")
#
#
# #CHECK:print(eigenvec)
#
# ## Plot PCA1 versus PCA2
#
#
# #
# # ##ax is the subplot
# # ax.scatter(eigenvec["PCA1"], eigenvec["PCA2"], label = "Comp. PCA1 to PCA2")
# # ax.set_ylabel("PCA2")
# # ax.set_xlabel("PCA1")
# # ax.legend()
#
# #CHECK:
# #plt.show()
# #LOOKS GREAT OMG :,^)
# #plt.savefig("PCA1_v_PCA2")
#
#
#
# ## Allelic frequencies
# #(bash) plink --vcf genotypes.vcf --freq
#     ##OUTPUT: plink.frq
#
# ##Plotting allelic frequencies
#
# allelic_freq = np.genfromtxt("plink.frq", dtype = [int, str, str, str, float, int], encoding = None, names = ["Chr", "SNP", "A1", "A2", "MAF", "NCHR0BS"])
# # #CHECK:
# #print(allelic_freq["MAF"])
# #Plotting from 0 to 300
#
# ax.hist(allelic_freq["MAF"])
# ax.set_ylabel("Frequency")
# ax.set_xlabel("Allelic frequency")
#plt.show()
#CHECK: 
#looks great! Wow, did it again on a roll B)

#plt.savefig("Allelic_frequencies")


#(bash) plink --vcf genotypes.vcf --pheno CB1908_IC50.txt --pca 10 --allow-no-sex --assoc > qassoc.CB1908

#(bash) plink --vcf genotypes.vcf --pheno GS451_IC50.txt --pca 10 --allow-no-sex --assoc > qassoc.GS451



fig, ax = plt.subplots(nrows=1)

test = np.genfromtxt("plink.qassoc", skip_header = 1, dtype = str)
# print(test)

association = np.genfromtxt("plink.qassoc", skip_header = 1, dtype = str )
# print(association)

# names = ["CHR", "SNP", "BP", "NMISS", "BETA", "SE", "R2", "T", "P"]

pvalue = association[:,8].astype(float)

y = -np.log10(pvalue)
x = np.arange(0, len(association[:,2]))

print(pvalue)
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

# ymax = min(pvalue)
# print(ymax)

# plt.show()

# plt.savefig("association-pval-CB1908")



# Looking at CB1908
# print(association)
min = np.argmin(pvalue)
#print(min) = 188404

print(association[min][1])
# rs10876043


parsed_vcf = parse_vcf("genotypes.vcf")[1:]
# print(parsed_vcf)
# snv = np.where(parsed_vcf[rs10876043])
# print(snv)
# samples = genotypes[:,9]
# genotypes = parsed_vcf[]

# print(parsed_vcf[:][2])

homdom = []
het = []
homrecess = []
counter0 = 0
counter1 = 0
counter2 = 0
counter3 = 0

for row in parsed_vcf:
    for i in row:
        # print(i)
        if i == "rs10876043":
             if parsed_vcf[9:] == "./.":
                 counter0 =+ 1
                 continue
             elif genotypes[9:] == "0/0":
                 counter1 =+ 1
                 homrecess.append()
             elif genotypes[9:] == "0/1" and "1/0":
                 counter2 =+ 1
                 het.append()
             elif genotypes[9:] == "1/1":
                 counter3 =+ 1
                 homdom.append()
         else:
             continue
           
        # homrecess.append(parsed_vcf[9:] == "0/0")
        # het.append(parsed_vcf[9:] == "0/1" and "1/0")
        # homrecess.append(parsed_vcf[9:] == "1/1")

    
  
print(homdom)        

