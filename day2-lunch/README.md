# QBB2022 - Day 2 - Lunch Exercises Submission

git add README.md
git commit -m "Making the README.md file"
git push
	
#Exercise 1 - Extend your BED parser	
	#!/usr/bin/env python3
	#./bed_parser.py hg38_gencodev41_chr21.bed

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, str, int, str, str]
    for i, line in enumerate(fs):
        #the for loop prints every time an error occurs, otherwise outside of the for loop, it will only print the last line of error
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        
        #stripping each of the beds 10 - 12 to remove commas
        fields[9] = fields[9].rstrip(",")
        fields[10] = fields[10].rstrip(",")
        fields[11] = fields[11].rstrip(",")
        
        #looking if 10 or 11, then we have a problem
        if  (fieldN <= 2 or fieldN <= 9 or fieldN >= 12):
            print("Contains the expected the number of columns (3-9, 12)", file=sys.stderr)
        if not (fieldN < 3 or fieldN <= 9 or fieldN >= 12):
            #f is fancy way of autofill with the incorrect line
            print(f"Line {i} appears malformed1", file=sys.stderr)
            continue
            
        #if fieldN == 9 has 3 in the string converting to a line:
        if len(fields[8].split(",")) == 3:    
            print("Contains 3 values in RGB")
        if not len(fields[8].split(",")) == 3:
            print(f"Line {i} is not equal to 3 :(", file=sys.stderr)
            
        if fields[9].endswith(","):
            print("blockCount ends with ,") 
        if not fields[9].endswith(","):
            print("blockCount does NOT end with ,") 
                
        if fields[10].endswith(","):
            print("blockSize ends with ,")
        if not fields[10].endswith(","):
            print("blockSize does NOT end with ,")
            
        if fields[11].endswith(","):
            print("blockStart ends with ,")
        if not fields[11].endswith(","):
            print("blockStart does NOT end with ,")  
            
        if len(fields[10]) == len(fields[9]):
            print("blockSize = blockCount!")
        if not len(fields[10]) == len(fields[9]):
            print("blockSize DOES NOT = blockCount!")
        
        ####or is this saying
        #if (len(fields[10]) + len(fields[11])) == len(fields[9]):
        #    print("the blockSizes + blockStarts = blockCount!")
        #if not (len(fields[10]) + len(fields[11])) == len(fields[9]):
        #    print("the blockSizes + blockStarts DO NOT = blockCount!")
        
        if len(fields[11]) == len(fields[9]):
            print("blockStarts = blockCount!")
        if not len(fields[11]) == len(fields[9]):
            print("blockStarts DOES NOT = blockCount!")
            
        try:
            #loop through numbers 0 to 5 not including 6
            for j in range(min(len(field_types), len(fields))):
                #looking at field j = whatever data type we denoted applied to what it actually is
                fields[j] = field_types[j](fields[j])
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    fs.close()
    return bed
    

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    


#Exercise 2 - analyze a gene in BED file
	#import bed_parser
	#bed_parser.bed_parser('hg38_gencodev41_chr21.bed')
	#./bed_parser.py hg38_gencodev41_chr21.bed

	from bed_parser import *
	bp = bed_parser('hg39_gencodev41_chr21.bed')

	#GOALS:
	#Block count is the number of exons
	#if gene start and end are the same, what is the median number of exons?    
	    #Report the number of malformed entries
	    #Report the median number of exons for genes in the hg38_genecodev41_chr21.bed
	counter = 0
	for line in bp:
	    counter = 0
	    start = line[1]
	    end = line[2]
	    exon = line[9]
    
	    #For all genes, not for specific lengths of genes, so ignore
	    #if line in bp:
	    #    if end - start 

	    if line == 10:
	        counter = counter + 1
	    else:
	        for i, line != 10:
	            print(f's{i} malformed entries')
	    print(counter)
    


	#if __name__ == "__main__":
	#    fname = sys.argv[1]
	#    bed = parse_bed(fname)