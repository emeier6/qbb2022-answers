#Homework Exercise – Plot a heatmap, visualizing power for unfair coin tosses



#A – Expand simulation conditions
	A) probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
		-I get three values:
			0.85
			0.0
			0.93
		-The numpy.arange(0.55, 1.05, 0.05) corresponds to the start number, the stop number, and the step number.
			Print the numpy arange: [1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55]
		-The step is set at 0.05, so we see the values change by 0.05. 
		-The order is inverted because [::-1] inverses the list generated, so it starts and the highest value (1.05 is excluded)
	B) numpy.around( ,decimals=2)
		-Rounds to the nearest decimal given a number of decimals so that you don't get a massive streak of decimals
			Print both numpy arange and numpy around arange
			#OUTPUT:
			[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]
			[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]
		-I am not seeing a difference in the range of values, but I presume there is a benefit when working with oddly-spaced set data intervals
		-The order is inverted because [::-1] inverses the list generated, so it starts and the highest value (1.05 is excluded)

#B – Compute and store power
	Taking the single output and now putting it in a larger combined list
		-The double for loop loops first through probability list, and then the second for loop add the search for tosses.
		-But, we are only looking to relate the single line or value of each of the probabilities, and for each of the tosses. 
		-The tosses is a list, but we are not filling in a list for each of the matrix points, just a single point that was defined as the single toss variable. 
		-The same is true for probs and single probs. then, we can print the power_twoD to see if we ran this correctly.
		 The code:
	power_twoD = numpy.zeros((len(probs), len(tosses)))
	for i, singleprob in enumerate(probs):
	    for j, singletoss in enumerate(tosses):
	        power_twoD[i,j] = run_experiment(singleprob, singletoss, correct_the_pvalues = True)
	print(power_twoD)
	

#C – Plot
	A)
		CODE:
		#Creating a heat map plot of the matrixed values = power_twoD
		fig, ax = plt.subplots()
		ax = sns.heatmap(power_twoD, vmin = 0, vmax = 1, annot=True, annot_kws={"size": 7}, xticklabels=tosses, yticklabels=probs, cmap='cubehelix')
		ax.set_xlabel("Array of tosses")
		ax.set_ylabel("Array of probabilities")    
		ax.set_title("Power matrix of probability and tosses array")

		#plt.show()

		plt.savefig("SHE.png")
		plt.close(fig)

	B) comment on any trends that you observe within your heatmap for the relation of power with the probability or number of toss parameters
		-As you increase the skew or increase the likelyhood of the outcome for heads by weighing it, then it takes less iterations to increase the likelyhood of returning a head to 1.
		-However, if we make the coin more fair (~0.55 probability), then it takes many more iterations to increase to the desired outcome.
		-Also, increasing the number of iterations of the simulation allows us to more quickly get to the desired outcome (in this case, 1)
		
	C) Make two plots one with and one without corrections
			CODE:
			fig, (ax1, ax2) = plt.subplots(ncols=2)
			sns.heatmap(power_twoD_Corr, ax=ax1, vmin = 0, vmax = 1, annot=True, cbar=False, annot_kws={"size": 7}, xticklabels=tosses, yticklabels=probs, cmap='cubehelix')
			ax1.set_xlabel("Array of tosses")
			ax1.set_ylabel("Array of probabilities")    
			ax1.set_title("Corrected power matrix of \n (probability v. tosses) arrays")

			sns.heatmap(power_twoD, vmin = 0, vmax = 1, ax=ax2, annot=True, cbar=False, annot_kws={"size": 7}, xticklabels=tosses, yticklabels=probs, cmap='cubehelix')
			ax2.set_xlabel("Array of tosses")
			ax2.set_ylabel("Array of probabilities")    
			ax2.set_title("Uncorrected power matrix of \n (probability v. tosses) arrays")

			#plt.show()

			plt.savefig("Comp_Corr_NonCorr.png")
			plt.close(fig)
		
		-Uncorrected shows that at lower iteration numbers, the power is higher, aka the rate of false positives is higher.

#D – Compare to a real study
	A) THE BIOLOGY:
		-As human sperm are diploid, it is assumed that there would be an equal likelihood of passing on each allele.
		-Carioscia et al. (2022) use single-sperm sequencing to discuss an effect known as "transmission distortion" (TD).
		-TD results in alleles being disproportionately passed on, as it is thought that some alleles affect aspects of fertility, including:
			-include meiotic drive,
			-gamete competition or killing,
			-embryonic lethality, and
			-mobile element insertion,
		for the purpose of having a higher likelihood of passing on the allele. 
	B) Figure S13 Summary:
		-Here, we see the importance of power correction when looking at sperm transmission rate in comparison to sperm number.
		-Using the Bonferroni-adjusted p-value, we see in figure B that the power decreases, thereby decreasing and attempting to account for false positives in the computation.
		-The claim, which is supported in Fig S13, is that the Bonferroni-adjusted p-value increases the statistical power to call small TD at single loci by more than 80%.
	C) compare the simulation experiment that you performed with the simulation experiment performed for Figure S13.
		-Essentially, theFig S13 and the simulated/in-class generated figure "Comp_Corr_NonCorr" show the same thing:
			General Trends:
				-As sample size increases, the power to call smaller probabilities increases. However, there is still a threshold to call.
				-Additionally, as the probability increases even in smaller iteration sizes, there is more power to call.
			
		-The parameter that corresponds to transmission rate (TD) is the probability, aka:
				probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]
				
		-The parameters that corresponds to the Number of sperm axis is the tosses, aka:
				tosses = numpy.array([10, 50, 100, 250, 500, 1000])
				
		-We use the binomial test and Bonferroni correction to ask how different our observed values are to the expected values. In this case, both expected values are 0.5 probability of either: heads or tails, or sperm alleles being passed on.
		Uncorrected:
			-We see a greater power given to both probability and iteration arrays, where as there are both less iterations and lower probabilities, there is still greater power to call.
		Corrected:
			-The Bonferroni-adjusted method and power correction allows us to decrease the power and ability to call.
			-This is done by accounting for the number of false positives, which the alpha p-value level of significance threshold states that a p-value below 0.05 denotes that the difference in our observed versus expected values is significant.
			-So, by accounting for a false-positive rate of 5% (0.05), we can adjust the p-value to the total number of samples/iterations we are testing.
			-This is noted with p-value = 0.05 / #iterations or samples
				-This is extremely important because as sample sizes increase, we expect a greater total number of false positives.
				-Alternatively, smaller sample sizes are more likely to be affected by skew and false positives, so it is a better way to account for any sort of variation that could affect a call for significance.
		
				
#E – Submit