#!/usr/bin/env python3
import matplotlib.pyplot as plt   
import numpy as np
    #importing packages


#np.random.seed(42)    
    #setting a seed data to allow for reproducibility (if study includes generating random data)
    #essentially, a random number generator from the data, like data sampling 
   
   
    
#norm_data = np.random.normal(0, 1, int(1e6))
    #np.random.normal represents the bell-shaped typical distribution known as (Gaussian) distribution.
        #mean 0, std dev 1, 50 size of data or samples
        #naming the numpy random normally distributed data as norm_data
            #int(1e6) = 1 million
            #As distribution increases and the sample size increases, you get more normal distributions
        #Same as what we were doing in R all long ago, statistical confidence increases with more iterations of multiple random number sequence generations (seed) 




#plt.hist(norm_data, bins = 50)
    #histogram plotting of norm_data file (that is looking at normal distribution of 5 variables)
    #bins = how many categories there are 

#plt.show()
    #showing the file
    





################## Running bcftools ########################
########## SOME POP GEN STUFF ##############################

#conda create -n bcftools -y python=3 bcftools
#conda activate bcftools
#bcftools

    ###DIDNT WORK:
    
#conda deactivate
#conda create -n bcftools -y python=3 bcftools -c conda-forge
#conda activate bcftools
#bcftools

#Desired tool from bcftools?
    #query        transform VCF/BCF into user-defined formats
    #bcftools query -f 
        #will extract the '%POS\n' file.bcf
            #This will look for the POS and create a new line for each position
            #We are looking at allele freqs, so:
                #bcftools query -f "%AF\n" ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz > chr21_af.txt
                    #calling .txt for us to recognize only just a text file, so add .txt
                    #NOT a vcf file


## the new chr21_af.txt
    #wc -l = almost a million lines :^)
    
#conda deactivate to exit terminal
#    (bcftools) to (base)

snp_af = np.genfromtxt("chr21_af.txt")
#print(np.genfromtxt("chr21_af.txt"))
    #check to see that it downloaded well
        #OUTPUT: [0.   0.1  0.01 ... 0.   0.   0.03]
#print(snp_af.shape)
        #shape tells you the number of arrays loaded in, good other check
            #OUTPUT: (976599,)
plt.hist(snp_af, bins = 50)
    #Population is skewed left, kinda showing that there are a lot of unique SNPs, and there are many unique SNPs
        #Consequence of exploding population size = more variation in SNPs across populations. 
        #Could also be like, with climate change and as species go extinct, new species will enter the niches and also grow.
        #Converseley, one could imagine that if human populations shrink, we would see more alignments towards the right of the graph, and more similar SNPs
plt.show()
          
          
       
       
       
          
            
########## LAST IN CLASS EXERCISE ################################################

#file in use: gencode.v41.annotation.gtf.gz
#.gz is a compressed gtf file, and neds to be changed from binary/comp format to a workable format
    #look at with gzcat :^)
        #gzcat gencode.v41... | head #to get the first 10 lines
    
    #gzcat gencode.v41.annotation.gtf.gz | grep -v "^##" | cut -f 1 | sort | uniq -c > genes_per_chrom.txt
        #grep -v to undo the headers and exclude, ^ denotes at the beginning
        #cutting the first column and 
        #sorting by the first column
        #sorting by the number of unique variables
        #storing as a .txt because we are only extrapolating a few columns


#Now, plotting! :)
    #To plot, plot as a barchart because categories (chrom) and y = counts

#SEE: barchart.py    
        


    


