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

# You're definitely on the right track here. There are three errors that I see
# that are going to prevent from doing what you want. The first is that the
# filename is actually sys.argv[1], not sys.argv[0]. That list contains all of
# things on the command line following "python", so the first item (index 0) is
# actually the name of the script. The next issue is that in your second for
# loop, you are getting each line, but you are pulling out the last character
# from it using [-1:]. I think I understand what you are going for. However,
# before you can get the last lines of the file, you need to store them, which
# you clearly understand from your second block of code. Unfortunately, your
# second block won't work because you are trying to convert the line into an
# integer. Once you have your list of lines ("file"), then you don't need to the
# file anymore. You can just loop through your list. This list is what you
# want to take a slice out of, but instead of -1 (which is the last item), you
# need [-n_lines:], which gives you the last n_lines lines. You're so close.
# Definitely keep at it because you're almost there. - Mike