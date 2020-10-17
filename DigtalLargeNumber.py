def DLN(a,b,c):
    bin = binary(b)
    arr = []
    for x in range(len(bin)):
        if bin[x] != 0:
            y = a**(2**(len(bin)-x-1))%c
            arr.append(y)
    r = modu(arr,c)
    return r

def modu(arr,c):
    x = arr[0]%c
    for i in range(1, len(arr)):
        x = x*arr[i] %c
    return x%c
def binary(x):
    bin = []
    while (x >= 1):
        bin.append(x % 2)
        x = x // 2
        binary(x)
    str = [i for i in bin]
    bin = str[::-1]
    return bin
def main():
    # a**b (mod n)
    print(DLN(667,937,2537)) #1808




main()