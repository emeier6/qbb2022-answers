#!/usr/bin/env python3
#conda install openblas -y 
    #takes a minute

### Interactive Python interface for the Interactive lecture:
###### DATA EXPLORATION AND VISUALIZATION

    #Using differnt types of graphing to visualize the data
    #Understand different uses of imports/modules

#Libraries:
    #Matplotlib, biopython, numpy, ...
    
        #NumPY: efficient numerical analysis
        #SciPy: clustering, lin alg
        #Statsmodels: Statistics and ML

#Importing:
    #importing pre-made code
        #alias "np" can be anything
#    import numpy as np
    
    #importing a parsed file
        #"parse_vcf" can be anything
#    from vcfParser import parse_vcf
    
#Data visualization - MATPLOTLIB
    #single, double, multidimensional
    #Good resource in the bootcamp, as well as fundamentals of data visualization
    #https://clauswilke.com/dataviz
    
    #STEP 1: Import matplotlib
    
################ IN CLASS LIVE TUTORIAL #########################################

    
import matplotlib.pyplot as plt    

#create some strings of information
x = [1, 2, 3, 4, 5]
y = [25, 8, 2, 8, 25]

x2 = [2, 4, 6]
y2 = [8, 64, 216]

#Create new figure and axis
    #Will memorize this at a certain point, just for plotting formatting
    #subplots allows us to lay out multiple panels on a plot
    #fig = entire plotting space
    #ax = panel
#fig, ax = plt.subplots()
#Now, making two seperate panels
fig, ax = plt.subplots(nrows=2)
print(len(ax))
    #this shows us we have two panel
    
#ax.plot(x, y, label = "x^2")
ax[0].plot(x, y, label = "x^2")
    #can make another call for ax.plot on the same panel as the previous one
#ax.plot(x2, y2, label = "x^3")
ax[1].plot(x2, y2, label = "x^3")
ax[0].legend()
ax[1].legend()
    #legend allows you to add labels, but can only be added if we show the plot with    
    #cannot run a legend on an array with only one variable 
#plt.show()

print(genes_per_chrom)    #plt.savefig("FILENAMETOSAVETO")
    #need to denote as.png or .pdf, which ever file makes the most sense

plt.close(fig)
    #will plot, then need to close the plot before continuing with coding :^)


    #NEED TO SILENCE plt.show() THIS AND THEN RUN BACK THE ./day3-afternoon.py IN ORDER TO OVERWRITE FILE NAME
    #THIS WILL THEN ALLOW FOR THE FILE TO BE SAVED AND OPENABLE with:
        #open lineplot.png
        
