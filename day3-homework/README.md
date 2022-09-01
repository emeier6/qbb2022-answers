# QBB2022 - Day 3 - Homework Exercises Submission
	git add README.md ex2_a.png
	git commit -m "edited figure and answers for day 3 hw exercise 2"
	git push

#Exercise 1 - Have PLINK return the first 3 principal components.
	#FILE USE LOCATION: /Users/cmdb/data/vcf_files/ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz

	    #LOOK at file:
	        #gzcat ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz | head

	#open plink in bash, running in base terminal    
	plink
	#make the gz into vcf file with --vcf
	#look at the pca only first 3 columns with -- pca 3
	--vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3


	#OUTPUT: Results saved to plink.eigenval and plink.eigenvec .
	

#Exercise 2 - 
	import sys
	import numpy as np
	import matplotlib.pyplot as plt   

	#fname = sys.argv[1]
	#PCA coordinates from each sample stored in eigenvec
	    #In linear algebra terms, these are the first and second eigenvectors of the covariance matri

	    #figuring out what to name in eigenvec
	        #Step 1: 
	            #less -S plink.eigenvec
	        #Step 1:
	            #Name the eigen values, which there are 5 
	                #columns 1 and 2 are the same ID 
	                #Column 3 = PCA1
	                #Column 4 = PCA2
	                #Column 5 = PCA3

	eigenvec = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["Sample", "Sample", "PCA1", "PCA2", "PCA3"])
	#eigenval = np.genfromtxt("plink.eigenval")


	#CHECK:print(eigenvec)

	## Plot PCA1 versus PCA2


	fig, ax = plt.subplots(nrows=1)

	#ax is the subplot
	    #ax.scatter(eigenvec["PCA1"], eigenvec["PCA2"], label = "Comp. PCA1 to PCA2")
	    #ax.set_ylabel("PCA2")
	    #ax.set_xlabel("PCA1")    
	#ax.legend()

	#CHECK:plt.show()
	    #LOOKS GREAT OMG :,^)


	#SAVING PCA1 to PCA2 AS A FIGURE:


	#plt.savefig("FILENAMETOSAVETO")
	    #need to denote as.png or .pdf, which ever file makes the most sense
	#plt.savefig("ex2_a.png")
	#plt.close(fig)


	ax.scatter(eigenvec["PCA1"], eigenvec["PCA2"], label = "Comp. PCA1 to PCA3")   
	ax.set_ylabel("PCA1")
	ax.set_xlabel("PCA3")    
	#ax.legend()
	#CHECK:plt.show()
	    #SHE GORGEOUS

	#RUNNING IN BASH: python plink.py ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz 



	plt.savefig("ex2_b.png")
	plt.close(fig)

	#OUTPUT: These two files are now saved as "ex2_1.png" and "ex2_b.png" and uploaded into github
	
#EX2b - Do you notice any structure among the points? 
	Yes! There is structure among the points! 
#EX2c - What do you think these populations represent?
	The structures appear to cluster in both figures, where you have wo populations separated in the lower PCA1 values.
	Comparatively, you have a streiation more toards the larger part of PCA1/PCA3 x-axis, which denotes another separated population.
	These clumps are representative of populations, where the population clusters stacked on top of each other are different, but more closely related to each other compared to the straeated line edging towards the right of the PCA graphs. 
	#What do you think this structure represents?	
	


#Exercise 3 -
	cp /Users/cmdb/data/metadata_and_txt_files/integrated_call_samples.panel .
	#CHECK with ls
	sort plink.eigenvec > sortedEigen
	sort integrated_call_samples.panel > sortIntCalls
	join sortedEigen sortIntCalls
	#RUN TO CHECK
	join sortedEigen sortIntCalls > sortedEigenIntCalls
	
NP3.py
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
		for i, country in enumerate(country_list):
		    row = np.where(EigenInt["Country"] == country)
		    print(row)
		    xg.append(EigenInt["PCA1"][row])
		    yg.append(EigenInt["PCA2"][row])
		    ax.scatter(xg[i], yg[i], label = country )
		ax.set_ylabel("PC2")
		ax.set_xlabel("PC1")    
		#ax.legend(loc="best", mode = "expand", ncol = 6)
		ax.legend(loc='upper right', bbox_to_anchor=(1, 1.15),
		          ncol=6, fancybox=True, shadow=True)

		#CHECK:
		#plt.show()
		    #LOOKS GREAT
		plt.savefig("ex3_a.png")
		plt.close(fig)

		#RUN:python np.py sortedEigenIntCalls

		#COUNTRY
		#cut -f 6 sortedEigenIntCalls | sort | uniq -c 

		#CONTINENT
		#cut -f 7 sortedEigenIntCalls | sort | uniq -c 

		#SEX
		#cut -f 8 sortedEigenIntCalls | sort | uniq -c 


		#RUN: python np3.py sortedEigenIntCalls
		


NP2.py
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