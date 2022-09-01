You've made great progress on the bed parser! It looks like you have all the code blocks set aside for the things you have to do for this script. I'll try to summarize what you have left to do, in case that helps you check off items:

* For bed8 and up files (when `len(fields) >= 8`), you're currently checking to make sure it splits into three items. You'll want to also convert each of those list items into an integer, and replace `fields[8]` with your converted list
* Similarly, for bed12 files (when `len(fields) == 12`), you want to:
    * Strip the `,` characters from the ends of columns 11 and 12, and replace those columns (`fields[10]` and `fields[11]`) with lists of integers
    * Make sure the number of elements in the `fields[10]` and `fields[11]` lists is the same as the number in `fields[9]`
* Print the number of malformed entries at the end of the script

You're so close to being done though! Good luck with finishing things, and you can always ask a TA for help if you want more tips.

Also one small suggestion: Instead of doing `if` and `if not`, you can do `if` and `else`! The `else` block will run if the `if` statement evaluates to false.
