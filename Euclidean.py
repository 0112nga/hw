
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
    print('step 1. p0 = 0')
    p.append(1)
    print('step 2. p1 = 1')
    for x in range(2,len(q)+1):
        print('step {}. p{}= '.format(x,x), end ='')
        y = p[x-2] -p[x-1]*q[x-2]
        # print(p[x-2], end = '')
        print('{} - {}.({}) mod {} = '.format(p[x-2],p[x-1],q[x-2],n), end = '')
        while(y<0):
            y = y + n
        print(y)
        p.append(y)
    return p[len(q)]
def findx0 (r,a,b,n,gcd):
    x0 = r * b / gcd % (n/gcd)
    return int(x0)
def main():
    x = gcd(43,6,341)
    r = extendEculidean(341,x[0])
    print('result = ', end= '')
    print(findx0(r,43,6,341,x[1]))


main()