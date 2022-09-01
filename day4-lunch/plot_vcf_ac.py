#!/usr/bin/env python3

import sys
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
#fig.savefig( vcf + ".png" ) #we are now making out own plots


ax.set_yscale("log")
ax.set_ylim(0,(1e-2))
ax.set_ylabel("log(another one)")

ax.set_xlabel("Something :^)")    
ax.legend()

ax.set_title(vcf)


plt.show()

#fs.close()

#plt.savefig("lncRNA.chr21.bed.vcf.png")
#plt.close(fig)

#JUST GOING TO RUN AND CHANGE processed_pseudogene.chr21.bed.vcf
#RUNNING: python plot_vcf_ac.py processed_pseudogene.chr21.bed.vcf