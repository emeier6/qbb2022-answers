#!/usr/bin/env python3

#FILE USE LOCATION: /Users/cmdb/data/vcf_files/ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz

    #LOOK at file:
        #gzcat ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz | head

## RUNNING PLINK
    #open plink in bash, running in base terminal    
    #plink
        #Just by itself, needs command :)
        #Genotype data format, PCA can run in any program
            #get data in numeric, so vcf to parse and then convert to 0 1 and 2, python can do it in psychic (using PCA to convert into numberss)
    #make the gz into vcf file with --vcf
    #look at the pca only first 3 columns with -- pca 3
    #--vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3
        #converts genotypes to 1, 2, 3 (het, hom rec, hom alt)
        #extracts a line from multidimensional space


#OUTPUT: Results saved to plink.eigenval and plink.eigenvec .
import sys
import numpy as np
import matplotlib.pyplot as plt   

#fname = sys.argv[1]
#PCA coordinates from each sample stored in eigenvec
    #In linear algebra terms, these are the first and second eigenvectors of the covariance matri

    #figuring out what to name in eigenvec
        #Step 1: 
            #less -S plink.eigenvec
        #Step 1:
            #Name the eigen values, which there are 5 
                #columns 1 and 2 are the same ID 
                #Column 3 = PCA1
                #Column 4 = PCA2
                #Column 5 = PCA3

eigenvec = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["Sample", "Sample", "PCA1", "PCA2", "PCA3"])
#eigenval = np.genfromtxt("plink.eigenval")


#CHECK:print(eigenvec)

## Plot PCA1 versus PCA2


fig, ax = plt.subplots(nrows=1)

#ax is the subplot
#ax[0].scatter(eigenvec["PCA1"], eigenvec["PCA2"], label = "Comp. PCA1 to PCA2")
#ax[0].set_ylabel("PCA2")
#ax[0].set_xlabel("PCA1")    
#ax.legend()

#CHECK:plt.show()
    #LOOKS GREAT OMG :,^)


#SAVING PCA1 to PCA2 AS A FIGURE:


#plt.savefig("FILENAMETOSAVETO")
    #need to denote as.png or .pdf, which ever file makes the most sense
#plt.savefig("ex2_a.png")
#plt.close(fig)


ax.scatter(eigenvec["PCA1"], eigenvec["PCA3"], label = "Comp. PCA1 to PCA3")   
ax.set_ylabel("PCA3")
ax.set_xlabel("PCA1")    
#ax.legend()
#CHECK:
#plt.show()
    #SHE GORGEOUS

#RUNNING IN BASH: python plink.py ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz 



plt.savefig("ex2_b.png")
plt.close(fig)

#OUTPUT: These two files are now saved as "ex2_1.png" and "ex2_b.png" and uploaded into github

#sort each file, save each file differently
    #might need to make sure it's tab deliminated
    #unix command tr:
        #translates characters and take one character 
        #tr " " "\t" FILENAME
    #unix command sed:
        #stream editor, 
#then join
