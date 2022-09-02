#!/bin/bash

############### NOTES for LINEAR REGRESSION MODELS #####################
#PURPOSE:
	
	'''
	#Making regressions to test hypotheses
	#Basic setup: y = b + ax
	
		IE: Heritability:
			F1_height = ß0 + ß1 x (mid-parent height)
	--------------------------	
	Multiple linear regressions:
		y = ß0 + ß1x1 + ß2x2 + ...
		x# denotes number of x-axes (and plains)
		
		T-test:
			*Single predictor value (x1), T/F
			*Asking is slope sig-diff from y = 0?
		
		Pearson-Correlation: 
			*Where points differ from a set line
		
		Spearman: 
			*Ranked order of values in space (further from 0,0)	
	
	----------------------------
	Fitting linear models:
		Ordinary least squares;
			*Sum of squared difference to a reference line:
				Vertical distance line from point, then squaring
			*Goal is to find the smallest squared difference (minimizing)
			*Looking at an estimate of the minimized sum of squares, and then 
				obtaining regressiong coefficients to get standard error
	----------------------------
	Hypothesis testing!:
		H0: No relationship between predicted var and response var.
		H1: There is some relationship between predicted var and response var.
		
		Computing and testing:
			*How big/small IS the diff?
				
				t = (ß1 - 0) / (SE(ß01))
				
				The probability of seeing a number greater than or equal to t
					*assumes ß0 = 0

			*The assumptions: 
				
				1. Indep data points
					Non-independent data points: different regression models IE
						Mixed-effects models
						
				2. Normally distributed residuals
				
				3. Variance around a regression line for all values is equal
					Typically not
				
				IE when the assumptions are broken:
					 Nested structure with gene expression to cell type
			
	----------------------------------------------------------------------------
					 
	Practicing these regression models in Python:
		
			Library:   statsmodels.formula.api as smf
				*Borrowing from R lmao
			'''
			#To tell the model to make a basic 1x variable linear regression from data
#model = smf.ols(formula = "income ~ 1 + education", data = my_data)
#results = model.fit()
#results.summary()
		#This prints out a nice results table with lots of information from the generated model
		
	'''Interpreting:
		*Intersect: const to coef
		*Slope: education to coef
		*P-value: P>|t| in education to coef
		*R^2 for how well the model fits the data, 
			and therefore the predicted power of the model
			
		For every increase in education metric, we see an increase in income [broad] by 
		'''
#less -S of penguins.csv # to see the data structure



