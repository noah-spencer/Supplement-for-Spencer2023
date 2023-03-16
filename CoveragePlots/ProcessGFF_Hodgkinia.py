#! /usr/bin/env python3

import sys

if len(sys.argv) != 2:
    sys.exit(
        'This script processes a gff file, and returns to stdout a table to be used as an input of genome_plotting.\n'
        'Direct the output to a csv file.\n'
        'Usage: ./process_gff.py <gff_file>\n')
Script, Gff_file = sys.argv

### To format the input appropriately for use in the Processing.py script, write stdout to a .pro file with a name that
### matches the genome/chromosome field in your tab-delimited .txt file containing the per-base coverage values.


## Assign Hodgkinia genes to broad functional categories.
Genes = {'rplB': 'riboprot', 'rplC': 'riboprot', 'rplD': 'riboprot', 'rplE': 'riboprot',
         'rplF': 'riboprot', 'rplJ': 'riboprot', 'rplK': 'riboprot', 'rplL': 'riboprot', 'rplM': 'riboprot',
         'rplN': 'riboprot', 'rplO': 'riboprot', 'rplP': 'riboprot', 'rplQ': 'riboprot', 'rplS': 'riboprot',
         'rplT': 'riboprot', 'rplU': 'riboprot', 'rplV': 'riboprot', 'rplX': 'riboprot', 'rplY': 'riboprot',
         'rpmA': 'riboprot', 'rpmB': 'riboprot', 'rpmE': 'riboprot', 'rpmF': 'riboprot', 'rpmG': 'riboprot',
         'rpmI': 'riboprot', 'rpmJ': 'riboprot', 'rpsA': 'riboprot', 'rpsB': 'riboprot', 'rpsC': 'riboprot',
         'rpsD': 'riboprot', 'rpsE': 'riboprot', 'rpsF': 'riboprot', 'rpsG': 'riboprot', 'rpsH': 'riboprot',
         'rpsI': 'riboprot', 'rpsJ': 'riboprot', 'rpsK': 'riboprot', 'rpsL': 'riboprot', 'rpsM': 'riboprot',
         'rpsN': 'riboprot', 'rpsP': 'riboprot', 'rpsQ': 'riboprot', 'rpsR': 'riboprot', 'rpsS': 'riboprot',
         'rsmA': 'riboprot', 'rsmH': 'riboprot', 'rsmI': 'riboprot', 'cobA': 'biosynth', 'cobJ': 'biosynth',
         'cobM': 'biosynth', 'cobL': 'biosynth', 'cobH': 'biosynth', 'cobN': 'biosynth', 'cobS': 'biosynth',
         'cobT': 'biosynth', 'cobO': 'biosynth', 'cobQ': 'biosynth', 'cobD': 'biosynth', 'cobP': 'biosynth', 
         'cbiX': 'biosynth', 'groS' : 'chaperone', 'groL' : 'chaperone', 'dnaJ' : 'chaperone', 'dnaK' : 'chaperone', 
         'hisG': 'biosynth', 'hisI':'biosynth', 'hisA':'biosynth', 'hisF':'biosynth', 'hisH':'biosynth',
         'hisB':'biosynth', 'hisC':'biosynth', 'hisD':'biosynth', 'metC': 'biosynth', 'metH': 'biosynth'}


## Read in GFF3 annotation file.
GFF = open(Gff_file, 'r')


## For each feature in the genome annotation, write the following to a table:
## Chromosome name, gene name, category, putatively functional (vs pseudogenized), gene start, gene end, strand
Genome_list = []
Gene_table = []
for line in GFF:
    Line = line.split()
    if Line[0] == "##sequence-region":
        Genome_list.append(Line[1])
        Gene_table.append(["genome_entry", Line[1], Line[3]])
    elif Line[0] in Genome_list:
        if (Line[2] == "CDS"):
            Gene = 'Other'
            for key in Genes:
                if key in ''.join(Line[8:]):
                    Gene = Genes[key]
            if 'gene=' in ''.join(Line[8:]):
                GeneName = ''.join(Line[8:]).split("gene=")[1].split(";")[0]
            else:
                GeneName = ''.join(Line[8:]).split("locus_tag=")[1].split(";")[0]
            if 'Note=putative pseudogene' in ''.join(Line[8:]):
                Fun = 'Putative'
            else:
                Fun = 'Functional'
            Gene_table.append([Line[0], GeneName, Gene, Fun, Line[3], Line[4], Line[6]])
        elif (Line[2] == "pseudogene"):
            Fun = 'Pseudo'
            Gene = 'Pseudo'
            if 'gene=' in ''.join(Line[8:]):
                GeneName = ''.join(Line[8:]).split("gene=")[1].split(";")[0]
            else:
                GeneName = ''.join(Line[8:]).split("locus_tag=")[1].split(";")[0]
            Gene_table.append([Line[0], GeneName, Gene, Fun, Line[3], Line[4], Line[6]])
        elif (Line[2] == "rRNA"):
            if 'Note=putative pseudogene' in ''.join(Line[8:]):
                Fun = 'Putative'
            elif 'gene_biotype=pseudogene' in ''.join(Line[8:]) or 'pseudo=true' in ''.join(Line[8:]):
                Fun = 'Pseudo'
                Gene = 'Pseudo'
            else:
                Fun = 'Functional'
            GeneName = ''.join(Line[8:]).split("product=")[1].split(";")[0]
            Gene_table.append([Line[0], GeneName, 'rRNA', Fun, Line[3], Line[4], Line[6]])
        elif (Line[2] == "tRNA"):
            if 'Note=putative pseudogene' in ''.join(Line[8:]):
                Fun = 'Putative'
            elif 'gene_biotype=pseudogene' in ''.join(Line[8:]) or 'pseudo=true' in ''.join(Line[8:]):
                Fun = 'Pseudo'
                Gene = 'Pseudo'
            else:
                Fun = 'Functional'
            GeneName = ''.join(Line[8:]).split("product=")[1].split(";")[0]
            Gene_table.append([Line[0], GeneName, 'tRNA', Fun, Line[3], Line[4], Line[6]])
        elif (Line[2] == "tmRNA") or (Line[2] == "ncRNA") or (Line[2] == "RNase_P_RNA"):
            if 'Note=putative pseudogene' in ''.join(Line[8:]):
                Fun = 'Putative'
            elif 'gene_biotype=pseudogene' in ''.join(Line[8:]) or 'pseudo=true' in ''.join(Line[8:]):
                Fun = 'Pseudo'
                Gene = 'Pseudo'
            else:
                Fun = 'Functional'
            GeneName = ''.join(Line[8:]).split("product=")[1].split(";")[0]
            Gene_table.append([Line[0], GeneName, 'Other', Fun, Line[3], Line[4], Line[6]])


## Write table to CSV-formatted text output.
for entry in Gene_table:
    for item in entry:
        print(item, ",", sep='', end='')
    print('\n', end='')
