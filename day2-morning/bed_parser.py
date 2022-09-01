	#INTO PYTHON - requires .py file
    #Touch ___.py into the file of interest
    #open -a Textmate __.py

#!/usr/bin/env python 
    
import sys

def bed_parser(fname):
#fs = open("hg38_gencodev41_chr21.bed", mode='r')
    fs = open(fname, mode='r')
    # create empty list to hold entries
    bed = []
    data_types = [str, int, int, str, float, str]
    #Step line by line through file
    for line in fs:
        #Get rid of newline char and split into
        # seperate fields
        fields = line.rstrip().split("\t")
        #Name relevant fields, convertin to ints
        #when needed
        for h, line in enumerate(fs):
            fields = line.rstrip().split("\t")
        try:
                for i in range(min(len(data_types), len(fields))):
            #try:
                    if fields[i] != ".":
                        converter = data_types[i]
                        fields[i] = data_types[i](fields[i])
            #except:
            #   pass
        #chrom = fields[0]
        #start = int(fields[1])
        #end = int(fields[2])
        #create list of fields and put in bed-list
                bed.append(fields[:min(len(data_types), len(fields))])
            #bed.append([chrom, start, end])
        except:
                print(f"line {h} is malformed", file=sys.sstderr)
    fs.close()
    return bed

    #close out first 2 entries

    #for i in range(2):
    #    print(bed[i])

#protection for running the previous code and also importing it into something elses
if __name__ == "__main__":
#requires bed variable to be defined as what you want to print
    bed = bed_parser(sys.argv[1])
    
#pull out the first 2 entries as list and look
#at each entry in variable i    

    for i in bed[0:2]:
#    print entry 1s
        print(i)

#for i in range(2):
#NOT GOOD	print(i)


#OUTPUT:
#['chr21', 5011798, 5017145]
#['chr21', 5022530, 5036771]

#USE THIS TO CALL THE CODE IN REFERENCE TO A BED FILE:
#python bed_parser.py hg38_gencodev41_chr21.bed 

### PARTS OF A FUNCTION ####################

