Day 5 Lunch: Linear Regression

#Exercise 1: Wrangle the data with Unix
	1. ABSTRACT summary:
		-In this article, we are charcterizing how parental gamete recombination is related to mutations.
		-Recombination occurs when double stranded breaks are exchanged across sister chromatids.
		-This paper uses parent and offspring gene sequences, looking at how crossover is influenced by:
			-age, sex, sequence variance, and epigenetic factors.
		-The paper claims that transcribed regions are less likely to be crossed, maybe to reduce mutations.
		-They also find that:
			-Complex crossovers are more common in females, and increases with age of maternal age
				-Leading to increase in mutation in complex regions
			-Increasing maternal age correlates with an increase in low GC content, later regions.

	2. Starting aau1043_dnm.csv:
		-Sort, then unique -c mutations 
		-number of paternally inherited de novo mutations, maternally inherited de novo mutations for that proband
			Proband id = the 5th column 
		-STEP 1: Convert commas to tab deliminated to columns to then pull information
				
			#making commas tab deliminated
			sed 's/,/\t/g' aau1043_dnm.csv
			#checking that it is tab deliminated
			sed 's/,/\t/g' aau1043_dnm.csv | cat -t
			#stored as aay1043_dnm_tabdelim.csv
			
			sed 's/,/\t/g' aau1043_dnm.csv | sort -k 1,2 | cut -f 6 | sort | uniq -c
			sed 's/,/\t/g' aau1043_dnm.csv | sort -k 1,2 | uniq -c 
			
			sed 's/,/\t/g' aau1043_dnm.csv | sort -k 5 | grep --text "father" | cut -f 5,6 | uniq -c > 1043_males.vcf
			
			sed 's/,/\t/g' aau1043_dnm.csv | sort -k 5 | grep --text "mother" | cut -f 5,6 | uniq -c > 1043_mothers_count.vcf
			
		-STEP 2: Join these baddies
			
			sort -k 2 1043_males.vcf > 1043_males_sorted.vcf
			sort -k 2 1043_mothers_count.vcf > 1043_mothers_sorted.vcf 
			
			join -1 2 -2 2 1043_males_sorted.vcf 1043_mothers_sorted.vcf > 1043aau_mf_joined.vcf
			
		-STEP 3: Record which counts the columns represent:
			column 1 = proband id
			coulumn 2 = fathers count
			column 5 = mothers count

	
	3. Use unix to join the parental age of each of fathers and mothers with aau1043_parental_age.csv
		HEAD: Proband_id	fathers_count 	father	 mothers_count 	mother 	father_age	 mother_age
		
		STEP1: #pip install csvkit
		sed 's/,/\t/g' aau1043_parental_age.csv | (read -r; printf "%s\n" "$REPLY"; sort) > parental_age.csv
		
		STEP 2: #Remove header to allow for joining
		sed '1d' parental_age.csv > NEWparental_age.csv
		
		STEP 3: #sort by the proband id column and save new
		sort -k 1 NEWparental_age.csv > sortedNEWparental_age.csv
		
		STEP 4: Join the 1043aau_mf_joined.vcf and sortedNEWparental_age.csv file at the proband id
		join -1 1 -2 1 1043aau_mf_joined.vcf sortedNEWparental_age.csv > 1043aau_mf_age_joined.vcf
		
		
		STEP 5: Add in headers to the new joined vcf file :^D
		TRACKED HEADERS: Proband_id	fathers_count 	father	 mothers_count 	mother 	father_age	 mother_age
			sed  -i '1i FID IID PAT MAT SEX PHENOTYPE' test.txt
			sed  -i '1i Proband_id fathers_count father mothers_count mothers father_age mother_age' 1043aau_mf_age_joined.vcf 
			echo -e "Proband_id\fathers_count\father\mothers_count\mother\father_age\mother_age" | cat 1043aau_mf_age_joined.vcf 
			> file2
			echo "Proband_id fathers_count father mothers_count mother father_age mother_age" > headers.vcf
			cat 1043aau_mf_age_joined.vcf >> headers.vcf
			
			Didn't work...
			
		JK, just gonna do that in python lmao
		
		
#Exercise 2: Fit and interpret linear regression models with Python

	1. Use numpy genfromtxt to load the “joined” data from step 3 into a numpy array.
		CODE:
		#!/usr/bin/env python
		
		import numpy as np
		import matplotlib.pyplot as plt
		#import statsmodels.formula.api as smf
		#import statsmodels.api as sm
		#from scipy import stats
		
		#WORKING FILE: 1043aau_mf_age_joined.vcf 
		#TRACKED HEADERS: Proband_id	fathers_count 	father	 mothers_count 	mother 	father_age	 mother_age
		df = np.genfromtxt("1043aau_mf_age_joined.vcf", delimiter = " ", dtype = None, encoding = None, names = ["Proband_id", "father_mutation_count", "father", "mother_mutation_count", "mother", "father_age", "mother_age"])
		
		fig, ax = plt.subplots()
		
	2. 	Plot count of maternal de novo mutations vs. age for mothers and fathers
		CODE:
		################ FEMALES ############################################
		ax.scatter(df["mother_age"], df["mother_mutation_count"], cmap='viridis')
		
		ax.set_ylabel("Count of mutations")
		ax.set_xlabel("Age")
		ax.set_title("Mothers", fontsize = 10)
		#ax.legend()
		
		plt.show()
		
		#plt.savefig("ex2_a.png")
		#plt.close(fig)
	 
	 
		################   MALES ############################################
		#ax.scatter(df["father_age"], df["father_mutation_count"], color = "orange" )
		
		ax.set_ylabel("Count of mutations")
		ax.set_xlabel("Age")
		ax.set_title("Count of mutations versus age in fathers", fontsize = 14)
		#ax.legend()
		
		#plt.show()
		
		#plt.savefig("ex2_b.png")
		#plt.close(fig)
 		
					
	 3. Use ordinary least squares smf.ols() to test for an association between maternal age and maternally inherited de novo mutations.
	 	CODE:
		df = smf.ols(formula = "mother_mutation_count ~ 1 + mother_age", data = df)
		results = df.fit()
		print(results.summary())
		
		A) Is this relationship significant?
			Yes, the P|>|t is 0.000, meaning there is a significant effect of mother age on mother mutation count.
		B) What is the size of this relationship?
			I am unsure what you mean regarding "size of relationship", but the relationship expression can be written as such:
			
			mother_mutation_count = 2.4833 + 0.3786x
			*The relationship of this linear model isn't super strong at Adj. R^2 = 0.226
			
			Prob (F-statistic):           6.38e-24	
		

	4. Use ordinary least squares smf.ols() to test for an association between paternal age and paternal inherited de novo mutations.
	 	CODE:
		df = smf.ols(formula = "father_mutation_count ~ 1 + father_age", data = df)
		results = df.fit()
		print(results.summary())
		
		A) Is this relationship significant?
			Yes, the P|>|t is 0.000, which is again showing a significant effect of paternal age on paternally inhereted mutation counts.
		B) What is the size of this relationship?
			Again, I presume you are meaning the linear regression model, included here:
			
			father_mutation_count = 10.3887 + 1.3513x
			*This also has a stronger adjusted R^2 value of 0.616 for the fit of the model to the data.
			
			Interestingly, the Prob (F-statistic) = 5.60e-84, which is extremely low.
			
		-It appears that fathers have more of an effect on the number of mutations than mothers, but there could be another variable to explain this.
		-We can also calculate how significantly different these values are in the next section.
		
	5. Plot a histogram of the number of maternal de novo mutations and paternal de novo mutations per proband on a single plot with semi-transparency (and upload as ex2_c.png).
		CODE:
		df = np.genfromtxt("1043aau_mf_age_joined.vcf", delimiter = " ", dtype = None, encoding = None, names = ["Proband_id", "father_mutation_count", "father", "mother_mutation_count", "mother", "father_age", "mother_age"])
		

		fig, ax = plt.subplots()
		
		ax.hist(df["mother_mutation_count"], label = "mothers", alpha = 0.6)
		ax.hist(df["father_mutation_count"], label = "fathers", alpha = 0.5)
		ax.legend()
		ax.set_ylabel("Frequency of the count of mutations")
		ax.set_xlabel("Count of mutations")
		ax.set_title("Comparing the frequency and count of mutations \n between mothers and fathers to age", fontsize = 14)
		
		#plt.show()
		
		plt.savefig("ex2_c.png")
		plt.close(fig)
		
	
	6. Test whether the number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband.
		print(stats.ttest_ind(df["father_mutation_count"], df["mother_mutation_count"]))
		#OUTPUT:    
		Ttest_indResult(statistic=53.323950583065304, pvalue=1.1656909236893846e-263
			
		VERY significant :^) males more mutation.

	
	7. Predict the number of paternal de novo mutations for a proband with a father who was 50.5 years old at the proband’s time of birth.
		print(10.3887 + 1.3513*50.5)
		#OUTPUT: 78.62935
	


