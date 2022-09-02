#!/usr/bin/env python

import numpy
from scipy.stats import binomtest
from statsmodels.stats.multitest import multipletests

#n_tosses is number of tosses
#probability of heads
#no seed
def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    if seed is not None:
        numpy.random.seed(seed)
        #numpy random choice
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1 - prob_heads, prob_heads])
    return (results_arr)

#Front half of the room
#print(numpy.sum(simulate_coin_toss(10)))
    #OUTPUT: Random generators
    
#Back half of the room
#print(numpy.sum(simulate_coin_toss(10, seed = 4)))
    #OUTPUT: 6 because seeded from a value
    
#  PERFORM THE HYPOTHESIS TEST     
def perform_hypothesis_test(n_heads, n_tosses):
    binom_result = binomtest(n_heads, n_tosses)
    pval = binom_result.pvalue #grabbing the pvalue attribute from the binom_result
    return(pval)

#CHECK if worked: print(perform_hypothesis_test(2,5))




def correct_pvalues(pvals):
    corrected_pvalues = multipletests(pvals, method = "bonferroni")
    return(corrected_pvalues[1])
        #multiple things that it can return, we just want the pvalue
    
#print(correct_pvalues([0.005, 0.04, 0.0003, 0.01]))
    #OUTPUT: [0.02   0.16   0.0012 0.04  ]
    

# TEST IF DIFFERENT FROM H0
def interpret_pvalues(pvals):
    #checks all the p-values from the array
    interpreted = numpy.array(pvals) < 0.05
    return(interpreted) #an array of trues and falses

#print(interpret_pvalues([0.06, 0.5, 0.4, 0.01, 0.03]))  
      #OUTPUT: [False False False  True  True] This lines up to the pvalues that I put here as an example


########### POWER to decrease falsitivities
#both variables are integer inputs
def compute_power(n_rejected_correctly, n_tests):
    power = n_rejected_correctly / n_tests
    return(power)




#you can just randomly set the number of iterations
def run_experiment(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):
    #will have randomness, so need to set the seed number
    numpy.random.seed(seed)
    pvals = []
    for k in range(n_iters):
        #this is saying that we are storing the results from the coin toss with our previously defined perameters of number of tosses and probability
        results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads) #set seed toss earlier, so didnt need to set it within in the function
        #only storing the iterations when it =1 or when we get heads
        n_success = numpy.sum(results_arr)
        #
        pvals.append(perform_hypothesis_test(n_success, n_toss))
   ####################HOMEWORKs
    if correct_the_pvalues:
        pvals = correct_pvalues(pvals) #this will overwrite the pvales
    ###### Report pvalues and the power (being able to call the H0)
        #power = true positive rate or sensitivity
    pvals_translated_to_bools = interpret_pvalues(pvals)
        #we want to translate to 0 and 1 to get the number of trues
    power = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
    
    #return(pvals)    
    return(power)


#print(run_experiment(0.2, 30, n_iters=5))
power1 = run_experiment(0.6, 500)
print(power1)
power2 = run_experiment(0.95, 10, correct_the_pvalues = True)
print(power2)

#how can we control false positive methods wth too few sampling?
############### with ya boi BONFERRONI !!!!!!!!!!!!!!! :^)
########## in the def corrected_pvalues
###################HOMEWORK THING, coreected or not-corrected 
#pass a boolean argument to correct the pvalues

    #requires p value
    #alpha parameter (a float)
    #method = bonferroni
    #from stats models library 




