def vowelsAndConsonants (s):
    vowels = 0
    consonants = 0
    for i in s :
        if i.isalpha():
            if i.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    return vowels,consonants
def main():
    x = input("Input a string:")
    m = vowelsAndConsonants(x)
    print("The number of vowels are {} and the number of consonants are {}."
          .format(m[0], m[1]))

main()