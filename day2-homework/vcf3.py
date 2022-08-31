#!/usr/bin/env python3

from vcfParser import *
#* means import everything

#print(parse_vcf('random_snippet.vcf'))

randSNP = parse_vcf('random_snippet.vcf')

fs = open('dbSNP_snippet.vcf', "r")

SNP_dict = {}
for line in fs:
    if line.startswith("#"):
        continue
        
    else:
        fields = line.strip().split('\t')
        #finding out which is value and which is key
        #we want the position as the key so that we can substitute the value (the ID) in for the aligned position
        
        #POS
        fields[1] = int(fields[1])
        pos = fields[1]
        
        #ID
        identification = fields[2]
        
        SNP_dict[pos] = str(identification)
            

#key will be the ID
#value will be the POSITION

#sanity check
for k, v in SNP_dict.items():
    print(k, v)



#for randSNP in 
