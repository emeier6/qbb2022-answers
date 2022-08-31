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