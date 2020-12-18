def main():
    # learningFile = input('Learning data file name: ')
    learningFile = 'test.TXT'
    print('What would you like to do?'
          '\n1: Get the score of a word'
          '\n2: Get the average score of words in a file'
          '\n3: Find the highest / lowest scoring words in a file'
          '\n4: Sort the words in a file into positive.txt and negative.txt'
          '\n5: Exit the program')
    i = int(input('Enter a number 1 - 5: '))
    print(inputUser(i))

def inputUser(x):
    switcher = {
            1:  getScoreOfWord,
            2: getAverageScore,
            3: getHighestOrLowestScore(),
            4: 'Wednesday',
            5: 'Exit'
        }
    return switcher.get(x, "nothing")

main()

def getData(learningFile):
    file = open(learningFile)
    dictData = {}
    dataCount ={}
    lines = file.readlines()
    words = []
    for line in lines:
        w = line.strip().split(' ')
        words.append(w)
    for word in words:
        for index, w in enumerate(word):
            charList = [i for i in w]
            newWord = ''
            for input_char in w:
                if(charCheck(input_char) == 0):
                    charList.remove(input_char)
            for i in charList:
                newWord += i
            word[index] = newWord
    for word in words:
        word.remove(word[0])
    allword = []
    for index in range(len(words)):
        allword += words[index]
    setWord = set(allword)
    for w in setWord:
        dataCount[w.lower()] = 0
        dictData[w.lower()] = []
    for key in dataCount:
        for w in allword:
            if key == w.lower():
                dataCount[key] += 1
    rating = []
    for line in lines:
        rating.append(int(line[0]))
    for key in dictData:
        for index,word in enumerate(words):
            # if key in word:
            #     dictData[key].append(index)
            for i in word:
                if i.lower() == key:
                    dictData[key].append(rating[index])
    for key in dictData:
        dictData[key] = sum(dictData[key])/len(dictData[key])
    # print(len(words))
    print(dictData)
    print(dataCount)
    file.close()
    return dictData, dataCount
def charCheck(input_char):
    if ((int(ord(input_char)) >= 65 and
         int(ord(input_char)) <= 90) or
            (int(ord(input_char)) >= 97 and
             int(ord(input_char)) <= 122)):
        return 1

        # CHECKING FOR DIGITS
    elif (int(ord(input_char)) >= 48 and
          int(ord(input_char)) <= 57):
        return 1

        # OTHERWISE SPECIAL CHARACTER
    else:
        return 0
def getScoreOfWord(word):
    dictData = getData('test.TXT')[0]
    # dataCount = getData('test.TXT')[1]
    score = 0
    message = ''
    for w in dictData:
        if word.lower() == w:
            score = dictData[word]
            message = 'score = ' + str(score)
            if score > 2.01 :
                message += '\n'+word + ' is '+ 'positive'
            elif score < 1.99:
                message += '\n' + word + ' is ' + 'positive'
            else:
                message += '\n' + word + ' is ' + 'neutal'
            return message
    return None
# print(getScoreOfWord('best'))
def getAverageScore(filename):
    file = open(filename)
    line = file.readline()
    words = line.strip().split(' ')
    # for word in words:
    for index, w in enumerate(words):
        charList = [i for i in w]
        newWord = ''
        for input_char in w:
            if (charCheck(input_char) == 0):
                charList.remove(input_char)
        for i in charList:
            newWord += i
        words[index] = newWord
    score = 0
    for word in words:
        score += getScoreOfWord(word)
    averageScore = score/len(words)

    message = 'score = ' + str(score)
    if averageScore > 2.01:
        message += '\n' + word + ' is ' + 'positive'
    elif averageScore < 1.99:
        message += '\n' + word + ' is ' + 'positive'
    else:
        message += '\n' + word + ' is ' + 'neutal'
    file.close()
    return message
def getHighestOrLowestScore(filename):
    file = open(filename)
    line = file.readline()
    words = line.strip().split(' ')
    # for word in words:
    for index, w in enumerate(words):
        charList = [i for i in w]
        newWord = ''
        for input_char in w:
            if (charCheck(input_char) == 0):
                charList.remove(input_char)
        for i in charList:
            newWord += i
        words[index] = newWord
    maxScore = 0
    maxWord = ''
    minScore = 0
    minWord = ''
    for word in words:
        if maxScore <= getScoreOfWord(word):
            maxScore = getScoreOfWord(word)
            maxWord = word
        if minScore >= getScoreOfWord(word):
            minScore = getScoreOfWord(word)
            minWord = word
    message = 'Maximum score is ' + maxScore + ' for'+ maxWord + '\n'+ 'Minimum score is ' + minScore+' for'+ minScore
    file.close()
    return message

# getAverageScore('cat.TXT')
