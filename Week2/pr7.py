def convert(s):
    str = ''
    for index, val in enumerate(s):
        if val.isalpha():
            if index != 0:
                if val == val.upper():
                    str += ' '+val.lower()
                else:
                    str += val
            else:
                str += val
        else:
            str += val
    return str
def main():
    x = input("Input a sentence in which all of the words are run together but "
              "the first character of each word is uppercase (Eg: StopAndSmellTheRoses.): ")
    print(convert(x))

main()