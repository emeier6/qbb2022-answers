#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt   

EigenInt = np.genfromtxt("sortedEigenIntCalls", dtype = None, encoding = None, names = ["Sample", "Sample", "PCA1", "PCA2", "PCA3", "Country", "Continent", "sex"])


############ Adding for loops
fig, ax = plt.subplots(nrows=1)

sex_list = np.unique(EigenInt["sex"]) #field [7]
continents_list = np.unique(EigenInt["Continent"])
country_list = np.unique(EigenInt["Country"])
xg = []
yg = []
for i, continent in enumerate(continents_list):
    row = np.where(EigenInt["Continent"] == continent)
    print(row)
    xg.append(EigenInt["PCA1"][row])
    yg.append(EigenInt["PCA2"][row])
    ax.scatter(xg[i], yg[i], label = continent, )
ax.set_ylabel("PC2")
ax.set_xlabel("PC1")    
ax.legend(loc="upper right")


#CHECK:
#plt.show()
    #LOOKS GREAT
plt.savefig("ex3_b.png")
plt.close(fig)

#RUN:python np.py sortedEigenIntCalls

#COUNTRY
#cut -f 6 sortedEigenIntCalls | sort | uniq -c 

#CONTINENT
#cut -f 7 sortedEigenIntCalls | sort | uniq -c 

#SEX
#cut -f 8 sortedEigenIntCalls | sort | uniq -c 


#RUN: python np2.py sortedEigenIntCalls 