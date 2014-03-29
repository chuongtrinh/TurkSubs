import difflib

first = "The quick brown fox jumped over the fence"
firstCAP = "THE QUICK BROWN FOX JUMPED OVER THE FENCE"
second = "The quick brown bear jumped over the fence"
third = "The slow turtle trodded under the fence"
fourth = "The quick rabbit jumped over the gate"

strings = []

strings.append(first)
strings.append(firstCAP)
strings.append(second)
strings.append(third)
strings.append(fourth)

def stripPunctuation(string):
    output = ''
    exclude = ('!', ',', ':', '\'', '@')

    for char in string:
        if char not in exclude:
            output = output + char
    return output

def normalizeStrings(strings):
    newStrings = []
    for string in strings:
        string = string.lower()
        string = stripPunctuation(string)
        newStrings.append(string)
    return newStrings

def ratioMatrix(strings):
    matrix = []
    for firstSentence in strings:
        tempList = []
        for secondSentence in strings:
            tempS = difflib.SequenceMatcher(None, firstSentence, secondSentence)
            tempList.append(tempS.ratio())
        matrix.append(tempList)
    return matrix

def printMatrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)
