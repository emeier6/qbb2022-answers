# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 0 = 9 points out of 10 possible points

1. Index genome

  * --> +1, but I think there's a typo and that you mean `sacCer3.fa` not `savCer3.fa`

2. align reads

  * --> +1, but again I think there's a typo and instead of `bwa mem -t 4 -R "@RG\tID:A01_11\tSM:A01_11" -o A01_11.sam sacCer3.fa A01_11.sam`, you mean `bwa mem -t 4 -R "@RG\tID:A01_11\tSM:A01_11" -o A01_11.sam sacCer3.fa A01_11.fastq`

3. sort bam files and index sorted bam files (0.5 points each)

  * --> +1; good for loop for indexing the sorted bam files. You can use the loop structure for questions 2 and 3a too.

4. variant call with freebayes

  * --> +1; perfect!

5. filter variants

  * --> +1; fantastic explanation!

6. decompose complex haplotypes

  * --> +1; very good

7. variant effect prediction

  * --> +1; wonderful

8. python plotting script

  * --> +1; nice script overall. Would recommend GQ in the Format/sample specific column, not QUAL in column 5. You want the genotype quality and genotypes are sample specific
  * fascinating way to get the unique and count values for the variant effect annotations! Really like the `set` approach. Also consider the [numpy function `unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html) which will return the unique values and the corresponding counts for you if you use the the `return_counts` argument

9. 4 panel plot (0.25 points each panel)

  * --> +1; nice!

10. 1000 line vcf

  * I don't see the vcf file. Did you do `git add --force <yourweek3.vcf>`?
