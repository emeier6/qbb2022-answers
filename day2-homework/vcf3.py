#!/usr/bin/env python3

from vcfParser import *
#* means import everything

#print(parse_vcf('random_snippet.vcf'))

randSNP = parse_vcf('random_snippet.vcf')
db = parse_vcf('dbSNP_snippet.vcf') #Previous error:parse only needs the vcf file, not to be read
#db = open('dbSNP_snippet.vcf', "r") #This would be able to read

#If not parsing, will need to skip reading lines that start with "#", then also strip the lines and split the lines with tab. :
    #if:
    #   line.startswith("#"):
    #       continue
    #else:
    #   fields = line.strip().split('\t')

SNP_dict = {}
for line in db:
    if line[0] == "CHROM":
        continue
    chrm = line[0]
    pos = line[1]
    identification = line[2]
    
    SNP_dict[(chrm, pos, identification)] = identification
    
counter = 0
for i, things in enumerate(randSNP):
    if things[0] == "CHROM":
        continue
    chrm = things[0]
    pos = things[1]
    identification = things[2]
    
    if (chrm, pos) in SNP_dict.keys():
        things[2] = SNP_dict[(chrm, pos, identification)]
    else:
        counter = counter + 1
        #conter =+ 1
print(counter)        

##OUTPUT: Says there are only 24 malformed entries.

