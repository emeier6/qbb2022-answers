# Week 1 Genome Assembly -- Feedback

1 + 1 + 1 + 0 + 0.5 + 1 + 0.75 + 1 + 1 + 1 = 8.25 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * good --> +1

2. Question 1.2, 1.4 simulation script(s)

  * looks good --> +1

3. Question 1.2, 1.4 plotting script(s)

  * looks good --> +1

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * I see where the plots would be saved in your script, but I don't see the plots. Please add. --> +0

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * answer appears incomplete --> +0.5

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size --> +0.25, that's not the n50. It should be one of the contig sizes you've listed already. Specifically, you want to order the contigs by length, largest to smallest, and then sum to find the contig whose length is shorter than or equal to other contigs larger than it, such that the sum of these contigs is half the genome length.

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> + 0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> +0.33

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.5
  * length of novel insertion --> +0.5, you want to add one to that length. Length is end - start + 1

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.5
  * secret message --> +0.5
