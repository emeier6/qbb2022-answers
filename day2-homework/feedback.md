Great work writing documentation of `vcfParser.py`! I can tell from your annotations that you were really thinking through what each line was doing as you wrote it down.

Also great work on your dbSNP VCF annotater script. It might also help to go through this script at some point and add some comments, so that future you remembers what each line is doing!

One comment I have about your current script is regarding your dbSNP dictionary. Remember that we're using this dictionary to look up SNPs for which we have the chromosome and position, and want to know the SNP ID. So that means that the key of each dictionary entry should contain the chromosome and position, and the value should contain the SNP ID. That might explain why your counter is only going up to 24 (I think you should expect to see 100 random_snippet SNPs that aren't in the dbSNP database).
