CHAPTER 18
MEIER_tail.py


FUNCTIONAL CODE:
Command Line: random_snippet.vcf -1

#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys #import module
filename = sys.argv[0] #SET the input filename
if len(sys.argv) > 2: #IF user-specified number of lines provided
  n_lines = int(sys.argv[2]) #SET the desired number of lines
#END IF
else: #OTHERWISE
  n_lines = 10 #SET the desired number of lines to a default
#END OTHERWISE
with open('random_snippet.vcf', 'r') as file: ##SET a storage list for lines in the file
    for i, line in enumerate(file): #FOR every line in the open file
      if i < n_lines: #IF a desired line by its numerical position
       print(line.strip('\r\n')) #PRINT the line
#END FOR

with open("random_snippet.vcf", "r") as file: #SET a subset of the storage list to be the last ____ items in the storage list
    for line in file: #FOR every line in the subset (file_in composed to the last two numbers in set)
     print(line.strip('\r\n')[-1:]) #Print the line

'''
NOTE: I know this code isn’t the best, and it doesn’t include the add to list (append). However, when I reworded that into the code, it would not run the later section. This is the other code that I have yet to figure out:

NON-FUNCTIONAL CODE:

Command Line: random_snippet.vcf -1

#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys #import module
filename = sys.argv[0] #SET the input filename
if len(sys.argv) > 2: #IF user-specified number of lines provided
  n_lines = int(sys.argv[2]) #SET the desired number of lines
#END IF
else: #OTHERWISE
  n_lines = 10 #SET the desired number of lines to a default
#END OTHERWISE
with open('random_snippet.vcf', 'r') as file: ##SET a storage list for lines in the file
    for i, line in enumerate(file): #FOR every line in the open file
        file.append(int(line.strip())
    ##END FOR

with open("random_snippet.vcf", "r") as file: #SET a subset of the storage list to be the last ____ items in the storage list
    for line in file: #FOR every line in the subset (file_in composed to the last two numbers in set)
     print(line.strip(‘\r\n’)[-1:]) #Print the line
    #END FOR
'''
