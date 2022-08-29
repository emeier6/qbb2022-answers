#!/bin/bash

#USAGE: bash exercise1.sh input_VCF = 

for nuc in A C G T
do
  echo "Considering " $nuc
  #awk '/^#/{next} {if ($4 == $nuc) {print $5}}' $1 | sort | uniq -c

  #awk -v i="$i" '/^#/{next} {if (NR==i) {print $1, $2}}' temp_file
  awk -v nuc="$nuc" '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c

  #awk 'NR=='$i'{print $1, $2}' temp_file
  ##awk '/^#/{next} {if ($4 == '$nuc') {print $5}}' $1 | sort | uniq -c
done