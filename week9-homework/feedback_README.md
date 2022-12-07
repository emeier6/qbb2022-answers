This is a great start. There are a few more things we need from you for this to be complete:
1. I think you may be clustering the expression a bit weirdly. The output of running `linkage` is an array that describes the dendrogram, so you don't necessarily want to plot it directly as your heatmap. Rather, you want to run `leaves_list` on this array, which will give you an ordered list/array of indicies which you can use to reorganize your `log_trans_filt`. You would do `leaves_list` on both `rows` and `columns` as you have them labeled here, and then use the output to reorganize the rows, then columns of `log_trans_filt`. (-0.2 point)
2. Also, you should be able to just plot the dendrogram on the output of running `linkage` directly. I'm not entirely sure what you're going for with `Zi = sci.ward(pdist(columns))`, but it looks like somehow you lost a sample (there should be 10 branches total) (-0.2 point)
3. We still need your code for the regression (both models), the QQ plot for the model without sex, the volcano plot for the model with sex, and a comparison of the significant (10% FDR) transcripts between the two models (-5 points)

Let us know if you have any questions!
(4.6/10)
