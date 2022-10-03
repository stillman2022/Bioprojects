#Python 3.10
#GDC Data Portal TSV Mutation Export Current View.
#Takes GDC Data Portal TSV Mutation Export Current View and formats the mutations with Case ID in csv file.

#Example text:
"""DNA Change	Type	Consequences	# Affected Cases in Cohort	# Affected Cases Across the GDC	Impact	Survival
chr9:g.14125722delAC	Deletion	Frameshift NFIB L323Ffs*84	1 / 1,100.00%	1 / 13,582	VEP: HIGH	add to survival plot
chr16:g.50781271A>T	Substitution	Missense CYLD D515V	1 / 1,100.00%	1 / 13,582	VEP: MODERATE, SIFT: deleterious - score 0, PolyPhen: probably_damaging - score 0.999	add to survival plot"""

#Importing the need modules.
import os, re, csv

#Place holders for later.
csv_list = []
mutation_dict = {}
#Header for csv file.
header = ['Case ID', 'Mutations']
#The regex pattern to be used to extract mutation from text.
mutation_pattern = r"chr\d+:g.\S+"
#Input location of tsv files to be summerized.
file_location = input("Enter location of tsv files.")

#Opens all the files in the designated file location.
for tsv_file in os.listdir(file_location):
    with open(os.path.join(file_location,tsv_file), 'r') as mutation_file:
        #Assign files text.
        mutation_text = mutation_file.read()
        #Finding mutations in text and assigning to list.
        mutations_list = re.findall(mutation_pattern, mutation_text)
        #Assigning filename as key and mutation list as value.
        mutation_dict[tsv_file[:-4]] = mutations_list

#Turning keys and values in mutation_dict into something csv writer can use.
for k, v in mutation_dict.items():
    csv_list.append([k, v])

#Begin writing csv file.
with open(os.path.join(file_location, "mutation_sum.csv"), 'w', encoding ='UTF8') as mutation_sum:
    #Creating cvs writer.
    writer = csv.writer(mutation_sum, lineterminator = '\n')
    #Writing header to csv.
    writer.writerow(header)
    #Writing the data to the csv
    for rows in csv_list:
        writer.writerow(rows)

