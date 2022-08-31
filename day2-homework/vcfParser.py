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
        
        
