#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

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

s = np.random.binomial(n, p, 1000en )

# statistics = sci.stats.binom( )
# random_gen = random.Generator.binomial( )

summary = sum(np.random.binomial(9, 0.1, 20000) == 0)/20000
print(summary)
# Check: 0.38735s

'''Plotting :^) '''




