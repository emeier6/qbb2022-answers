#!/usr/bin/env python 
#
# (bash) cp ~/cmdb-quantbio/assignments/lab/bulk_RNA-seq/extra_data/dros_gene_expression.csv .
# (bash) curl https://raw.githubusercontent.com/bxlab/cmdb-quantbio/main/assignments/lab/bulk_RNA-seq/extra_data/dros_gene_expression.csv --output dros_gene_expression.csv]

import numpy as np
import numpy.lib.recfunctions as rfn
import scipy as sci

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

rows = sci.cluster.hierarchy.linkage(log_trans_filt)

columns = sci.cluster.hierarchy.leaves_list(log_trans_filt)