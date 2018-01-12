def parseInput():
    filepath = 'day4input.txt'
    input = []
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line = line.strip('\n').split('\t')
            for word in line:
                input.append(word)
            line = fp.readline()
    return input

def getValidPhrases(phrases):
    count1 = 0
    count2 = 0
    length = len(phrases)
    for i in range(0, length):
        track = []
        words = phrases[i].split(' ')
        numWords = len(words)
        j = 0
        done = False
        valid = True
        valid2 = True
        while not done and j < numWords:
            if words[j] not in track:
                
                track.append(words[j])
            else:
                done = True
                valid = False
            j += 1
        if valid:
            count1 += 1
    return (count1, count2)



def main():
    words = parseInput()
    validPhrases = getValidPhrases(words)
    print validPhrases[0], validPhrases[1]
main()
