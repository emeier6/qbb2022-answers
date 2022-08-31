#!/usr/bin/env python3
import matplotlib.pyplot as plt   
import numpy as np
    #importing packages

np.random.seed(42)    
    #setting a seed data to allow for reproducibility (if study includes generating random data)
    #essentially, a random number generator from the data, like data sampling 
    
norm_data = np.random.normal(0, 1, int(1e6))
    #np.random.normal represents the bell-shaped typical distribution known as (Gaussian) distribution.
        #mean 0, std dev 1, 50 size of data or samples
        #naming the numpy random normally distributed data as norm_data
            #int(1e6) = 1 million
            #As distribution increases and the sample size increases, you get more normal distributions
        #Same as what we were doing in R all long ago, statistical confidence increases with more iterations of multiple random number sequence generations (seed) 
plt.hist(norm_data, bins = 50)
    #histogram plotting of norm_data file (that is looking at normal distribution of 5 variables)
    #bins = how many categories there are 

plt.show()
    #showing the file
    


################## Running bcftools ########################

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


                

            
    


