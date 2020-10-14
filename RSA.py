
def find(p,q,e, mess):
    n = p * q
    z = (p-1)*(q-1)
    x = gcd(e, 1, z)
    r = extendEculidean(z,x[0])
    d = findx0(r,17,1,60,x[1])
    bin = binary(d)
    x = 1
    m = []
    for y in mess:
        for i in range(len(bin)):
            if bin[i] != 0:
                x *= y**(2**(len(bin)-1-i))%n
        m.append(x%n)
        x = 1
    str = ''
    for i in m:
        str += chr(i)
    return str


def binary(x):
    bin = []
    while (x>=1):
        bin.append(x%2)
        x = x // 2
        binary(x)
    str = [i for i in bin]
    bin = str[::-1]
    return bin
def gcd(a,b,n):
    quotient = []
    while ( a != 0):
        c = n % a
        q = int(n / a)
        quotient.append(q)
        n = a
        a = c
    return quotient,n
def extendEculidean(n,q):
    p = []
    p.append(0)
    p.append(1)
    for x in range(2,len(q)+1):
        y = p[x-2] -p[x-1]*q[x-2]
        while(y<0):
            y = y + n
        p.append(y)
    return p[len(q)]
def findx0 (r,a,b,n,gcd):
    x0 = r * b / gcd % (n/gcd)
    return int(x0)
def main():
    p = int(input('Enter p: ')) #7
    q = int(input('Enter q: ')) #11
    e = int(input('Enter e: ')) #17
    message = input('Enter encryoted message: ')   #'37 39 29'
    mes = message.split(' ')
    intmes = [int(i) for i in mes]
    print('original message: ', end='')
    print(find(p,q,e,intmes))

main()