#!/usr/bin/env python
#python working.py /Users/cmdb/data/vcf_files/random_snippet.vcf 

import sys

def vcf_parser(fname):
    try:
        fs = open(fname)
    except:
        raise FileNotFoundError("no file by such name")
    
    #chrom, pos, ID, ref, alt, qual, filter, info, format, 
    vcf = []    
    format_fields = {}
    #make dictionary
    info_fields = {}
    type_mapper = {
        "Float": float,
        "Integer": int,
        
    }
    malformed = 0
    for line in fs:
        if line.startswith('#'):
            #omit the continue and try parsing
            try:
                if line.startswith("##FORMAT"):
                    #then get info from filter
                    #Want 2 things:
                    #1.ID
                    #2.Description
                    fields = line.spliot('<')[1].split(',')
                    for item in fields:
                        key, value = item.split('=')
                        if key == "ID":
                            name = value
                        elif key == "Description":
                            desc = value
                    format_fields[name] = desc
                if line.startswith("##INFO"):
                    #then get info from filter
                    #Want 2 things:
                    #1.ID
                    #2.Description
                    fields = line.spliot('<')[1].split(',')
                    for item in fields:
                        key, value = item.split('=')
                        if key == "ID":
                            name = value
                        elif key == "Description":
                            desc = value
                        elif key == "Type":
                            itype = value
                            #store in its own dictionary
                    info_fields[name] = itype
                fields = line.rstrip().split("\t")
        #appending the vcf (what we are writing to) and fields are what we are splitting and appending to vcf
                if len(fields) < 8:
                    malformed += 1
                    continue
        try:
            fields[1] = int(fields[1])
            if fields[5] != ".":
                fields[5] = float(fields[5])
            fields[7] = fields[7].split(";")
            info = {}
            for i in range(len(fields[7])):
                temp = fields[7][i].split('=')
                if len(temp) == 2:
                    if 
                    info[temp[0]] = temp[1]
                elif len(temp) == 1:
                    info[temp[0]] = None
            fields[7] = info
            
            if len(fields) >= 8:
                fields[i] = []
                for i in range(8, len(fields)):
                    fields[i] = fields[i].split(':')
            #fields[5] = int(fields[5])
            vcf.append(fields)
        except:
            malformed += 1
    if malformed > 0:
        print(f"there were {malformed} malformed entries")
#        vcf.append(fields)
    return vcf
    
if __name__ == "__main__":
    vcf = vcf_parser(sys.argv[1])
    print(vcf[0][:12])

