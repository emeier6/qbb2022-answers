Great work on this Emily! I'm sorry the last part was such a struggle, but I have some suggestions for how you might be able to speed it up. First, a couple minor comments:
1. When you're calculating the length of the bins for Question 3C, you've got the right idea, but we don't actually care about the total length of the `assembly.fasta` for this question. The `assembly.fasta` file has genomic information for a bunch of different species strains. We're using it as our reference because we expect our sample to have a bunch of different strains of bacteria. The only thing that matters is the raw length of the bin (which you've calculated here already). Those lengths look to be in the megabase range, which is on the order we would expect for a prokaryotic genome (although currently you're including new line characters in the count... how could we get rid of those?) (no points deducted)
2. When you're doing the binning, we were intending that you would find bins across ALL time points at once. At this point, we're less interested in the make-up over time, and more so interested in just ALL of the species/strains present. You can do this by just running `jgi_summarize_bam_contig_depths` on all BAM files at once (e.g. input `SRR*.bam`) and then running `metabat2` once on the output of that command. You should still get 6 bins, which makes sense, because the last time point is already really diverse. (-0.25 point)

Okay, so how can we speed up the analysis for Step 3. You've got the right idea that we want to look at the taxonomy of all of the contigs within each bin. But, as you learned yourself, some of the bins can have a TON of contigs. So, how do we go about dealing with that? What I would suggest is--for each bin--looping through all of the contigs within that bin, and for each, grepping it against the `assembly.kraken` file. One way to structure this might be:

```
for contig_id in $(grep ">" bin.1.fa |  cut -d ">" -f 2)
do
    grep $contig_id assembly.kraken
done
```

Then, we could pipe the output of that for loop to a couple of `cut` commands to get the taxonomic information we're interested in. If you haven't seen the `$()` structure before, it essentially allows you "capture" the output of running a command, where you can store it in a variable, or in this case, loop through it.

This was a really solid effort though, so great work.

(9.75/10)
