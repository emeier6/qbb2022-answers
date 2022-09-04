#!/usr/bin/env python

#CHAPTER 18
#MEIER_tail.py
#RUNNING: ./Meier_tail_MS.py random_snippet.vcf



#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys #import module
#filename = sys.argv[1] #SET the input filename
filename = open("random_snippet.vcf", "r")

if len(filename) > 2: #IF user-specified number of lines provided
       #SET the desired number of lines
       n_lines = int(filename[2])
#END IF
else: #OTHERWISE
      n_lines = 10 #SET the desired number of lines to a default
#END OTHERWISE

lines = []
for i, line in enumarete(filename): ##SET a storage list for lines in the file
    line = filename(i) #FOR every line in the open file
#END FOR

inv_lines = lines[-5:-1]
for i in inv_lines:
     print(line.strip('\r\n')) #Print the line in reverse order



'''

# You're definitely on the right track here. There are three errors that I see
# that are going to prevent from doing what you want. The first is that the
# filename is actually sys.argv[1], not sys.argv[0]. That list contains all of
# things on the command line following "python", so the first item (index 0) is
# actually the name of the script. 
##DONE


#The next issue is that in your second for
# loop, you are getting each line, but you are pulling out the last character
# from it using [-1:]. I think I understand what you are going for. However,
# before you can get the last lines of the file, you need to store them, which
# you clearly understand from your second block of code. Unfortunately, your
# second block won't work because you are trying to convert the line into an
# integer. 

#Once you have your list of lines ("file"), then you don't need to the
# file anymore. You can just loop through your list. This list is what you
# want to take a slice out of, but instead of -1 (which is the last item), you
# need [-n_lines:], which gives you the last n_lines lines. You're so close.
# Definitely keep at it because you're almost there. - Mike