

#knowing what conda environments are available. Also shows us if packages are compatable, and which conda we are in
conda info --env

#undestanding what is installed. Also tells us the version of each installed conda
conda list | less

    #Question about environment:
        #1. Would you have to open the environment, IE cmdb-meme, to see what is in there?
            conda list -n bcftools | less -S
            #allows you to see what is in the file, the version, the channel and the build
        #2. Can you auto update? -Maybe, but shouldn't have things change unless you know. 
    

##################################################
# In class exercise

conda create --name day4-morning
    #OUTPUT: Do you want to work in /Users/cmdb/miniconda3/envs/day4-morning ?

[enter] or y

conda activate day4-morning
    #OUTPUT: shows that the base is now day4-morning
    
conda install samtools==1.1
    #OUTpUT: installs samtools version 1.1 as well as a few other base packages
    #asks: Want to install these other packages?

[enter] or y

#Where did this install?
which samtools
    #OUTPUT: /Users/cmdb/miniconda3/envs/day4-morning/bin/samtools 
    #AKA, installed in the base v1.14, but in the working terminal day4-morning is the v1.1
    
samtools --version | less
    #shows us the version in the working directory day4-morning
    
conda deactivate
    #go back to base terminal

which samtools
    #OUTPUT: /Users/cmdb/miniconda3/envs/day4-morning/bin/samtools 
    #Where stored

samtools --version | less
    #OUTPUT: 1.14


