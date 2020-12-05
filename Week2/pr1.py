
def getInitial(fullName):
    name = fullName.split(' ')
    for val in name:
        print(val[0].upper()+'. ', end='')

def main():
    x = input("Input your full name:")
    print("Result: ", end='')
    getInitial(x)

main()