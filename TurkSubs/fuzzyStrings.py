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

def scoreStrings(matrix):
    totalScores = []
    for row in matrix:
        rowScores = []
        sumRow = sum(row) - 1.0
        prodRow = reduce(lambda x, y: x*y, row, 1)
        AvgRow = sumRow / (len(row) - 1)
        rowScores.append(sumRow)
        rowScores.append(prodRow)
        rowScores.append(AvgRow)
        totalScores.append(rowScores)
    return totalScores    

def pickBestScores(matrix):
    bestScores = []
    
    maxSum = max((element[0]) for element in matrix)
    maxProd = max((element[1]) for element in matrix)
    maxAvg = max((element[2]) for element in matrix)
    
    bestScores.append(maxSum)
    bestScores.append(maxProd)
    bestScores.append(maxAvg)
    
    return bestScores

def pickBestIndexes(matrix):
    scores = pickBestScores(matrix)
    

foo = ratioMatrix(strings)
printMatrix(foo)

print '----------------------------------------------------------------------------------------'

bar = scoreStrings(foo)
printMatrix(bar)

print '----------------------------------------------------------------------------------------'

print(pickBest(bar))