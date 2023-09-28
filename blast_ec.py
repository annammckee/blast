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
# retain the subject start and end postitions and removing orientation effect
# blast_keep = []
blast_dict = {}
for line in fin_blast.readlines(): # .readlines() is a method of our open file object
    results = line.strip().split("\t") # strip away trailing newlines, then split the str
    if float(results[2]) >= 30 and int(results[3]) >= (0.9*int(results[12])):
        blast_id = results[1]
        blast_right = min(results[8], results[9])
        blast_left = max(results[8], results[9])
        if blast_id in blast_dict: # does the key already exist
            blast_dict[blast_id].append([blast_right, blast_left]) # lookup the list associated with blast_id and append the left and right positions to that list
        else: # if not, add it with a list as the left/right position values
            blast_dict[blast_id] = ([blast_right, blast_left])



print(blast_dict)
        # blast_keep.append((results[1], blast_right, blast_left))
# print(blast_keep)

bed_file=[]
for line in fin_bed.readlines():
    columns = line.strip().split("\t")
    bed_file.append((columns[1], columns[2], columns[3]))


# bed_dict = {}
# for line in fin_bed.readlines(): 
#     weight, treatment = line.strip().split("\t") 
#     if treatment in treatment_weights_dict: # does the key already exist
#         treatment_weights_dict[treatment].append(weight) # lookup the list associated with treatment and append this weight to that list
#     else: # if not, add it with a list as the value
#         treatment_weights_dict[treatment] = [weight]

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