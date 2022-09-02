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
		
		-
		