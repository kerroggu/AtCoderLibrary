# Verified by
# https://yukicoder.me/problems/no/979

## return prime factors of N as dictionary {prime p:power of p}
## within 2 sec for N = 2*10**20+7
def primeFactor(N):
    i,n=2,N
    ret={}
    d,sq=2,99
    while i<=sq:
        k=0
        while n%i==0:
            n,k,ret[i]=n//i,k+1,k+1
        if k>0 or i==97:
            sq=int(n**(1/2)+0.5)
        if i<4:
            i=i*2-1
        else:
            i,d=i+d,d^6
    if n>1:
        ret[n]=1
    return ret

## return divisors of n as list
def divisor(n):
    div=[1]
    for i,j in primeFactor(n).items():
        div=[(i**k)*d for d in div for k in range(j+1)]
    return div

## return the list of prime numbers in [2,N], using eratosthenes sieve
## within 2sec for N = 1.2*10**7
def PrimeNumSet(N):
    Max = int(N**0.5)
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList:
        if seachList[0] <= Max:
            break
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

## retrun LCM of numbers in list b
## within 2sec for no of B = 10*5  and  Bi < 10**6
def LCM(b,mo=10**9+7):
    prs=PrimeNumSet(max(b))
    M=dict(zip(prs,[0]*len(prs)))
    for i in b:
        dc=primeFactor(i)
        for j,k in dc.items():
            M[j]=max(M[j],k)
    
    r=1
    for j,k in M.items():
        if k!=0:
            r*=pow(j,k,mo)
            r%=mo
    return r
