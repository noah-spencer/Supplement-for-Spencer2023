# Supplement-for-Spencer2023

Python & Processing.py scripts used for transcriptomic analysis of cicada endosymbionts. The relevant preprint/publication will be linked here once it is available.

## Coverage Plots

Scripts and data for plotting strand-specific, per-base RNA-seq coverage along annotated *Hodgkinia* and *Sulcia* genomes/chromosomes.

### ProcessGFF_Hodgkinia.py & ProcessGFF_Sulcia.py

Written by Piotr Łukasik, Noah Spencer in Python 3.

These scripts take a GFF3 *Hodgkinia* or *Sulcia* genome annotation file as input. Direct the output to a text file with extension .pro, *e.g.* TETUND.pro, SMDICSEM.pro, *etc.*.

Annotation files can be found in the "Annotations" directory. Example output files suitable for input to PlotCoverage.pyde are also provided.

For *Sulcia* MAGSEP, the *Sulcia* genome from *Magicicada tredecim* is used (see Methods section). For *Hodgkinia* MAGSEP, the .pro files for each contig will need to be separated before use in PlotCoverage.pyde. To achieve this, simply execute the included bash script MAGSEParate.sh after generating the file MAGSEP.pro using ProcessGFF_Hodgkinia.py.

### PlotCoverage.pyde

Written by Piotr Łukasik, Noah Spencer in Processing 3.5.4 (Python mode).

This script takes the following files as input: a two-column text file giving per-base RNA-seq coverage along a genome/chromosome (output from the genomecov -d command in BEDTools v.2.24.0, see Methods section) and annotation information in a comma-separated text file (output from ProcessGFF.py script). The output is one or more images in a PDF format. For best results, run in the Processing 3.5.4 IDE (in Python mode) and adjust the spec_colors, SPEC_LIST, GENOME_LIST, and scale_y variables as appropriate for your genome or genomes of interest.

Files containing the per-base coverage data can be found in the "PerBaseCoverage" directory and are organized first by endosymbiont (*Hodgkinia* or *Sulcia*) and then by host species. For each endosymbiont+host pairing, there are a total of 6 files giving plus and minus strand coverage values from each of three specimens (except in *Hodgkinia* MAGSEP, *Sulcia* MAGSEP, and *Hodgkinia* TETULN, which have data from only 2 samples).