#!/usr/bin/env python
# (bash) python recreate_fig3a.py 416685-1.txt 

import sys
import numpy as np

k562_model_predictions = [] #predictions
k562_observations = [] #real
gene_names = [] #these are for the red gene names
descriptions = [] #these are for the red globin gene names

for i, line in enumerate(open(sys.argv[1])):
    # if line.startswith("#"):
#         continue
    if line.strip('"').startswith("##"):
        header = np.array(line.strip('"\r\n').split('\t'))
        k562_obs_idx = np.where(header == "E123")[0][0]
        #index with 0 to tell that this is all we are looking for in this new array
        #adding the second [0] removes the brackets
        print(k562_obs_idx)
        print(header)
    elif not line.strip('"').startswith("#"):
        fields = line.strip('"\r\n').split('\t')
        if i < 10:
            print(fields)
            quit()
        