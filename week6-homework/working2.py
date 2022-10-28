#!/usr/bin/env python 


# python working2.py dCTCF_full.6400.matrix ddCTCF_full.6400.matrix 6400_bins.bed dCTCF_full.40000.matrix heatmap_1

import sys
import numpy 
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def remove_dd_bg(mat):
    N = mat.shape[0]
    mat2 = numpy.copy(mat)
    for i in range(N):
        bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
        mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
        if i > 0:
            mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
    return mat2    

def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat


def main():
    in1_fname, in2_fname, bin_fname, in3_fname, out_fname = sys.argv[1:6]
    data1 = numpy.loadtxt("dCTCF_full.6400.matrix", dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt("ddCTCF_full.6400.matrix", dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
    frags = numpy.loadtxt("6400_bins.bed", dtype=numpy.dtype([('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))
    data3 = numpy.loadtxt("dCTCF_full.40000.matrix", dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))

    chrom = b'chr15'
    start = 11170245
    end = 12070245
    start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                         (frags['start'] <= start) &
                                         (frags['end'] > start))[0][0]]
    end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                       (frags['start'] <= end) &
                                       (frags['end'] > end))[0][0]] + 1


    #find the rows where the position is within the ends
    position_ddCTCF = numpy.where((data2['F1'] >= start_bin) & (data2['F2'] <= end_bin))
    #add those positions into a new file
    filtered_dd = (data2[position_ddCTCF])
    #subtract the start value to make as 0
    filtered_dd['F1'] = (filtered_dd['F1'] - start_bin)
    filtered_dd['F2'] = (filtered_dd['F2'] - start_bin)
    #Now, we need to be log transforming the score data
    filtered_dd['score'] = numpy.log(filtered_dd['score'])
    #Subtracting the log values by the minimum log value of the data set
    filtered_dd['score'] = (filtered_dd['score'] - numpy.min(filtered_dd['score']))
    # Quick Check:
    # print(filtered_dd)
    
    
    position_dCTCF = numpy.where((data1['F1'] >= start_bin) & (data1['F2'] <= end_bin))
    filtered_d = (data1[position_dCTCF])
    filtered_d['F1'] = (filtered_d['F1'] - start_bin)
    filtered_d['F2'] = (filtered_d['F2'] - start_bin)
    filtered_d['score'] = numpy.log(filtered_d['score'])
    filtered_d['score'] = (filtered_d['score'] - numpy.min(filtered_d['score']))
    
    # This is dCTCF
    # Setting up the data for plotting
    mat1 = numpy.zeros([end_bin - start_bin + 1, end_bin - start_bin + 1 ])
    # Fill in the an array for the number of points that we have
    # for i in range(len(mat)): 
    # mat[sparse['F1'][i], sparse['F2'][i]] = sparse['score'][i]
    # mat1[filtered_d['F1'][i], filtered_d['F2'][i]] = filtered_d['score'][i]
    mat1[filtered_d['F1'], filtered_d['F2']] = filtered_d['score']
    # Inserting the data into the matrix
    mat1[filtered_d['F2'], filtered_d['F1']] = filtered_d['score']
    # Quick check
    # print(mat1)
    
    
    # This is for ddCTCF
    mat2 = numpy.zeros([end_bin - start_bin + 1, end_bin - start_bin + 1 ])
    # print(mat2.shape, mat1.shape)
    # Fill in the an array for the number of points that we have
    # for i in range(len(mat)):
    # mat[sparse['F1'][i], sparse['F2'][i]] = sparse['score'][i]
    # mat1[filtered_d['F1'][i], filtered_d['F2'][i]] = filtered_d['score'][i]
    mat2[filtered_dd['F1'], filtered_dd['F2']] = filtered_dd['score']
        # Inserting the data into the matrix
    mat2[filtered_dd['F2'], filtered_dd['F1']] = filtered_dd['score']
        # Quick check
    # print(mat2)
    # print(mat2)
    
    fig, ax = plt.subplots(3)
        
    # Plotting dCTCF
    ax[0].imshow(mat1, cmap = 'magma')
    ax[0].set_title('dCTCF')
    
    
    # Plotting ddCTCF
    ax[1].imshow(mat2, cmap = 'magma')
    ax[1].set_title('ddCTCF')
    #
    ax[2].imshow(smooth_matrix(remove_dd_bg(mat2)) - smooth_matrix(remove_dd_bg(mat1)), cmap = 'seismic')
    ax[2].set_title('ddCTCF - dCTCF')
    #
    plt.tight_layout()
    # plt.show()
        
    plt.savefig("Not_Iced_matrix_3")

if __name__ == "__main__":
    main()