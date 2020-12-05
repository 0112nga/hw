def capitalize(sentence):
    m = sentence.split('. ')
    str =''
    for index,val in enumerate(m):
        if index == len(m)-1:
            str += val[0].upper() + val[1:len(val)]
            break
        str += val[0].upper() + val[1:len(val)] + '. '
    return str
def main():
    x = input("Input sentence (Eg: hello. my name is Joe. what is your name?): ")
    print('Result sentence capitalized: '+capitalize(x))


main()