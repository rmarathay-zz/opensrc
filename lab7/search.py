import networkx as nx


def parseFile(textFile):
    inputFile = open(textFile)
    wordList = []
    for word in inputFile:
        if(word[-1] == '\n'):
            word = word[0:len(word)-2]
            wordList.append(word)
    wordList.pop(len(wordList)-1)
    return wordList

def createGraph(dataList):
    G = nx.Graph()
    word = ""
    for word in dataList:
        for w in word:





def addEdge():
    print "addEdge"
        # add a edge between words that have the same letters except 1
        # any order

def addNode():
    print "addNode"


if __name__ == '__main__':
    dataList = parseFile("words4.txt")
    print dataList
