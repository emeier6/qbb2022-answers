#VCF2.py, which is going to loop back the output from vcfParser.py so that we can look at the id column from random_snippet and see if equal and then substitute with the ID from dbSNP

#First, is look at the dbSNP.vcf and make a dictionary for the dbSNP IDs.
    #We need to pull the position and the ID from dbSNP
    
    #chmod +x FILENAME
    
    #!/usr/bin/env python3
    
from vcfParser import *
#* means import everything

#print(parse_vcf('random_snippet.vcf'))

randSNP = parse_vcf('random_snippet.vcf')
#theSNP = open('random_snippet.vcf', "r")

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

###sanity check = works!
#    for k, v in SNP_dict.items():
#        print(k, v)
    
###Likely dont need to append the dbSNP file because we are only using the SNP_dict, so no need to override with:
    #fs.append(fields)?
    
    #to add the new field information and overwrite

### Is this a function we want here? Or we are still trying to use this fs to look at vcfParser aka randSNP?
#fs.close()



##############################################################################
#Second, we have to go line by line and search the random_snippet.vcf and look to see if the IDs of dbSNP (from that dictionary) match. 

#THINKING:
#for fields[1] in randSNP:
#    if fields[1] = fs[pos].map(SNP_dict)
#df['First_Name'] = df['ID'].map(fnames)

for line in randSNP:
    #we may need to denote this, since it did not skip over the # in the vcfParser
    #ALREADY DONE in the vcfParser:
    #fields = line.rstrip().split("\t")
    #fields[1] = int(fields[1])

    if line.startswith("#"):
        continue
    else:
        #already defined in vcfParser, do not need to include fields here:
        #fields = line.rstrip().split("\t")

#If it does, then overwrite with the dbSNP ID
        if randSNP.fields[1] == SNP_dict[pos]:
          randSNP.fields[2] = str(identification)

#If not, then skip
        else:
      #then skip?
          continue
          #or should we set that 
      #    if fields[1] != SNP_dict[pos]:
      #        fields[2] = fields[2]#[0]
              #do we need this [0] here?
              
#should we fs.close() for dbSNP? I don't think we should considering we are still working with the fsself.
        randSNP.append(fields)
#randSNP.append(fields[1])
#randSNP.append(fields[2]) 

    #randSNP[1][2] = new_version
    
    #if we have the output from the samples that we just formatted, then we write that description
 
print(randSNP)
    
    
    

#Then run the random_snippet.vcf with the changes
#run code:
#python vcf2.py

