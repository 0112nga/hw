def convertPigLatin(s):
    m = s.split(' ')
    str = ''
    for val in m:
        str += val[1:len(val)].upper() + val[0].upper()+'AY '
    return str
def main():
    x = input("Input s a sentence (Eg: I SLEPT MOST OF THE NIGHT ): ")
    print('Pig Latin: '+ convertPigLatin(x))
main()

