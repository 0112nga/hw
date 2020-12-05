
def convert(message):
    m = ''
    for i in message:
        if i.isdigit():
            m += str(i)
        elif i.upper() in 'ABC':
            m += '2'
        elif i.upper() in 'DEF':
            m += '3'
        elif i.upper() in 'GHI':
            m += '4'
        elif i.upper() in 'JKL':
            m += '5'
        elif i.upper() in 'MNO':
            m += '6'
        elif i.upper() in 'PQRS':
            m += '7'
        elif i.upper() in 'TUV':
            m += '8'
        elif i.upper() in 'WXYZ':
            m += '9'
        elif i == '-':
            m += '-'
        else:
            return 'Invalid input'
    return m


def main():
    x = input("enter a 10-character telephone number in the format XXX-XXX-XXXX: ")
    print(convert(x))

main()