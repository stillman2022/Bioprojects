import copy

prime_sequence = "gatcctccat atacaacggt atctccacct caggtttaga tctcaacaac ggaaccattg"

complementry_sequence = copy.copy(prime_sequence)

complementry_sequence = list(complementry_sequence)

for i in range(len(complementry_sequence)):
    if complementry_sequence[i] == 'a':
        complementry_sequence[i] = 't'
    elif complementry_sequence[i] == 't':
        complementry_sequence[i] = 'a'
    elif complementry_sequence[i] == 'g':
        complementry_sequence[i] = 'c'
    elif complementry_sequence[i] == 'c':
        complementry_sequence[i] = 'g'
    else:
        pass

complementry_sequence = ''.join(complementry_sequence)