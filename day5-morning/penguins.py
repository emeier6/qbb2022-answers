#!/usr/bin/env python
#less -S of penguins.csv # to see the data structure

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats

#Easier parsing through just commas, compared to csv
#names = True will take the first line as the headers for each of the subsequent files
df = np.genfromtxt("penguins.csv", delimiter = ",", dtype = None, encoding = None, names = True)

#CHECK:print(df)
#print(df.dtype)
    #OUTPUT: ('species', '<U9'), ('island', '<U9'), ('bill_length_mm', '<f8'), ('bill_depth_mm', '<f8'), ('flipper_length_mm', '<i8'), ('body_mass_g', '<i8'), ('sex', '<U6'), ('year', '<i8')]
        
        
'''        
    Comparing a row of indeces for a certain name (array) as 0, 1, 2,... 
        Subsetting! :^)
'''
rows = np.where(df["species"] == "Adelie")
df_adelie = df[rows]

    #This is DOUBLE subsetting, something like:
        #rows2 = np.where((df["species"] == "Adelie") and (df["island"] == "Dream"))
    #and also nesting, which can be done as:

df_adelie_m = df_adelie[np.where(df_adelie["sex"] == "male")]
df_adelie_f = df_adelie[np.where(df_adelie["sex"] == "female")]
#print(df_adelie_f)


'''
    Observing distribution of flipper length for m v f (single hist plot)
'''

fig, ax = plt.subplots()

ax.hist(df_adelie_m["flipper_length_mm"], label = "male", alpha = 0.6)
ax.hist(df_adelie_f["flipper_length_mm"], label = "female", alpha = 0.5)
#transparency = "alpha"
ax.set_xlabel("flipper length (mm)")
ax.set_ylabel("number of penguins")

ax.legend()
#plt.show()

'''
    Are the flipper lengths actually different? We can test using a t-test!
'''

#print(stats.ttest_ind(df_adelie_m["flipper_length_mm"], df_adelie_f["flipper_length_mm"]))
    #OUTPUT: Ttest_indResult(statistic=4.5588666963515765, pvalue=1.08977531716496e-05)
'''
    Interpreting results:
    pvalue <<< 0.05, so these are statistically different 
'''
'''
    Now, asking the same question with a general linear regression
'''

#As we are testing both m and f in a pop, we want both so df_adelie
#model = smf.ols(formula = "flipper_length_mm ~ 1 + sex", data = df_adelie)
#YAY!! WROTE IT BEFORE THE PROF!!
#results = model.fit()
#print(results.summary())

'''Results:
	*Intersect: 187.7945
	*Slope[male]: 4.6164
    *Prob (F-statistic): 1.09e-05 *difference in model
	*P-value: 0.000
	*R^2: 0.126
		
	For every increase in education metric, we see an increase in income [broad] by 
'''

#Finding out what the results report, so you can pull things
#print(dir(results))
#Printing the p-values
#print(results.pvalues)
    #OUTPUT:
    #Intercept      7.235707e-195
    #sex[T.male]     1.089775e-05

'''
    MULTIPLE LINEAR REGRESSIONS
'''

#modelmultivar = smf.ols(formula = "flipper_length_mm ~ 1 + species + sex + island + year", data = df)
#results = modelmultivar.fit()

#print(results.summary())

'''
    ANOVASSS - nesting models
'''
#full_model = smf.ols(formula = "flipper_length_mm ~ 1 + species + sex", data = df).fit()
#reduced_model = smf.ols(formula = "flipper_length_mm ~ 1 + species", data = df).fit()
fullest_model = smf.ols(formula = "flipper_length_mm ~ 1 + sex + year + island", data = df).fit()

#print(sm.stats.anova_lm(reduced_model, full_model, typ = 1))
#print(fullest_model.summary())


#Different types of ANOVAS with different interpretations. Here, we are just using type 1
#QUESTION: does the full model better explain the data than the more simple model?
'''
    OUTPUT:
      df_resid           ssr  df_diff      ss_diff        F        Pr(>F)
    0     330.0  14692.753022      0.0          NaN      NaN           NaN
    1     329.0  10787.149248      1.0  3905.603773  119.118  7.109600e-24
    
    Interpret:
    species matters, after controlling for sex
'''


'''
    PREDICTING flipper length USING MODEL
'''
#female, island of Dream, year 2008
#What is the predicted flipper length?

#MANUAL MODEL: 
#print(- 3957.9483 + 0 + 2.0736*2008 - 16.1405)
    #OUTPUT:189.69999999999933 mm


#THE forget FUNCTION
new_data = df[0]
new_data.fill(0)
new_data['island'] = 'Dream'
new_data['sex'] = 'female'
new_data['year'] = 2008
print(fullest_model.predict(new_data))
