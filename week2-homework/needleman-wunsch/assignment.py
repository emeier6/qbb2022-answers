#!/usr/bin/env python3

import numpy as np
import sys
from fasta import readFASTA
#python assignment.py CTCF_38_M27_AA.faa BLOSUM62.txt -10
#python assignment.py CTCF_38_M27_DNA.fna HOXD70.txt -300

'''denoting score values'''
#FOR DNA: python assignment.py 3 -3 -300
#FOR protein: # python assignment.py -10

#for DNA
#3 = match
#-3 mismatch
#-2 is the gap
'''this is the needleman-wunch model for looking at sequence alignment!! so cool!!!'''

"python assignment.py HOXD70.txt -10 "

#========================#
# Set sequences to align #
#========================#

# In the homework assignment, you'll reading sequences from a
# FASTA file. For the live-coding, we'll define them
# explicitly in the script.

#query or i should pertain to your first sequence and reference sequence
#sequence1 = 'ACGTGG'
# print(sequence1)
#subject should pertain to the sequence of interest
#sequence2 = 'ACGTA'
# print(sequence2)
'''for the first AA or BLOSUM test'''
input_sequences = readFASTA(open(sys.argv[1]))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]
# #sequence2 = np.array(input_sequences([seq2_id[0], input_sequences[0]]))
#

Hox_matrix = np.loadtxt(sys.argv[2], dtype = "object", skiprows=1)
#blosum = np.loadtxt(sys.argv[2], dtype = "object", skiprows=1)

gap_penalty = float(sys.argv[3]) 

# print(Hox_matrix)
#
header = list(Hox_matrix[:,0])
#header = list(blosum[:,0])

# print(header)
score = Hox_matrix[:,1:]
#score = blosum[:,1:]


#converting matrix into the numbers
score = score.astype(int)
# print(score)

# 3 = d
# 2 = v
# 1 = h


F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
traceback_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
#
for i in range(len(sequence1)+1):
    F_matrix[i,0] = i * gap_penalty
    traceback_matrix[i,0] = 1

for j in range(len(sequence2)+1):
    F_matrix[0,j] = j * gap_penalty
    traceback_matrix[0,j] = 3
# print(score)
# print(traceback_matrix)

for i in range(1, len(sequence1)+1):
     for j in range(1, len(sequence2)+1):
         n1 = sequence1[i-1]
         n2 = sequence2[j-1]
         
         index_i = header.index(n1)
         index_j = header.index(n2)
         
         d = F_matrix[i-1,j-1] + score[index_i, index_j]
         h = F_matrix[i,j-1] + gap_penalty
         v = F_matrix[i-1,j] + gap_penalty

         #gives us the maximum score value from either the d, v or h value
         F_matrix[i,j] = max(d,h,v)
         
         #this tells us what the max value came from
         # 2 = d
         # 1 = v
         # 3 = h
         if d >= h and d >= v:
             traceback_matrix[i,j] = 2
        
         elif h > d and h >= v:
             traceback_matrix[i,j] = 3
         
         elif v > d and v > h:
             traceback_matrix[i,j] = 1
         

# print(traceback_matrix)
#Quickest route and highest quality route         
# for i, row in enumerate(F_matrix[::-1]):
#     if i == 0:
#         best_index = len(row)
#     else:
#         v_gap = best_index
#         v_match = best_index - 1
#         if row[v_gap] < row[v_match]:
#             best_ind = v_match
#         else:
#             best_ind = v_gap
#
i = traceback_matrix.shape[0] - 1
j = traceback_matrix.shape[1] - 1
align1 = ""
align2 = ""

# print(sequence1, sequence2)
while i > 0 or j > 0:
    #making -1 because the sequence starts at 0, but the list is an additional one 
    if traceback_matrix[i,j] == 2:
        align1 += sequence1[i-1]
        align2 += sequence2[j-1]
        i -= 1
        j -= 1
        
    elif traceback_matrix[i,j] == 1:
        align1 += sequence1[i-1]
        align2 += '-'
        i -= 1
        
    elif traceback_matrix[i,j] == 3:
        align1 += '-'
        align2 += sequence2[j-1]
        j -= 1
        
#reverses lists AND strings :^)

align1 = align1[::-1]
align2 = align2[::-1]


#print(align1)    
print(align1.count('-'))

#print(align2)    
print(align2.count('-'))
         # 2 = d
         # 1 = v
         # 3 = h
           

           
