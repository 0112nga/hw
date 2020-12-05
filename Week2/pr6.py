def countFre(str):
    count = {}
    for i in str:
        count[i] = [x for x in range(len(str)) if str[x] == i]
    numOfFreq = [len(i) for i in count.values()]
    maxFreq = max(numOfFreq)
    charFreq = []
    for index, val in enumerate(numOfFreq):
        if val == maxFreq:
            charFreq.append(list(count.keys())[index])
    return charFreq

def main():
    x = input("Enter a string: ")
    print('the character that appears most frequently in the string: ',end='')
    for i in countFre(x):
        print(i + ' ', end='')

main()