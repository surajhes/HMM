import sys
import ast
import operator


class State(object):
    def __init__(self, currentState, prevState, probability):
        self.currentState = currentState
        self.prevState = prevState
        self.probability = probability

def containsNum(s):
    return any(i.isdigit() for i in s)

hmmmodel = open('hmmmodel.txt', 'r')
transitionProbability = {}
wordTagProbability = {}
tp = 'Transition Probability'
ep = 'Emission Probability'
previousState = ''
tempMap = {}
for line in hmmmodel:
    line = line.strip()
    if line == ep:
        break
    else:
        if line == tp:
            pass
        else:
            tokens = line.split('$$$$$', 1)
            previousState = tokens[0]
            tempMap = ast.literal_eval(tokens[1])
            transitionProbability[previousState] = tempMap
            tempMap = {}
for line in hmmmodel:
    line = line.strip()
    tokens = line.rsplit('$$$$$', 1)
    word = tokens[0]
    wordMap = ast.literal_eval(tokens[1])
    wordTagProbability[word] = wordMap
    wordMap = {}

hmmmodel.close()
hmmoutput = open('hmmoutput.txt','w')
tag = ''
output = {}
inputFile = open(sys.argv[1])
backPointer = {}
probability = {}

for line in inputFile:
    words = line.split()
    states = []
    startState = State('q0', None, 0.0)
    states.append(startState)
    previousState = startState
    tempState = previousState.currentState
    for word in words:
        word = word.lower()
        if wordTagProbability. has_key(word):
            wordTag = wordTagProbability[word]
            temp = {}
            for tags in wordTag.keys():
                value = wordTag[tags]
                value = float(value) + previousState.probability + float(transitionProbability[previousState.currentState][tags])
                temp[tags] = value
            tag = max(temp.iteritems(), key=operator.itemgetter(1))
            currentState = State(tag[0],previousState.currentState,tag[1])
            states.append(currentState)
            previousState = currentState
        else:
            if containsNum(word):
                zzProbability = transitionProbability[tempState]['ZZ']
                currentState = State('ZZ',previousState.currentState,zzProbability)
                states.append(currentState)
                previousState = currentState
            else:
                tempMap = transitionProbability[tempState]
                tag = max(tempMap.iteritems(), key=operator.itemgetter(1))
                prob = previousState.probability + float(tag[1])
                currentState = State(tag[0],tempState,prob)
                states.append(currentState)
                previousState = currentState
    index = 1
    output = {}
    for word in words:
        output[word] = states[index].currentState
        index += 1
    line = ''
    for word in words:
        line = line + word+'/'+output[word]+' '
    line = line.strip()
    hmmoutput.write(line)
    hmmoutput.write('\n')
hmmoutput.close()
