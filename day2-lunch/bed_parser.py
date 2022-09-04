#!/usr/bin/env python3
#./bed_parser.py hg38_gencodev41_chr21.bed

import sys

def parse_bed(fname):
#    counter = 0
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
        else (fieldN < 3 or fieldN <= 9 or fieldN >= 12):
            #f is fancy way of autofill with the incorrect line
            print(f"Line {i} appears malformed1", file=sys.stderr)
            continue
            
        #if fieldN == 9 has 3 in the string converting to a line:
        field8 = []
        if len(fields[8].split(",")) == 3:    
            #print("Contains 3 values in RGB")
            field8.append(fields[8].split(","))
        else i, len(fields[8].split(",")) >= 3:
            print(f"Line {i} is not equal to 3 :(", file=sys.stderr)
            continue
            
        if len(fields) > 9:
            field9 = []
            if fields[9].endswith(","):
                #print("blockCount ends with ,") 
                field9.append(fields[9].rstrip(","))
            else:
                #print("blockCount does NOT end with ,") 
                continue
                
            field10 = []    
            if fields[10].endswith(","):
                print("blockSize ends with ,")
                field10.append(fields[10].rstrip(","))
            else:
                #print("blockSize does NOT end with ,")
                continue
                
            field11 = []
            if fields[11].endswith(","):
                #print("blockStart ends with ,")
                field11.append(fields[11].rstrip(","))
                
            else:
                #print("blockStart does NOT end with ,")  
                continue
            ####or is this saying
            #if (len(fields[10]) + len(fields[11])) == len(fields[9]):
            #    print("the blockSizes + blockStarts = blockCount!")
            #if not (len(fields[10]) + len(fields[11])) == len(fields[9]):
            #    print("the blockSizes + blockStarts DO NOT = blockCount!")
            counter = 0
            if len(field10) == len(field9):
                print("blockSize = blockCount!")
            else len(field10) == len(field9):
                #print("blockSize DOES NOT = blockCount!")
                counter += 1
            print(counter)    
        
        
            counter = 0
            if len(field11) == len(field9):
                print("blockStarts = blockCount!")
            else len(field11) == len(field9):
                #print("blockStarts DOES NOT = blockCount!")
                counter +=1
            print(counter)
            
        try:
            #loop through numbers 0 to 5 not including 6
            for j in range(min(len(field_types), len(fields))):
                #looking at field j = whatever data type we denoted applied to what it actually is
                fields[j] = field_types[j](fields[j])
            bed.append(fields)
        except:
            print(f"Line {j} appears malformed", file=sys.stderr)
#            counter = counter + 1
 #           print(counter)
    fs.close()
    return bed
    

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    
#Block count is the number of exons
#if gene start and end are the same, what is the median number of exons?    

#Fields 9, 11, and 12 are lists, and then loop through the lists and change each value to a field type to be used
