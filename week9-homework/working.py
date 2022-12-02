#!/usr/bin/env python 
#
# (bash) cp ~/cmdb-quantbio/assignments/lab/bulk_RNA-seq/extra_data/dros_gene_expression.csv .
# (bash) curl https://raw.githubusercontent.com/bxlab/cmdb-quantbio/main/assignments/lab/bulk_RNA-seq/extra_data/dros_gene_expression.csv --output dros_gene_expression.csv]

import numpy as np
import numpy.lib.recfunctions as rfn
import scipy.cluster.hierarchy as sci
from scipy.spatial.distance import pdist
import matplotlib as mpl
import matplotlib.pyplot as plt
from statsmodels.formula.apu import ols

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = input_arr.dtype.names
# print(col_names)

row_names = input_arr['t_name']
# print(row_names)


# List needed to index after the first value in each of the arrays
fpkm_values = input_arr[list(col_names[1:])]
# print(the_arr)
#  OUTPUT: Works!

fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=np.float)
# print(fpkm_values_2d)
# print(len(fpkm_values))

medians = np.median(fpkm_values_2d, axis=1)
# print(medians)
# print(len(medians))

filtered_fpkm = fpkm_values_2d[np.where(medians > 0)[0],:]
# print(filtered_fpkm)

# 0.1 must be inside the parentheses before log transforming, or infinity lol
log_trans_filt = np.log2(filtered_fpkm + 0.1)
# print(log_trans_filt)
# Looks good!



'''Clustering the data by sample AND transcript'''
# print(log_trans_filt)

rows = sci.linkage(log_trans_filt)
# print(rows) checking that looks fine
x = np.array(rows)
# print(x)
cols = np.transpose(log_trans_filt)
columns = sci.linkage(cols)
# print(columns)


'''Linkage is a plotting function'''
# IE: will use the row values to assign the distance matrix as a tree
# X = [[i] for i in [2, 8, 0, 4, 1, 9, 9, 0]]
# Z = linkage(rows, 'single')

# Didnt work: Zward = sci.linkage(cols, 'ward')
Zi = sci.ward(pdist(columns))
# Heatmap, use:
fig, ax = plt.subplots()

#Dendrogram, use: 
# fig = plt.figure(figsize=(25, 10))
# Adding the heatmap to the log transformed data
ax.imshow(Zi)

sci.leaves_list(Zi)
dn = sci.dendrogram(Zi)
# Show all ticks and label them with the respective list entries
# ax.set_xticks(np.arange(len(rows)), labels=row_names)
# ax.set_yticks(np.arange(len(columns)), labels=col_names)

ax.set_title("log2 of transformed and filtered FPKM")

fig.tight_layout()
plt.show()
# plt.savefig("heatmap_Filtered&Transformed")
# plt.savefig("dendrogram_Filtered&Transformed")




'''Differential Gene Expression'''
log_trans_filt = np.log2(filtered_fpkm + 0.1)

