#!/usr/bin/env python
# (bash) python recreate_fig3a.py 416685-1.txt 

import sys
import numpy as np
import matplotlib.pyplot as plt

k562_model_predictions = [] #predictions in column 5
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
        #Sanity check looks good: print(k562_obs_idx)
        #Sanity check looks good:print(header)
    elif not line.strip('"').startswith("#"):
        fields = line.strip('"\r\n').split('\t')
        if i < 10:
            print(fields)
            quit()
        k562_model_predictions.append(float(fields[4])) # the 5th column are the predictions we want. Need numerical values, change from string to float
        k562_observations.append(float(fields[k562_obs_idx])) # change from string to float
        gene_names.append(fields[1]) #fine for this to be a string, no changes needed
        description.append(fields[2]) #fine for this to be a string, no changes needed

# Make a scatterplot of figure 3a from the paper :^)