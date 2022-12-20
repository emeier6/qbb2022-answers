#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
from scipy.stats import binom
import seaborn as sns


# setting the values
# of n and p
n = 100
p = 0.5


# defining the list of r values
r_values = list(range(n + 1))
# obtaining the mean and variance 
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# printing the table
# print("r\tp(r)")
# for i in range(n + 1):
#     print(str(r_values[i]) + "\t" + str(dist[i]))
# printing mean and variance
# print("mean = "+str(mean))
# print("variance = "+str(var))



# defining list of r values
r_values = list(range(n + 1))
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# plotting the graph 
# plt.bar(r_values, dist)
# plt.show()



s = np.random.binomial(n, p, 1000)
# result of flipping a coin 10 times, tested 1000 times.
print(sum(np.random.binomial(9, 0.1, 20000) == 0)/20000)

#fixing the seed for reproducibility
#of the result
np.random.seed(10)

size = 10000
#drawing 10000 sample from 
#binomial distribution
sample = np.random.binomial(n, p, size)
bin = np.arange(0,n,1)
#
# plt.hist(sample, bins=bin, edgecolor='blue')
# plt.title("Binomial Distribution")
# plt.show()
#
# sns.kdeplot(np.random.binomial(100, 0.5, size))
# sns.kdeplot(np.random.binomial(1000, 0.5, size))
# sns.kdeplot(np.random.binomial(10000, 0.5, size))
# sns.kdeplot(np.random.binomial(100000, 0.5, size))
# sns.kdeplot(np.random.binomial(1000000, 0.5, size))
# sns.kdeplot(np.random.binomial(10000000, 0.5, size))

# plt.legend(["$n = 100, p = 0.5$",
#             "$n = 1000, p = 0.5$",
#             "$n = 10000, p = 0.5$"])
# plt.legend(["$n = 100, p = 0.5$",
#             "$n = 1000, p = 0.5$",
#             "$n = 10000, p = 0.5$",
#             "$n = 100000, p = 0.5$",
#             "$n = 1000000, p = 0.5$",
#             "$n = 10000000, p = 0.5$"])

# plt.show()
# plt.savefig("3_binomial_permutations")
# plt.savefig("6_binomial_permutations")



# rng = np.random.default_rng()
# n, p = 10, .5  # number of trials, probability of each trial
# s = rng.binomial(n, p, 1000)
# # result of flipping a coin 10 times, tested 1000 times.
# sum(rng.binomial(9, 0.1, 20000) == 0)/20000.
# # answer = 0.38885, or 39%.


#
# sns.ecdfplot(np.random.binomial(100, 0.5, size))
# sns.ecdfplot(np.random.binomial(1000, 0.5, size))
# sns.ecdfplot(np.random.binomial(10000, 0.5, size))
# sns.ecdfplot(np.random.binomial(100000, 0.5, size))
# sns.ecdfplot(np.random.binomial(1000000, 0.5, size))
# sns.ecdfplot(np.random.binomial(10000000, 0.5, size))
#
# # plt.legend(["$n = 100, p = 0.5$",
# #             "$n = 1000, p = 0.5$",
# #             "$n = 10000, p = 0.5$"])
# plt.legend(["$n = 100, p = 0.5$",
#             "$n = 1000, p = 0.5$",
#             "$n = 10000, p = 0.5$",
#             "$n = 100000, p = 0.5$",
#             "$n = 1000000, p = 0.5$",
#             "$n = 10000000, p = 0.5$"])
# plt.show()

# plt.savefig("3_proportion_permutations")
# plt.savefig("6_proportion_permutations")


'''Changing the p value!'''

pval = 0.8

sns.ecdfplot(np.random.binomial(100, pval, size))
sns.ecdfplot(np.random.binomial(1000, pval, size))
sns.ecdfplot(np.random.binomial(10000, pval, size))
sns.ecdfplot(np.random.binomial(100000, pval, size))
sns.ecdfplot(np.random.binomial(1000000, pval, size))
sns.ecdfplot(np.random.binomial(10000000, pval, size))

# plt.legend(["$n = 100, p = 0.5$",
#             "$n = 1000, p = 0.5$",
#             "$n = 10000, p = 0.5$"])
plt.legend(["$n = 100, pval$",
            "$n = 1000, pval$",
            "$n = 10000, pval$",
            "$n = 100000, pval$",
            "$n = 1000000, pval$",
            "$n = 10000000, pval$"])
# plt.show()
# plt.savefig("6_proportion_0.386pval_permutations")
# plt.savefig("6_proportion_679pval_permutations")
plt.savefig("6_proportion_80pval_permutations")