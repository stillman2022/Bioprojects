#Python 3.10
#Basic Trait Matcher.

#Class that determines which samples best match the target sample in traits.
class Match():

        # A list of all the samples.
        self.cohort = cohort
        # Sorting the list to be more manageable later.
        self.cohort.sort(key=len)
        # Index of which sample to select from the cohort.
        self.index = index
        # The Target sample.
        self.target = cohort[index]
        # Samples that have more traits than the target.
        self.longer = [long for long in self.cohort if len(long) > len(self.target)]
        # Samples that have the same number of traits as the target.
        self.equal = [equal for equal in self.cohort if len(equal) == len(self.target) and equal != self.target]
        # Samples that have less traits than the target.
        self.lesser = [less for less in self.cohort if len(less) < len(self.target)]
        # Place-holders to make functions work
        self.perfect_long = 100000000000
        self.perfect_lesser = 0
        self.long_match = [0, []]
        self.equal_match = [0, []]
        self.less_match = [0, []]

    # Function that finds the best matches that have more traits than the target.
    def __long_matches__(self):
        #Loop to test on the longer samples.
        for long in self.longer:
            #Determining the similarities between the target and sample.
            matches = list(set(long) & set(self.target))
            #Calcualting the rate at which the sample contains matching traits to the target.
            match_rate = len(matches)/len(long)
            #Calcualting the rate if the sample had all the traits of the target.
            perfect_match = len(self.target)/len(long)
            #If the sample matches with the target perfectly note the length.
            if match_rate == perfect_match and self.perfect_long == 100000000000:
                self.perfect_long = len(long)
            #The best match at the closest trait number has been found, so do not advance beyond this trait length.
            if len(long) > self.perfect_long:
                break
            #If the rate of the current sample matches the rate of the previous best match, add to list.
            if self.long_match[0] == match_rate:
                self.long_match.append(long)
            #If the rate of the current sample is higher, restart best match list with new sample.
            if self.long_match[0] < match_rate:
                self.long_match.clear()
                self.long_match.append(match_rate)
                self.long_match.append(long)

            else:
                pass
        #Returing best matches.
        return self.long_match

    # Function that finds the best matches that have same number of traits than the target.
    def __equal_matches__(self):
        #Loop to test on the equal samples.
        for equal in self.equal:
            # Determining the similarities between the target and sample.
            matches = list(set(equal) & set(self.target))
            # Calcualting the rate at which the sample contains matching traits to the target.
            match_rate = len(matches)/len(equal)
            # Calcualting the rate if the sample had all the traits of the target.
            perfect_match = len(self.target)/len(equal)
            # If the rate of the current sample matches the rate of the previous best match, add to list.
            if self.equal_match[0] == match_rate:
                self.equal_match.append(equal)
            #If the rate of the current sample is higher, restart best match list with new sample.
            if self.equal_match[0] < match_rate:
                self.equal_match.clear()
                self.equal_match.append(match_rate)
                self.equal_match.append(equal)

            else:
                pass
        # Returing best matches.
        return self.equal_match

    # Function that finds the best matches that have less traits than the target.
    def __less_matches__(self):
        #Loop to test on the lesser samples.
        for less in self.lesser:
            # Determining the similarities between the target and sample.
            matches = list(set(less) & set(self.target))
            # Calcualting the rate at which the sample contains matching traits to the target.
            match_rate = len(matches)/len(less)
            # Calcualting the rate if the sample had all the traits of the target.
            perfect_match = len(self.target)/len(less)
            # If the sample matches with the target perfectly note the length.
            if match_rate == perfect_match and self.perfect_lesser == 0:
                self.perfect_lesser = len(less)
            # The best match at the closest trait number has been found, so do not advance beyond this trait length.
            if len(less) < self.perfect_lesser:
                break
            # If the rate of the current sample matches the rate of the previous best match, add to list.
            if self.less_match[0] == match_rate:
                self.long_match.append(less)
            #If the rate of the current sample is higher, restart best match list with new sample.
            if self.less_match[0] < match_rate:
                self.less_match.clear()
                self.less_match.append(match_rate)
                self.less_match.append(less)

            else:
                pass
        # Returing best matches.
        return self.less_match


cohort = [['a', 'b', 'c', 'd'], ['a', 'c'], ['a'], ['a', 'b', 'c'], ['a', 'b'], ['a', 'c', 'd'], ['a', 'b', 'c', 'e']]


#Print one target.

test = Match(cohort = cohort, index = 1)

print(f"Best match for sample(s) with more traits: {test.__long_matches__()}")

print(f"Best match for sample(s) with equal traits: {test.__equal_matches__()}")

print(f"The target sample: {test.target}")

print(f"Best match for sample(s) with less traits: {test.__less_matches__()}")


# Find best matches for all samples in cohort.
"""for index in range(len(cohort)):
    test = Match(cohort=cohort, index=index)
    print(f"Best match for sample(s) with more traits: {test.__long_matches__()}")
    print(f"Best match for sample(s) with equal traits: {test.__equal_matches__()}")
    print(f"The target sample: {test.target}")
    print(f"Best match for sample(s) with less traits: {test.__less_matches__()}")"""