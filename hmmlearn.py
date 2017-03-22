import sys
import math
from collections import Counter

modelFile = open(sys.argv[1])
transitionKey = ''
transitionMatrix = {}
fileLines = []
wordTags = []
allTagsOfWords = {}
tags = []
tagsMapList = {}
for line in modelFile:
    fileLines.append(line)
for line in fileLines:
    previousState = "q0"
    splitWords = line.split()
    for word in splitWords:
        wordsWithoutTags = word.rsplit('/', 1)
        text = wordsWithoutTags[0]
        tag = wordsWithoutTags[1]
        tags.append(tag)
        tagsList = []
        transitionKey = transitionKey + previousState + '-' + tag
        text = text.lower()
        if tagsMapList.has_key(previousState):
            tagsList = tagsMapList.get(previousState)
            tagsList.append(tag)
        else:
            tagsList.append(tag)
            tagsMapList[previousState] = tagsList
        if transitionMatrix. has_key(transitionKey):
            count = transitionMatrix.get(transitionKey)
            count += 1
            transitionMatrix[transitionKey] = count
        else:
            transitionMatrix[transitionKey] = 1
        if allTagsOfWords. has_key(text):
            wordTags = allTagsOfWords[text]
            wordTags.append(tag)
        else:
            wordTags.append(tag)
            allTagsOfWords[text] = wordTags
        previousState = tag
        wordTags = []
        transitionKey = ''

finalTagProbability = {}
tagProbability = {}
tagsList = []
for key in transitionMatrix.keys():
    tempTags = key.split('-')
    value = transitionMatrix[key]
    if finalTagProbability.has_key(tempTags[0]):
        tagProbability = finalTagProbability[tempTags[0]]
        tagProbability[tempTags[1]] = value
        finalTagProbability[tempTags[0]] = tagProbability
    else:
        tagProbability[tempTags[1]] = value
        finalTagProbability[tempTags[0]] = tagProbability
    tagProbability = {}

tagsCount = Counter(tags)
wordTagProbability = {}
wordsProbabilities = {}
for key in allTagsOfWords.keys():
    tagList = allTagsOfWords[key]
    tagsCounterList = Counter(tagList)
    for wordTag in tagsCounterList.keys():
        totalTimesInTag = tagsCounterList[wordTag]
        probability = float(totalTimesInTag)/float(tagsCount[wordTag])
        wordTagProbability[wordTag] = math.log(probability)
        wordsProbabilities[key] = wordTagProbability
        wordTagProbability = {}
# tagsMapList
tagsCounter = []
tagsProbability = {}
individualTags = tagsMapList.keys()
# add 1 smoothing here.
for key in tagsMapList.keys():
    tagsCounter = tagsMapList.get(key)
    tagsCounter.extend(individualTags)
    tagsMapList[key] = tagsCounter

# add one smoothing ends
tagsCounter = []
for key in tagsMapList.keys():
    tagsCounter = tagsMapList.get(key)
    tagsCounterMap = Counter(tagsCounter)
    for tagKey in tagsCounterMap.keys():
        if tagsProbability.has_key(key):
            tempProbMap = tagsProbability[key]
        else:
            tempProbMap = {}
        probability = float(tagsCounterMap[tagKey])/float(len(tagsCounter))
        tempProbMap[tagKey] = math.log(probability)
        tagsProbability[key] = tempProbMap
# the transitions are in the form of current stage to next stage. CS-NS (current stage - next stage)

# write to hmmmodel.txt
hmmmodel = open("hmmmodel.txt", 'w')
hmmmodel.write("Transition Probability")
for key, value in tagsProbability.items():
    hmmmodel.write("\n")
    hmmmodel.write(key + "$$$$$" + str(value))

hmmmodel.write("\nEmission Probability")
for key, value in wordsProbabilities.items():
    hmmmodel.write("\n")
    hmmmodel.write(key + "$$$$$" + str(value))
modelFile.close()
hmmmodel.close()

