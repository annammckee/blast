## CONVERTING WEEK4 BASH CODE TO PYTHON
#!/usr/bin/env python3

import sys

#rename command line inputs to something meaningful
fin_blast = open(sys.argv[1])
fin_bed = open(sys.argv[2])



# create an empty list for where to put high quality matches
# iterate over each line and sepearte the columns by removing the newline char at the end and delimiting by tab
blast_list = []
for line in fin_blast.readlines():# .readlines() is a method of our open file object
    columns = line.strip().split("\t") # strip away trailing newlines, then split the str
    if float(columns[2]) > 30 and float(columns[3]) >= (0.9*float(columns[12])): # set the criteria for results that you want to keep (>30% match, covering >90 of the query length)
        blast_id = columns[1] #2nd column is the blast sequence ID
        blast_left = int(columns[8]) # retain the subject start and end postitions and convert to int
        blast_right = int(columns[9])
        blast_list.append([blast_id, blast_left, blast_right])


# create an empty list to populate with bed file information
bed_list = []
for line in fin_bed.readlines(): # .readlines() is a method of our open file object
     columns = line.strip().split("\t") # strip away trailing newlines, then split the str
     bed_id = columns[0] # bed seq ID column
     bed_left = int(columns[1]) # retain the subject start and end postitions, covert to int
     bed_right = int(columns[2])
     gene = columns[3] # gene name
     bed_list.append([bed_id, bed_left, bed_right, gene])

fin_blast.close()
fin_bed.close()  

# create an empty gene list to populate with unique genes that contain the retained blast sequences
gene_list = []
for blast_seq in blast_list: # iterate over the blast_list
    for bed_seq in bed_list: # iterate over the bed_list
        if blast_seq[0] == bed_seq[0]: # only continue if were on the right contig
            if blast_seq[1] >= bed_seq[1] and blast_seq[1] <= bed_seq[2]:# only continue if the sequence is completely within the gene
                if blast_seq[2] >= bed_seq[1] and blast_seq[2] <= bed_seq[2]:
                    if bed_seq[3] not in gene_list: # only add unique gene names to the list
                        gene_list.append(bed_seq[3])

print(len(gene_list))

# convert gene_list to str in order to write to file
gene_str = ""
for gene in gene_list:
    gene_str += gene + "\n" # add the gene to the string, add a new line after each gene
outfile = open(sys.argv[3], 'w') # 'w' mode means we will write to the file
outfile.write(gene_str)
outfile.close()