#!/usr/bin/env python


import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats


#WORKING FILE: 1043aau_mf_age_joined.vcf 
#TRACKED HEADERS: Proband_id	fathers_count 	father	 mothers_count 	mother 	father_age	 mother_age


#fig, ax = plt.subplots()

################   FEMALES ############################################
#ax.scatter(df["mother_age"], df["mother_mutation_count"] )
#ax.set_ylabel("Count of mutations")
#ax.set_xlabel("Age")
#ax.set_title("Count of mutations versus age in mothers", fontsize = 14)
#ax.legend()

#plt.show()

#plt.savefig("ex2_a.png")
#plt.close(fig)



################   MALES ############################################
#ax.scatter(df["father_age"], df["father_mutation_count"], color = "orange" )

#ax.set_ylabel("Count of mutations")
#ax.set_xlabel("Age")
#ax.set_title("Count of mutations versus age in fathers", fontsize = 14)
#ax.legend()

#plt.show()

#plt.savefig("ex2_b.png")
#plt.close(fig)


'''
vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )
'''


###############################



#df = smf.ols(formula = "mother_mutation_count ~ 1 + mother_age", data = df)
#results = df.fit()
#print(results.summary())
df = np.genfromtxt("1043aau_mf_age_joined.vcf", delimiter = " ", dtype = None, encoding = None, names = ["Proband_id", "father_mutation_count", "father", "mother_mutation_count", "mother", "father_age", "mother_age"])



df = smf.ols(formula = "father_mutation_count ~ 1 + father_age", data = df)
results = df.fit()
print(results.summary())



#############################################



################   HIST ############################################


fig, ax = plt.subplots()

ax.hist(df["mother_mutation_count"], label = "mothers", alpha = 0.6)
ax.hist(df["father_mutation_count"], label = "fathers", alpha = 0.5)
ax.legend()
ax.set_ylabel("Frequency of the count of mutations")
ax.set_xlabel("Count of mutations")
ax.set_title("Comparing the frequency and count of mutations \n between mothers and fathers to age", fontsize = 14)

#plt.show()

#plt.savefig("ex2_c.png")
#plt.close(fig)


####################### t-test ####################################

#print(stats.ttest_ind(df["father_mutation_count"], df["mother_mutation_count"]))
#OUTPUT:    Ttest_indResult(statistic=53.323950583065304, pvalue=1.1656909236893846e-263

#father_mutation_count = 10.3887 + 1.3513x
print(10.3887 + 1.3513*50.5)
    #OUTPUT: 78.62935
