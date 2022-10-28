#!/usr/bin/env python 

# /analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix
# /analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix

# Fitler by this range chr15:11170245-12070245
# Run both through load_data

# using the load_data.py working environment, copied from below with additions for designated inputs

import sys

import numpy 
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Adding in the files laid out in the def main group
# in1_fname = open("ddCTCF_ontarget_6400_iced.matrix")
# in2_fname = open("dCTCF_ontarget_6400_iced.matrix")
# bin_fname = open("6400_bins.bed")

  
# python working.py dCTCF_ontarget_6400_iced.matrix ddCTCF_ontarget_6400_iced.matrix 6400_bins.bed dCTCF_full.40000.matrix heatmap_1

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
    # in1_fname should be ddCTCF
        #ddCTCF_ontarget_6400_iced.matrix
    
    # out_fname = heatmap_1
    # in2_fname should be dCTCF
        #dCTCF_ontarget_6400_iced.matrix
    # bin_fname should be bed file with bin locations
        #6400_bins.bed
    # heatmap_1
    
    # python working.py dCTCF_ontarget_6400_iced.matrix ddCTCF_ontarget_6400_iced.matrix 6400_bins.bed dCTCF_full.40000.matrix heatmap_1 
    in1_fname, in2_fname, bin_fname, in3_fname, out_fname = sys.argv[1:6]
    data1 = numpy.loadtxt("dCTCF_ontarget_6400_iced.matrix", dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
    data2 = numpy.loadtxt("ddCTCF_ontarget_6400_iced.matrix", dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
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
    print(mat1)
    
    
    # This is for ddCTCF
    mat2 = numpy.zeros([end_bin - start_bin + 1, end_bin - start_bin + 1 ])
    print(mat2.shape, mat1.shape)
    # Fill in the an array for the number of points that we have
    # for i in range(len(mat)):
    # mat[sparse['F1'][i], sparse['F2'][i]] = sparse['score'][i]
    # mat1[filtered_d['F1'][i], filtered_d['F2'][i]] = filtered_d['score'][i]
    mat2[filtered_dd['F1'], filtered_dd['F2']] = filtered_dd['score']
        # Inserting the data into the matrix
    mat2[filtered_dd['F2'], filtered_dd['F1']] = filtered_dd['score']
        # Quick check
    print(mat2)
    
    
    
    
    #Insertion for the 40000 bins information, same as before BUT adding in the fragment lengths that we are interested in
    position_40k = numpy.where((data3['F1'] >= 54878) & (data3['F2'] <= 54951))
    filtered_40k = (data3[position_40k])
    filtered_40k['F1'] = (filtered_40k['F1'] - 54878)
    filtered_40k['F2'] = (filtered_40k['F2'] - 54878)
    filtered_40k['score'] = numpy.log(filtered_40k['score'])
    filtered_40k['score'] = (filtered_40k['score'] - numpy.min(filtered_d['score']))
    mat3 = numpy.zeros([54951 - 54878 + 1, 54951 - 54878 + 1 ])
    mat3[filtered_40k['F1'], filtered_40k['F2']] = filtered_40k['score']
        # Inserting the data into the matrix
    mat3[filtered_40k['F2'], filtered_40k['F1']] = filtered_40k['score']
        # Quick check
    print(mat3)
    #Looks ok! Now moving on

    insulation_scores = []
    nt_list = []

    for i in range(5, 54951 - 54878 + 1):
        insulation_scores.append(numpy.mean(mat3[(i - 5):i, i:(i + 5)]))
        # print(insulation_scores)

    nt_list = numpy.linspace(10400000, 13400000, len(insulation_scores))
    
    # The 
    
    fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
    ax[0].axis('off')
    plt.margins(x=0)
    ax[1].set_xlim(10400000, 13400000)
    plt.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=1.0,
                    top=1.0,
                    wspace=0.4,
                    hspace=0.0)
    ax[0].set_title("dCTCF 40000")
    ax[0].imshow(mat3, cmap = 'magma')
    # fig, ax = plt.subplots(3)
    ax[1].scatter(nt_list, insulation_scores)
    ax[1].set_title('Insulation Score')
    plt.tight_layout()
    # plt.show()
    
    plt.savefig("Insulation_Scores")
#     # Plotting dCTCF
     # ax[0].imshow(mat1, cmap = 'magma')
 #     ax[0].set_title('dCTCF')
 #     # plt.imshow(mat1, vmin = 0, vmax = mat1, cmap = 'magma')
 #
 #     # Plotting ddCTCF
 #     ax[1].imshow(mat2, cmap = 'magma')
 #     ax[1].set_title('ddCTCF')
#
#     ax[2].imshow(smooth_matrix(remove_dd_bg(mat2)) - smooth_matrix(remove_dd_bg(mat1)), cmap = 'seismic')
#     ax[2].set_title('ddCTCF - dCTCF')
#
    # plt.tight_layout()
    # plt.show()
    
    
        #dif = (mat2 - mat1)
   



if __name__ == "__main__":
    main()
    
    