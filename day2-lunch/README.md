# QBB2022 - Day 2 - Lunch Exercises Submission

git add README.md
git commit -m "Making the README.md file"
git push

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
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if not (fieldN <= 9 or fieldN >= 12):
            print(f"Line {i} appears malformed12", file=sys.stderr)
            continue
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    fs.close()
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
	
	
	
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
        
        fields[9] = fields[9].rstrip(",")
        fields[10] = fields[10].rstrip(",")
        fields[11] = fields[11].rstrip(",")
        
        #looking if 10 or 11, then we have a problem
        if  (fieldN < 3 or fieldN <= 9 or fieldN >= 12):
            print("Yay! Has 3!", file=sys.stderr)
        if not (fieldN < 3 or fieldN <= 9 or fieldN >= 12):
            #f is fancy way of autofill with the incorrect line
            print(f"Line {i} appears malformed1", file=sys.stderr)
            continue
        #if fieldN == 9 has 3 in the string converting to a line:
        if len(fields[8].split(",")) == 3:    
            print("Yay! Has 3!")
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
    


#Fields 9, 11, and 12 are lists, and then loop through the lists and change each value to a field type to be used