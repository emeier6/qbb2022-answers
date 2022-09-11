#!/usr/bin/env python


import numpy as np
#import argparse as ap
from scipy.stats import poisson
import matplotlib.pyplot as plt
#from statsmodels.stats.multitest import multipletests

#
# #n_tosses is number of tosses
# #probability of heads
# #no seed
#
# genome = np.array(np.zeros(int(1e6)))
#
# #50,000 reads, will look at random generation where the start is wherever rand gene is
# for i in range(50000):
#     randgene = np.random.randint(0, 999900)
#     for j in range(randgene, randgene + 100):
#         genome[j] += 1
# #rint(np.sum(genome))
# #OUTPUT: Yields 5mil reads
# x = np.array(genome)

#print(np.sum(x))



#Probability mass function using the Poisson distribution

#generate random values from Poisson distribution with mean=3 and sample size=10

#lambda = 5
#mu = lambda 

#pmf = poisson.pmf(x, mu=5) #, loc

# fig, ax = plt.subplots()
#
# ax.plot(x, poisson.pmf(x, mu=5), 'bo', ms=8)
#
# ax.hist(x, density=True, color = "lightblue")
# ax.vlines(x, 0, poisson.pmf(x, mu=5), colors='b', lw=5, alpha=0.5)
#
# ax.set_ylabel("Frequency")
# ax.set_xlabel("Number of reads")
# ax.set_title("Frequency of 5x reads in genome")
# #plt.show()
# plt.savefig("ex1_3.png")


#How many times does the arrangement have 0x coverage?
# zeros = np.where(x==0)
# #zeros = np.count_nonzero(x==0)
# #OUTPUT: 6214
# print(len(zeros[0]))
#OUTPUT: 6645

#looks like, the "frequency" is about 0.025 from the histogram, so the number of 0 reads when doing  50,000 reads of 100bp = 1,250 reads (with 0 coverage) * the area of the curve= 3,150
#Poisson plots the probability that the output equals 0, so it isn't a frequency of the events, so the probablility of about 0.00863 still needs to be transferred to frequency, which is plotted by 


######### 1.4 ##################

#
#
# genome2 = np.array(np.zeros(int(1e6)))
#
# #50,000 reads, will look at random generation where the start is wherever rand gene is
# for i in range(150000):
#     randgene = np.random.randint(0, 999900)
#     for j in range(randgene, randgene + 100):
#         genome2[j] += 1
# #rint(np.sum(genome))
# #OUTPUT: Yields 5mil reads
# x2 = np.array(genome2)
#
# #print(np.sum(x2))
#Dat checks


#Probability mass function using the Poisson distribution
#generate random values from Poisson distribution with mean=3 and sample size=10

#lambda = 15
#mu = lambda
#
# pmf = poisson.pmf(x2, mu=15) #, loc
#
# fig, ax = plt.subplots()
#
# ax.plot(x2, poisson.pmf(x2, mu=15), 'go', ms=8)
#
# ax.hist(x2, density=True, color = "lightgreen")
# ax.vlines(x2, 0, poisson.pmf(x2, mu=15), colors='g', lw=5, alpha=0.5)
#
# ax.set_ylabel("Frequency")
# ax.set_xlabel("Number of reads")
# ax.set_title("Frequency of 15x reads in genome")
# #plt.show()
# plt.savefig("ex1_4.png")

#How many times does the arrangement have 0x coverage?
# zeros = np.where(x2==0)
# # #zeros = np.count_nonzero(x==0)
# # #OUTPUT:
# print(len(zeros[0]))
# #OUTPUT: 5

#frequency is 0.001 = 150, 









#############################################################3
### 2.1 ###
#conda install mummer=3.23=h6de7cb9_11
#conda create -n spades
#conda activate spades
#conda install -c bioconda spades

#curl http://cab.spbu.ru/files/release3.15.5/SPAdes-3.15.5-Darwin.tar.gz -o SPAdes-3.15.5-Darwin.tar.gz
#tar -zxf SPAdes-3.15.5-Darwin.tar.gz
#cd SPAdes-3.15.5-Darwin/bin/
#~/Downloads/SPAdes-3.15.5-Darwin/bin


#-o asm denotes what the new name is, and it will push into a folder
#~/Downloads/SPAdes-3.15.5-Darwin/bin/spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31
###2.1
#four contigs were produced

### 2.2 ###
#grep '>NODE_5' contigs.fasta | head
#Total length of contigs for NODE 1: 105830 
#Total length of contigs for NODE 2: 47860
#Total length of contigs for NODE 3: 41351
#Total length of contigs for NODE 4: 39426
#NO NODE 5 HELL YEA

### 2.3 ###
#Size (length) of largest contig = NODE 1 at 105830


# ### 2.4 ###  What is the contig N50 size?
# print((105830 + 47860 + 41351 + 39426)/2)

# #OUTPUT: 117233.5 is the contig N50 size, which resides in NODE 2





#######################################################

#conda install mummer=3.23=h6de7cb9_11
#dnadiff ~/qbb2022-answers/week1-homework/asm/ref.fa ~/qbb2022-answers/week1-homework/asm/asm/scaffolds.fasta
#less -S out.delta
#out.report

### 3.1 ###
#OUTPUT: AvgIdentity                    99.98                99.98
#From the reference to the qry, what is the qry? The qry is our assemnbled output


### 3.2 ###
#Reference: 207007    
#Our assembly (qry): 207000

### 3.3 ###
#From my assembly: I find one insertion of 712 bp, and specutively, from TotalIndels we see 15 reported (tentatively 14 deletions since 1 insertion). However, with the Total G indels, there is onyl 1 (insertion), that is accounted for when the 20bp before and after the indel sequence is aligned to the reference. So there is only 1 insertion

#### So, what is the true difference between Total and TotalG?




#nucmer ~/qbb2022-answers/week1-homework/asm/ref.fa ~/qbb2022-answers/week1-homework/asm/asm/scaffolds.fasta
#show-coords out.delta


#######################################################

### 4.1 ###
# G alignment versus m alignment
# the left alignment for our query is at position 26788 and then is a gap insertion through alignment position 27499 (a difference of 711 insertion)



### 4.2 ###
#this corresponds to the reference position as 26790, but it is 711 bp shorter than the generated assembled genome

### 4.2 ###
#samtools faidx ~/qbb2022-answers/week1-homework/asm/asm/scaffolds.fasta NODE_1_length_234497_cov_20.506978:26788-27499

#Name of the sc affolds.fasta file and the region of the insert we are looking at

#python dna-decode.py -h
#python dna-decode.py -d --input asm/NODE_1_length_234497_cov_20.506978:26788-27499

#Do need to specify the 

#./dna-decode.py -d --input asm/NODE_1_length_234497_cov_20.506978:26788-27499

## OUTPUT:
'''The decoded message :  Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens...'''