#!/usr/bin/env python

import numpy
from scipy.stats import binomtest
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multitest import multipletests

#add these two to the top, since we are defining the variables we are running
tosses = numpy.array([10, 50, 100, 250, 500, 1000])
probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
#print(numpy.arange(0.55, 1.05, 0.05))
#print(probs)
#[::-1 corresponds to [start 0 : stop 0 : step -1]
#format string python, wc3 schools has a link with formatting types
    #could be like print(f" {}") with print(ef" {}") to denote scientific notation, or print(2f" {}") to denote 2 decimal points
    
def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Simulates a coin toss (fair or unfair depending on prob_heads)
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation; default is None
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''    
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads])
    return (results_arr)

def perform_hypothesis_test(n_heads, n_tosses):
    '''
    Performs a two-sided binomial test
    Input: n_heads, an integer, number of coin tosses that resulted in heads/success
           n_tosses, an integer, total number of coin tosses/trials
    Output: pval, a float reporting the final pvalue from the binomial test
    Resources: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html#scipy.stats.binomtest
    '''
    binom_result = binomtest(n_heads, n_tosses)
    pval = binom_result.pvalue
    return(pval)

def correct_pvalues(pvals):
    '''
    Will apply the bonferroni multiple hypothesis testing correction method to input pvalues
    Input: pvals, an array-like object containing uncorrected pvalues
    Output: corrected_pvalues[1], an array containing corrected pvalues
    Resources: https://www.statsmodels.org/dev/generated/statsmodels.stats.multitest.multipletests.html
    '''
    corrected_pvalues = multipletests(pvals, method='bonferroni')
    return(corrected_pvalues[1])

def interpret_pvalues(pvals):
    '''
    Will interpret or convert pvalues from floats to booleans (Trues or Falses) reporting whether or not you reject the null hypothesis
    True -- reject null Hypothesis
    False -- fail to reject null hypothesis
    Input: pvals, an array-like object containing pvalues (floats)
    Output: interpreted, an array containing booleans
    '''
    interpreted = numpy.array(pvals) < 0.05
    return (interpreted)

def compute_power(n_rejected_correctly, n_tests):
    '''
    Will compute the power, defined as the number of correctly rejected null hypothesis divided by the total number of tests (AKA the True Positive Rate or the probability of detecting something if it's there)
    Input: n_rejected_correctly, an integer, the total number of tests in which the null hypothesis was correctly rejected
           n_tests, an integer, the total number of hypothesis tests which were performed
    output: power, a float, the power
    '''
    power = n_rejected_correctly / n_tests
    return(power)

def run_experiment(prob_heads, n_toss, n_iters = 100, seed = 389, correct_the_pvalues = False):
    '''
    Input: prob_heads, a float, the probability of a simulated coin toss returning heads
           n_toss, an integer, the number of coin tosses to simulate
           n_iters, an integer, the number of iterations for each simulation. default is 100
           seed, an integer, the random seed that you will set for the whole simulation experiment. default is 389
           correct_the_pvalues, a boolean, whether or not to perform multiple hypothesis testing correction
    Output: power, a float, the power of the experiment
    '''
    numpy.random.seed(seed)
    pvals = []
    for k in range(n_iters):
        results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
        n_success = numpy.sum(results_arr)
        pvals.append(perform_hypothesis_test(n_success, n_toss))
    if correct_the_pvalues:
        pvals = correct_pvalues(pvals)
    pvals_translated_to_bools = interpret_pvalues(pvals)
    power = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
    return(power)


    
#new array assigning start value at 0 for both probablility and tosses. Then, we define the length of the array with len for probabilities and for tosses.


#Taking the single output and now putting it in a larger combined list
#we are using the definitions from power to 
#the double for loop loops first through probability list, and then the second for loop add the search for tosses
#but, we are only looking to relate the single line or value of each of the probabilities, and for each of the tosses. The tosses is a list, but we are not filling in a list for each of the matrix points, just a single point that was defined as the single toss variable. The same is true for probs and single probs. then, we can print the power_twoD to see if we ran this correctly.
power_twoD_Corr = numpy.zeros((len(probs), len(tosses)))
for i, singleprob in enumerate(probs):
    for j, singletoss in enumerate(tosses):
        power_twoD_Corr[i,j] = run_experiment(singleprob, singletoss, correct_the_pvalues = True)

#CHECK:print(power_twoD)
#p<0.05 / number of thigs we are testing
#this can be done by iterating through, which is what we are doing here...

power_twoD = numpy.zeros((len(probs), len(tosses)))
for i, singleprob2 in enumerate(probs):
    for j, singletoss2 in enumerate(tosses):
        power_twoD[i,j] = run_experiment(singleprob2, singletoss2)    
    
  

power1 = run_experiment(0.6, 500, correct_the_pvalues = True)
#print(power1)
power2 = run_experiment(0.95, 10, correct_the_pvalues = True)
#print(power2)
power2b = run_experiment(0.95, 10)
#print(power2b)



#Creating a heat map plot of the matrixed values = power_twoD
fig, (ax2, ax1) = plt.subplots(ncols=2, gridspec_kw={'width_ratios': [1, 1.3]})
sns.heatmap(power_twoD_Corr, ax=ax1, vmin = 0, vmax = 1, annot=True, cbar=True, annot_kws={"size": 7}, xticklabels=tosses, yticklabels=probs, cmap='viridis')
ax1.set_xlabel("Array of tosses")
ax1.set_ylabel("Array of probabilities")    
ax1.set_title("Corrected", fontsize = 10)

sns.heatmap(power_twoD, vmin = 0, vmax = 1, ax=ax2, annot=True, cbar=False, annot_kws={"size": 7}, xticklabels=tosses, yticklabels=probs, cmap='viridis')
ax2.set_xlabel("Array of tosses")
ax2.set_ylabel("Array of probabilities")    
ax2.set_title("Uncorrected", fontsize = 10)

#fig.tight_layout()
fig.suptitle('Power matrix of probability versus tosses arrays', fontsize = 14)
#plt.show()

plt.savefig("Comp_Corr_NonCorr.png")
plt.close(fig)

