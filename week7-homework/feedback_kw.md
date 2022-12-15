# Week 8 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10 points out of 10 possible

1. call and phase variants with `medaka_variant` for 2/4 regions (0.5 pts each)

2. call and phase variants with `medaka_variant` for 2/4 regions (0.5 pts each)

3. mark reads with the correct haplotype tag with `whatshap haplotag` for 2/4 regions (0.5 pts each)

4. mark reads with the correct haplotype tag with `whatshap haplotag` for 2/4 regions (0.5 pts each)

5. split reads into two files based on their haplotype with `whatshap split` for 2/4 regions (0.5 pts each)

6. split reads into two files based on their haplotype with `whatshap split` for 2/4 regions (0.5 pts each)

7. properly changed the colorscheme for igv (0.5 pts) and made/loaded the index files (0.5 pts)

8. submitted 2 `.png` files from the IGV window, one for 2/4 regions (0.5 pts each)

9. submitted 2 `.png` files from the IGV window, one for 2/4 regions (0.5 pts each)

10. Part 6 question: Do you expect each region in H1 or H2 to correspond to the same parent of origin (i.e. the same haplotype)? Explain your reasoning. --> We actually can't guarantee that all H1 are from the same parent. The software are processing all of these regions separately, and aren't sharing information about the regions. Also, each chromosome independently segregates in cell division. Because of these reasons, we're combining all of the H1 and all of the H2 for simplicity's sake in visualizing/processing with igv, but we can't guarantee same parental origin biologically. And methylation presence isn't biological parent specific. For the chr14 locus, the paternal chromosome has methylation rather than the maternal chromosome like in the chr15 locus.
