#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt



vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

fig, ax = plt.subplots()
ax.hist( ac, density=True )

ax.set_yscale("log")
#ax.set_ylim(1,(1e-2))
ax.set_ylabel("log(frequency of the alternate alleles count)")

ax.set_xlabel("AC (Count of alternate alleles in called genotypes)")    

ax.set_title(vcf)

#plt.show()

fig.savefig( vcf + ".png" ) #we are now making out own plots
#plt.savefig("lncRNA.chr21.bed.vcf.png")
#plt.close(fig)

fs.close()


#JUST GOING TO RUN AND CHANGE gencode.v41.annotation.gtf 
#RUNNING: python plot_vcf_ac.py lncRNA.chr21.bed.vcf
#less -S gencode.v41.annotation.gtf 
#Adding my edited version of the 
