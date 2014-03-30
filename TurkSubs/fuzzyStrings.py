import difflib
from collections import Counter

first = "The quick brown fox, jumped over the fence!!"
firstCAP = "THE QUICK BROWN FOX, JUMPED OVER THE FENCE!!"
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

def column(matrix, index):
    return [row[index] for row in matrix]

def printMatrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

def ratioMatrix(oldStrings):
    strings = normalizeStrings(oldStrings)
    matrix = []
    for firstSentence in strings:
        tempList = []
        for secondSentence in strings:
            tempS = difflib.SequenceMatcher(None, firstSentence, secondSentence)
            tempList.append(tempS.ratio())
        matrix.append(tempList)
    
    return matrix

def scoreStrings(strings):
    matrix = ratioMatrix(strings)
    
    totalScores = []
    for row in matrix:
        rowScores = []
        sumRow = sum(row) - 1.0
        prodRow = reduce(lambda x, y: x*y, row, 1)
        
        if len(row) > 1:
            AvgRow = sumRow / (len(row) - 1)
        else:
            AvgRow = sumRow
            
        rowScores.append(sumRow)
        rowScores.append(prodRow)
        rowScores.append(AvgRow)
        totalScores.append(rowScores)
        
    return totalScores

def pickBestScores(strings):
    
    matrix = scoreStrings(strings)
    
    bestScores = []
    
    maxSum = max((element[0]) for element in matrix)
    maxProd = max((element[1]) for element in matrix)
    maxAvg = max((element[2]) for element in matrix)
    
    bestScores.append(maxSum)
    bestScores.append(maxProd)
    bestScores.append(maxAvg)
    
    return bestScores

def pickBestIndexes(strings):
    scores = pickBestScores(strings)
    matrix = scoreStrings(strings)
    
    indexes = []
    
    indexes.append(column(matrix,0).index(scores[0]))
    indexes.append(column(matrix,1).index(scores[1]))
    indexes.append(column(matrix,2).index(scores[2]))
    
    return indexes

def pickBestIndex(strings):
    indexes = pickBestIndexes(strings)
    data = Counter(indexes)    
    mode = data.most_common(1)
    return mode[0][0]

def pickBestString(strings):
    return strings[pickBestIndex(strings)]