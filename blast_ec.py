## CONVERTING WEEK4 BASH CODE TO PYTHON
#!/usr/bin/env python3

import sys

#rename command line inputs to something meaningful


fin_blast = open(sys.argv[1])
fin_bed = open(sys.argv[2])
outfile = sys.argv[3]

# create an empty list for where to put high quality matches
# iterate over each line and sepearte the columns by removing the newline char at the end and delimiting by tab
# set the criteria for results that you want to keep (>30% match, covering >90 of the query length)
# retain the subject start and end postitions
blast_keep = []
for line in fin_blast.readlines():
    results = line.strip().split("\t")
    if float(results[2]) > 30 and int(results[3]) > (0.9*int(results[12])):
        blast_keep.append((results[8], results[9]))



print(blast_keep)


bed_file = fin_bed.readlines()

#tblastn with selection criteria
#save the 9th column (subjust start location in the blast) of the output to the blast_out temp file



# | awk '$3>30 && $4>0.9*$13' | cut -f9 > $blast_out


# #need to use paste to extract the columns I want and put them into tabular format for use in loop
# paste   <(cut -f2 $bed_file) \
#         <(cut -f3 $bed_file) \
#         <(cut -f4 $bed_file) > $protein


# #iterates over each line in the blast_out file, which contains the start position of the HK domain
# #iterates over each line in the protein file, which contains the left position, right position, and gene names from the bed file
# #checks if the start position of the domain is wihtin the bounds of the genes from the bed file
# #if so, save the gene name to a list and append the list for each match
# while read domain_start
# do
#     while read protein_left protein_right protein_gene
#     do        
#         if [[ $domain_start -gt $protein_left && $domain_start -lt $protein_right ]]
#         then
#             echo $protein_gene >> $gene_list
#         fi
#     done < $protein
# done < $blast_out

# #sorts the gene_list containing HK domains and only keeps unique values
# sort $gene_list | uniq > $outfile

# #clears the values of all temp files
# rm $gene_list
# rm $blast_out
# rm $protein