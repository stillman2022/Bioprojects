import re
#agcacaggcaaatcagcctctcctgaactgaaagaactagtcagcagttgtacgccaccaggaacgccacgcacgtggaatggggcttgttcaactctat

#Sequence fragments to be joined together. Can have fragments that do not belong. The first sequence is the foundation of building the whole sequence.
seq_frag = ['gaaagaactagtcagcagttgta', 'agcacaggcaaatcagcctctc', 'cctctcctgaactgaaagaac', 'gttgtacgccaccaggaacgccac', 'aacgccacgcacgtggaatgggg', 'gaatggggcttgttcaactctat']

#Place holder for possible sequence that connect to the first sequence.
match_seq = ['xxx', 'xxx']

#How many base pairs the program will take out of the left side of the first sequence.
x = 4

#The list that can overlap with first sequence.
match_pos = seq_frag[1:]

#Loop to build sequence from the left until there are no more matches on the left side.
while len(match_seq) != 0:

    #Place holder to make sure search while loop activates.
    match_seq = ['xxx', 'xxx']

    #Loop to search for best match for left side.
    while len(match_seq) > 1:
        #Expand search length to narrow down matches.
        x += 1
        #Assign left side of the first sequence to try to find sequence that over laps.
        first_seg = seq_frag[0][:x]
        #Clear match_seq list, so only actual matches are stored.
        match_seq = []
        #Look through the fragments that can overlap with the first sequence one by one.
        for frag in match_pos:
            #See if frag has first_seq in it. Assign the regenx values.
            match_check = re.search(first_seg, frag)
            #Continue if there is a match.
            if match_check != None:
                #Determine if the overlap occurs from the match location to the edge of the fragment.
                if frag[match_check.start():] == seq_frag[0][:len(frag[match_check.start():])]:
                    #Add overlaping sequence to match_seq.
                    match_seq.append(frag)
        #Assign match_pos to match_seq, shortneing next search loop to just the fragments that matched last loop.
        match_pos = match_seq

    #If the best match is found.
    if len(match_seq) == 1 and match_seq != None:
        #Get Match values again.
        match_check = re.search(first_seg, match_seq[0])
        #Join best match and first sequence to replace current first sequence.
        seq_frag[0] = match_seq[0][:match_check.start()]+seq_frag[0]
        #Remove the best matching sequence from the list.
        seq_frag.remove(match_seq[0])
    else:
        print("Depleted matches")


    #Reset number of base pairs to on the left side of the new first sequence.
    x = 4
    #Establish new group to look for overlaps.
    match_pos = seq_frag[1:]
#See progress.
print(seq_frag)


#The same of the first secetion, but searchs from the right side of the first sequence.
match_seq = ['xxx', 'xxx']

x = -4

match_pos = seq_frag[1:]

while len(match_seq) != 0:

    match_seq = ['xxx', 'xxx']

    while len(match_seq) > 1:
        x -= 1
        first_seg = seq_frag[0][x:]
        match_seq = []
        for frag in match_pos:
            match_check = re.search(first_seg, frag)
            if match_check != None:
                if frag[:match_check.end()] == seq_frag[0][-(match_check.end()):] :
                    match_seq.append(frag)
        match_pos = match_seq


    if len(match_seq) == 1 and match_seq != None:
        match_check = re.search(first_seg, match_seq[0])
        seq_frag[0] = seq_frag[0] + match_seq[0][match_check.end():]
        seq_frag.remove(match_seq[0])
    else:
        print("Depleted matches")



    x = -4

    match_pos = seq_frag[1:]

print(seq_frag)
