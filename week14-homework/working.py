#!/usr/bin/env python

#USAGE: python scriptname.py KRAKEN_sample_input_file.kraken sample_name
#EXAMPLE: python make_krona_compatible.py KRAKEN/SRR492183.kraken SRR492183
# python working.py ~/qbb2022-answers/week14-homework/metagenomics_data/step0_givendata/KRAKEN/assembly.kraken ~/qbb2022-answers/week14-homework/bins_dir/bin2.fa


import sys

f = open(sys.argv[1])
sample = sys.argv[2]
out = open(sample + "_krona.txt", "w")

for line in f:
    new = sample.split('>')
print(new[2])
#
# for line in f:
#     fields = line.strip('\r\n').split('>')
#     out.write("\t".join(fields[1:]) + "\n")
#
#I also can't figure this out but I am trying really hard :(