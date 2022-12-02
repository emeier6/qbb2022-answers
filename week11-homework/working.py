#!/usr/bin/env python

import scanpy as sc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sc.settings.verbosity = 2             
# verbosity: errors (0), warnings (1), info (2), hints (3)
sc.logging.print_header()
sc.settings.set_figure_params(dpi=80, facecolor='white')
results_file = 'write/pbmc3k.h5ad'  
# the file that will store the analysis results


# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

# print(sc.__version__)
# print(adata)
# Var: 'gene_ids', 'feature_types', 'genome'



# # only consider genes with more than 1 count
# sc.pp.filter_genes(adata, min_counts=1)
# # normalize with total UMI count per cell
# sc.pp.normalize_per_cell(adata, key_n_counts='n_counts_all')
# # select highly-variable genes
# filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor='cell_ranger')

# filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor='cell_ranger', n_top_genes=1000, log=False)

## Subset the genes
# sc.tl.pca(adata, svd_solver='arpack')
# sc.pl.pca(adata, save = "unfiltered.png")


filtered = sc.pp.recipe_zheng17(adata, n_top_genes=1000)
# Pulling out the gene names
gene_names = adata.var.index
# Output: length=999

# print(gene_names)

## Making a PCA plot
# sc.tl.pca(adata, svd_solver='arpack')
# sc.pl.pca(adata, save = "filtered.png")

sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
# sc.tl.leiden(adata)




# sc.tl.tsne(adata)
# sc.pl.tsne(adata, color='leiden', save = "TSNE.png")
# adata.write(results_file)

# sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
# sc.pl.rank_genes_groups(adata, n_genes=25, sharey=False)
# adata.write(results_file)

# Make a list of the genes appearing with the highest score from the rank_genes by _groups data with leiden and t-test methods
# This also does n_25 most prevalent genes for clustering
candidate_genes = ["Nrxn3", "lgfbpl1", "Gria2", "Basp1", "Mdk", "Islr2", "Tmsp4x", "Dbi", "Stmn2", "mt-Atp6", "Hmgb2", "Meg3", "Hbb0bs", "mt-Co3", "Tmsb10", "Cldn5", "Reln", "Tuba1a", "Rgs5", "C1qb", "Stmn1"]
# print(candidate_genes)
# print(len(candidate_genes))
# OUTPUTS: Look good and have the correct number of genes listed and number = 21 genes

#  Genes list: 
#       Nrxn3  in BRAIN and lung! (AC)
#       Gria2 in BRAIN and lung! (AC)
#       Basp1 in BRAIN and lung! (MG)
#       Mdk in BRAIN and lung! (FB2, FB1, AC)
#       Islr2 in BRAIN and lung! (FB1, aEC)
#       Dbi in BRAIN and lung! (OL, AC)
#       Stmn2 in BRAIN and lung! (aEC)
#       Hmgb2 in BRAIN and lung! (MG)
#       Meg3 in BRAIN and lung! (MG, FB2)
#       Tmsb10 in BRAIN and lung! (EC1, vEC,capilEC...)
#       Cldn5 in BRAIN and lung! (vEC, EC1-3, capilEC, aEC)
#       Reln in BRAIN and lung! (AC)
#       Tuba1a in BRAIN and lung! (OL)
#       Rgs5 in BRAIN and lung! (cSMC, aaSMC, PC)
#       C1qb in BRAIN and lung! (MG)
#       Stmn1 in BRAIN and lung! (OL)

brain_marker_genes_dict = {
    'AC': ['Nrxn3', 'Gria2', 'Mdk', 'Dbi', 'Reln'],
    'MG': ['Basp1', 'Hmgb2', 'Meg3', 'C1qb'],
    'FB2': ['Mdk', 'Meg3'],
    'FB1': ['Mdk', 'Islr2'],
    'aEC': ['Islr2', 'Stmn2', 'Cldn5'],
    'OL': ['Dbi', 'Tuba1a', 'Stmn1'],
    'EC1': ['Tmsb10', 'Cldn5'],
    'EC2': ['Cldn5'],
    'EC3': ['Cldn5'],
    'capilEC': ['Tmsb10', 'Cldn5'],
    'vEC': ['Tmsb10', 'Cldn5'],
    'cSMC': ['Rgs5'],
    'aaSMC': ['Rgs5'],
    'PC': ['Rgs5']
}


brain_list = ['Nrxn3', 'Gria2', 'Basp1', 'Mdk', 'Islr2', 'Dbi', 'Stmn2', 'Hmgb2', 'Meg3', 'Tmsb10', 'Cldn5', 'Reln', 'Tuba1a', 'Rgs5', 'C1qb', 'Stmn1']
# print(len(brain_list))

# print(adata)
sc.tl.umap(adata, maxiter= 1000)

# sc.pl.umap(adata, color='leiden', save = "UMAP.png")
## Test with a single gene figure. Looks good! Very basic. Trying to add in multipanel genes from the list created earlier and look pretty :)
# plt.rc_context(sc.pl.umap(adata, color=brain_list, save = "Brain_cell_list_UMAP.png"))
## This outputs them all differentially and looks great! Some definitely look more specialized/localized than others.

sc.tl.leiden(adata, key_added='clusters', resolution=0.5)
# plt.rc_context(sc.pl.umap(adata, color='clusters', add_outline=True, legend_loc='on data',legend_fontsize=12, legend_fontoutline=2,frameon=False, title='clustering of cells', palette='Set1', save = "UMAP_leiden_clusters.png"))

sc.pl.dotplot(adata, brain_marker_genes_dict, 'clusters', dendrogram=True, save = "dotplot_with_dictionary.png")
# save = "dotplot_with_dictionary.png"
cluster2annotation = {
    '1, 3, 4, 6, 8, 16': 'AC',
    '3, 10, 18': 'MG',
    '2, 9': 'FB2',
    '2, 9': 'FB1',
    '4': 'aEC',
    '3': 'OL',
    '17': 'cSMC',
    '17': 'aaSMC',
    '17': 'PC'
}

# sc.pl.dotplot(adata, brain_marker_genes_dict, 'cell type', dendrogram=True)
#
# sc.pl.umap(adata, color='cell type', legend_loc='on data',
#            frameon=False, legend_fontsize=10, legend_fontoutline=2)
#
# plt.rc_context(sc.pl.violin(adata, ['Gria2', 'Basp1'], groupby='clusters' )