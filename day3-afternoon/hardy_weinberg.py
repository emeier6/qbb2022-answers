#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

from vcfParser import parse_vcf
#same as: vcfParser.parse() and
#import vcfParser

#make a list for allele frequency
af_list = []
#make a list for genotype frequencies
gt00_list = []
gt01_list = []
    #this will store all the heterozygotes at 01 and 10
gt11_list = []
#rand snippets at 10000 variants, so list should have that many too

fname = sys.argv[1]
#file name command line argument
vcf = parse_vcf(fname)
#already noted parse_vcf, rename and putting every element into the list



#CHECK: print(vcf[1])
    #shows us that vcf[1] is the list of all the different field, end is genotypes

for i in range(1, len(vcf)):
    snp = vcf[i]
    #8th field or 7th is a large dictionary with key as '__' : value
    af_list.append(snp[7]["AF"])
    #CHECK: print(snp[7]["AF"])
        #key in []
    #append the list, list appending is af_list and adding with append
    gt00_count = 0
    gt01_count = 0
    gt11_count = 0
    #resetting every time you encounter a new SNV
    #need another loop to integrate through the field of a given SNV    
    for j in range(9, len(snp)):
        #looking in the vcf file, we see the 10th position starts 0|0, so we label in python as 9th position through the length of the snp, whcih snp = vcf[i]
        if (snp[j] == "0|0"):
            gt00_count += 1
        elif (snp[j] == "0|1" or snp[j] == "1|0"):
            gt01_count += 1
        elif (snp[j] == "1|1"):
            gt11_count += 1
        #set up each of the conditions with if or elif fopr the other possibilities... could also be something else...
    #gt00_count = gt00_count / 2548
    #gt01_count = gt01_count / 2548        
    #gt11_count = gt11_count / 2548
        #now, we want to see the fractions of the counts out of the total number of people
    #adding the fraction of the counts to the total number of people in the lists with the genome fractions
    gt00_list.append(gt00_count / 2548)
    gt01_list.append(gt01_count / 2548)
    gt11_list.append(gt11_count / 2548)

#print(gt00_list)
#python hardy_weinberg.py random_snippet.vcf | less -S

#parse_vcf(fname)



#creating a figure with axes
fig, ax = plt.subplots()

#ax.plot(af_list, gt00_list, label = "Hom. Ref")
#ax.plot(af_list, gt01_list, label = "Het.")
#ax.plot(af_list, gt11_list, label = "Hom. Alt")
    #incorrect as a line plot lmao
ax.scatter(af_list, gt00_list, label = "Hom. Ref")
ax.scatter(af_list, gt01_list, label = "Het.")
ax.scatter(af_list, gt11_list, label = "Hom. Alt")   

ax.set_ylabel("Genotype frequency")
ax.set_xlabel("Allele frequency")    

ax.legend()
#plt.show()



#adding theoretical expectations as black dashed lines with width of two 
x = np.arange(0.0, 1.0, 0.01)
home_ref = x**2
het = 2 * x * (1 - x)
home_alt = (x - 1)**2
#** = squared
ax.plot(x, home_ref, lw = 2, color = "black", linestyle = "dashed")
ax.plot(x, het, lw = 2, color = "black", linestyle = "dashed")
ax.plot(x, home_alt, lw = 2, color = "black", linestyle = "dashed")

plt.show()
 


