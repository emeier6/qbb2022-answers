# QBB2022 - Day 2 - Homework Excercises Submission


	#adding the VCF
git add --force #for the VCF files

#Exercise 1 - Commenting on the vcf_parser.py_

	#!/usr/bin/env python3
	#sheband says python script and import sys

	import sys

	#defining what we are parsing, many dictionaries

	def parse_vcf(fname):
	    vcf = []
	    #this vcf list
	    #initializing a lot of dictionaries to store information
    
	    info_description = {}
	    info_type = {}
	    format_description = {}
	    #converting words to types of data
    
	    type_map = {
	        "Float": float,
	        "Integer": int,
	        "String": str
	        }
	    #counts the number of incorrectly formatted lines, skips and notes lines with errors
    
	    malformed = 0

	 #try and except statement
	    #try: opening a file name correctly
	    try:
        
	        fs = open(fname)
	        #if typed incorrectly, then reports that the file does not exist
        
	    except:
	        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)
	 #enumarating fs, which enumarates a set of numbers and the contents of the lines (telling us the line number)
	    #fs is the filename that we are running and enumerating

	    for h, line in enumerate(fs):
	        #the BIG if: starting the process of identifying the values statements
        
	        if line.startswith("#"):
	            #is the line a FORMAT line?
            
	            try:
	                #splitting the formatting line and removing formatting characters and adding a comma between each of the things splitting in the format line. This is being called fields. Splits into two columns and then strips into two lines. 
	                #The [1] is then piped to be stripped of any tailing formatting and adds a comma. n is a new line character, r is a carriage return (typwriter) and replacing it with a comma.
                
	                if line.startswith("##FORMAT"):
	                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                  
	                    i = 0
	                    start = 0
	                    in_string = False
	                    while i < len(fields):
	                        if fields[i] == "," and not in_string:
	                            if fields[start:i].count("=") == 1:
	                                name, value = fields[start:i].split('=')
	                                if name == "ID":
	                                    ID = value
	                                elif name == "Description":
	                                    desc = value
	                            start = i + 1
	                        elif fields[i] == '"':
	                            in_string = not in_string
	                        i += 1
	                    format_description[ID] = desc.strip('"')
	                elif line.startswith("##INFO"):
	                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
	                    i = 0
	                    start = 0
	                    in_string = False
	                    while i < len(fields):
	                        if fields[i] == "," and not in_string:
	                            if fields[start:i].count("=") == 1:
	                                name, value = fields[start:i].split('=')
	                                if name == "ID":
	                                    ID = value
	                                elif name == "Description":
	                                    desc = value
	                                elif name == "Type":
	                                    Type = value
	                            start = i + 1
	                        elif fields[i] == '"':
	                            in_string = not in_string
	                        i += 1
	                    info_description[ID] = desc.strip('"')
	                    info_type[ID] = Type
	                elif line.startswith('#CHROM'):
	                    fields = line.lstrip("#").rstrip().split("\t")
	                    vcf.append(fields)
	            except:
	                raise RuntimeError("Malformed header")
	        else:
	            #otherwise, we look at this information
	            try:
	                #making a list from the new split where we are removing anu spaces after the right of the strip, and then splitting where we see the \t. 
	                #Fields contains the columns of our line split
	                fields = line.rstrip().split("\t")
	                #For the second column, set that as an integer
	                fields[1] = int(fields[1])
	                #For the 6th column, if it is not a dot, then we are making that into a float because it could be denoted as 3.0, which is a float, while . is not. This is the quality is 5 section.
	                if fields[5] != ".":
	                    fields[5] = float(fields[5])
	                #We are making a dictionary for info, which is in a format where a lot of information is bunched by ";". 
	                info = {}
	                #splitting the information on the semicolon, we are making a list of strings.
	                for entry in fields[7].split(";"):
	                    temp = entry.split("=")
	                    #then, splitting entries on the = sign to make a list of strings, like [["AC", "91"], ["GF", "98"]. 
	                    #these lists are called temps
	                    if len(temp) == 1:
	                        info[temp[0]] = None
	                    else len(temp) > 1:
	                        info[temp[1]] = temp[2]
	                    #if the list is the first of two values without a second value, then we write that as [AC:None], because there is no second value.
	                    #temp 0 is the first value, and if the second value is not present, then we are saying it does not have a second value.

	                    #OTHERWISE, if there are two variables, then we are assigning the two variables into the info dictionary.
	                    else:
	                    #this else block is adding from the temp and its corresponding 
	                    #turning the value as the correct data type
	                    #temp is the string that we set earlier  
	                    #this populates the info dictionary with paired values that were constructed in temp  
	                        name, value = temp
	                        Type = info_type[name]
	                        info[name] = type_map[Type](value)
	                        #type_map is a dictionary that automatically converts values to its correct type (int, float, etc)
                    
                    
	                fields[7] = info
	                #replacing column 7 into the dictionary we just made previously
                
	                #if we count more than 8 fields, or there are more columns than after the info field, then...
	                if len(fields) > 8:
	                    #then we split the 8th field where we see the ":"
	                    fields[8] = fields[8].split(":")
	                    #then, if the length of the 8th field is greater than 1 after the split (ie: there were ":"), and make a new column split at the ":"
	                    if len(fields[8]) > 1:
	                        #for strings where there is more than 1 value (or paired values), then 
	                        for i in range(9, len(fields)):
	                        #then after the fields we already modified, we split into strings and keep populating the fields
	                        #taking all the columns after the 9th column are all tha sampels, and so we also want to split by ":"
	                        #telling you all the format of your GT calls for each of your samples, denoted by len(fields).
	                        #replacing complicated strings with ":" as lists
	                            fields[i] = fields[i].split(':')
	                        #split all the genotype columns if they have more than 1 indicated format
	                    else:
	                        fields[8] = fields[8][0]
	                    #if it isn't split, then it just keeps the single string that we generated. We turn it back into a string from a list
	                    #now, we add this back into the original vcf field using append
	                vcf.append(fields)
	                #EXCEPT, if these codes failed, then we skip and one to the count of malformed lines
	            except:
	                malformed += 1
                
	    vcf[0][7] = info_description
	    #
	    #if we have the output from the samples that we just formatted, then we write that description
	    if len(vcf[0]) > 8:
	        vcf[0][8] = format_description
	        #if there were any malformed, then we print how many malformed entries there were
	    if malformed > 0:
	        print(f"There were {malformed} malformed entries", file=sys.stderr)
        
	    return vcf
	    #return the list vcf

	#if the scriptname calling the command line script name, then
	if __name__ == "__main__":
	    #we are making the file executable
	    fname = sys.argv[1]
	    #getting the name of the file to input on
	    vcf = parse_vcf(fname)
	    #running the large function that we made and appended to run and parse the file that we've pulled and want to work with
	    for i in range(10):
	        print(vcf[i])
	    #print the vcf using temporary variable for the for loop in the first 10 columns
	    #for i in...
	        #range (4) 
	        #= range(0,4) #excluding 4# 
	        #= [0,1,2,3]
        
		#RUN THE CODE WITH:
		#python vcfParser.py random_snippet.vcf
        
        #git add README.md
		#git commit -m "Exercise 1 upload"
		#git push
#Exercise 2 - Annotating a file with SNP labels

	The dbSNP_snippet.vcf does not have any sample info like the random_snippet.vcf does
	
	#GOAL: Pull out the ID from the dbSNP_snippet.vcf and input it for the IDs of the random_snippet.vcf, where appropriate
	
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


#Corrected/Finished Exercise 2 (in class 31AUG22):
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

	

