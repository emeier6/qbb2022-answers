# 0a: Read in the Data
	import numpy as np
	
	input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
	col_names = input_arr.dtype.names
	# print(col_names)
	
	row_names = input_arr['t_name']
	# print(row_names)

# 0b: Process the Input Data
	import numpy as np
	import numpy.lib.recfunctions as rfn
	
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
	
	# Now, we are looking for the values in our 2D array that the means are greater than 0 in each array
	filtered_fpkm = fpkm_values_2d[np.where(medians > 0),:]
	
	print(filtered_fpkm)
	
	log_trans_filt = np.log2(filtered_fpkm + 0.1)
	# print(log_trans_filt)
	# Looks good!
	
# 1: Clustering