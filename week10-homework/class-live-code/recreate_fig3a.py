#!/usr/bin/env python
# (bash) python recreate_fig3a.py 416685-1.txt 

import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

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
            # quit() # remove that so I can actually run stuff lmao
        k562_model_predictions.append(float(fields[4])) # the 5th column are the predictions we want. Need numerical values, change from string to float
        k562_observations.append(float(fields[k562_obs_idx])) # change from string to float
        gene_names.append(fields[1]) #fine for this to be a string, no changes needed
        descriptions.append(fields[2]) #fine for this to be a string, no changes needed



# Make the figure 3a from the paper :^) is a scatter plot!
genesoi = ["PIM1", "SMYD3", "FADS1", "PRKAR2B", "GATA1", "MYC"]
genesoilocs = []

for i in genesoi:
    genesoilocs.append(np.where(np.array(gene_names) == i)[0][0])
    #here, we are pulling where the gene names correspond with the ones with hemoglobin subunit

for i in range(len(descriptions)):
    if "hemoglobin subunit" in descriptions[i]:
        genesoi.append(gene_names[i]) #append another column at that same row
        #know the gene names, but where do we plot them? X and Y values
        genesoilocs.append(i)

cor = pearsonr(k562_model_predictions, k562_observations)

fig, ax = plt.subplots()

ax.scatter(k562_model_predictions, k562_observations, color="blue", s=0.25, alpha=1)
ax.set_xlabel("Predicted K562 expression level (log10)")
ax.set_ylabel("K562 expression level \n10-fold cross validated")

# line_xs = np.linspace(min(min(k562_model_predictions) ,min(k562_observations) ), max(max(k562_model_predictions) ,max(k562_observations) ), 100)
line_xs = np.linspace(max(min(k562_model_predictions) ,min(k562_observations) ), min(max(k562_model_predictions) ,max(k562_observations)), 100)
line_ys = 0 + 1 * line_xs

ax.plot(line_xs, line_ys, color = "maroon")

# This is to add the r^2 and the n number
ax.text(0.5, 3.75, "r^2 = " + str(round(cor.statistic**2, 2)) + "\nn = " + str(len(k562_observations))) #double asterist to the second power, round to second decimal

#adding the red genes of interest
for i, idx in zip(genesoi, genesoilocs):
    print(i)
    print(idx)
    ax.text(k562_model_predictions[idx], k562_observations[idx], i, color="maroon", fontweight="demi")

#aesthetics
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)

plt.tight_layout()
# plt.show()

plt.savefig("Figure 3A")
