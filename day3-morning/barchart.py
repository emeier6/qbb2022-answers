#!/usr/bin/env python3
import matplotlib.pyplot as plt   
import numpy as np

genes_per_chrom = np.genfromtxt("genes_per_chrom.txt", dtype = None, encoding = None, 
                names = ["gene_count", "chrom_name"])
    #reading in mixed types of data, IE: chromosome strings in second column and integers as first column
        #let numpy guess thre dtype and the encoding type by setting it as none
        #lastly, we will name our columns 
    
    
#print(genes_per_chrom)
    #OUTPUT: shows numbers (integers) as floats, and not reading the second column
        #to fix this, we tell numpy to guess with the dtype and the encoding
        
        #now, include names of the columns
print(genes_per_chrom["gene_count"])
    #to report only the gene counts and, 
print(genes_per_chrom["chrom_name"])
    #to report only the chromosome names
    
    
    
fig, ax = plt.subplots()

ax.bar(genes_per_chrom["chrom_name"], genes_per_chrom["gene_count"])
    #x and then y in the ax.bar

plt.show()