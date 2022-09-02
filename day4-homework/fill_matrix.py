#!/usr/bin/env python

import numpy

#array 0 0.1 0.2. 0.3 0.4 and stuff, now decreasing the number of decimals :^)
#tosses is an array that will go 10 to 20 to 30
#now in two_dim arrays we give a tuple length of 2, length probablility is rows and length of tosses is a column of the matrix
#DAT FOR Loop is going through the probabilities and 
### DOIN anotha one to add the probability of the probability for toss to store the probability plus tosses

probabilities = numpy.around(numpy.arange(0, 0.5, 0.1), decimals = 2)
tosses = numpy.arange(10, 40, 10)

print(numpy.arange(0, 0.5, 0.1))
quit()

#initialize the array before the for loop with numpy.zeroes of the lengths of each of the matrix columns
new_twodim_arr = numpy.zeros((len(probabilities), len(tosses)))
for i, prob in enumerate(probabilities):
    for j,toss in enumerate(tosses):
        new_twodim_arr[i,j] = prob + toss
print(new_twodim_arr)


#now, we can look at the matrix we generate by running this array as now, and how we can array and store values



