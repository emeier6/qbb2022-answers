#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
from scipy.stats import binom


# Starting allele frequency
p = 0.6334

# Population size
n = 10
# Generations of assumed random genetic variation and drift
generations = 10

# Generating a random allele type before changing the fates, should be 50-50 fate
pop = np.ones(n) + np.random.uniform(-0.5, 0.5, n)
# print(pop)
# [1.30942415 0.64179491 0.64925822 0.76789762 0.81814693]

# Writing a for loop to create the probability of fitness for an allele over a set number of generations, seeing how fixes
for gen in range(generations):
    fitnessprops = pop/np.sum(pop)
    
# print(fitnessprops)
# [0.16332993 0.16842005 0.24516895 0.19946457 0.22361651]

# Randomly sampling number of offspring
numoffspring = np.random.multinomial(n, fitnessprops)

# Check that this still equals n at the beginning
# Length:
# print(len(numoffspring))
# Sum:
# print(np.sum(numoffspring))

# Making a library for the population and the number of offspring to study drift and population genetics
newpop = []
history=[pop]

for fitness, num in zip(pop, numoffspring):
    newpop.extend([fitness]*num)
    history.append(pop)
# Check length:
# print(len(newpop))

pop = np.array(newpop)
# Check: print(len(pop))
# print(len(history))

mean_fitness = np.mean(history, axis=1)
# Check the length: print(len(mean_fitness))
std_fitness = np.std(history, axis=1)
# Check the length: print(len(std_fitness))


'''Numpy one'''
binomial = np.random.binomial(n, p)

s = np.random.binomial(n, p, 1000 )

# statistics = sci.stats.binom( )
# random_gen = random.Generator.binomial( )

summary = sum(np.random.binomial(9, 0.1, 20000) == 0)/20000
print(summary)
# Check: 0.38735s

'''Plotting :^) '''
n, p = 10, .5  # number of trials, probability of each trial
s = np.random.binomial(n, p, 1000)
# result of flipping a coin 10 times, tested 1000 times.
sum(np.random.binomial(9, 0.1, 20000) == 0)/20000



rng = np.random.default_rng()
n, p = 10, .5  # number of trials, probability of each trial
s = rng.binomial(n, p, 1000)
# result of flipping a coin 10 times, tested 1000 times.
sum(rng.binomial(9, 0.1, 20000) == 0)/20000.
# answer = 0.38885, or 39%.


n = 6
p = 0.6
# defining the list of r values
r_values = list(range(n + 1))
# obtaining the mean and variance 
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# printing the table
print("r\tp(r)")
for i in range(n + 1):
    print(str(r_values[i]) + "\t" + str(dist[i]))
# printing mean and variance
print("mean = "+str(mean))
print("variance = "+str(var))


# setting the values
# of n and p
n = 6
p = 0.6
# defining list of r values
r_values = list(range(n + 1))
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# plotting the graph 
plt.bar(r_values, dist)
plt.show()

# fig, ax = plt.subplots()
#
# # Plotting
# ax.imshow(mat1, cmap = 'magma')
# ax.set_title('dCTCF')
#
# ax.set_title('ddCTCF - dCTCF')
# plt.tight_layout()
# plt.show()
#
#
# #plt.savefig("binomial_permutations")