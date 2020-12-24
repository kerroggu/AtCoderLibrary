########################################################################################################################################################################
# Verified by
# https://yukicoder.me/problems/no/979
# https://atcoder.jp/contests/abc152/tasks/abc152_e

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
## around 800 ms for N = 10**6  by PyPy3 (7.3.0) @ AtCoder
def PrimeNumSet(N):
    M=int(N**0.5)
    seachList=[i for i in range(2,N+1)]
    primes=[]
    while seachList:
        if seachList[0]>M:
            break
        primes.append(seachList[0])
        tmp=seachList[0]
        seachList=[i for i in seachList if i%tmp!=0]
    return primes+seachList


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

## return (a,b) s.t. a*x+b*y=gcd(x,y)
def extgcd(x,y):
    if y==0:
        return 1,0
    r0,r1,s0,s1 = x,y,1,0
    while r1!= 0:
        r0,r1,s0,s1=r1,r0%r1,s1,s0-r0//r1*s1
    return s0,(r0-s0*x)//y
