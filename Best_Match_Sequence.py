from difflib import SequenceMatcher

prime_sequence = 'gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg'

genes = ['tcctcca', 'aagaatggg', 'tgagtgg', 'acgcaagatc']

cutoff_point = 0.5

match_list = []
def match_making(prime_sequence, genes, cutoff_point, match_list):
    for i in range(len(genes)):
        for x in range(len(prime_sequence)):
            prime_slice = prime_sequence[x:(len(genes[i])+x)]
            sim = SequenceMatcher(None, prime_slice, genes[i]).ratio()
            if sim >= cutoff_point:
                match_list.append([round(sim, 3), x, genes[i]])


    match_list.sort(reverse = True)

    for match in match_list:
        print(match)

match_making(prime_sequence, genes, cutoff_point, match_list)
