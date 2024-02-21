########################################################################################################################################################################
# Verified by
# https://yukicoder.me/problems/no/979
# https://atcoder.jp/contests/abc152/tasks/abc152_e

## return prime factors of N as dictionary {prime p:power of p}
## within 2 sec for N = 2*10**20+7
def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1: continue
        while y != n - 1:
            y = y * y % n
            if y == 1 or t == n - 1: return 0
            t <<= 1
    return 1
    
def findFactorRho(n):
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g): return g
            elif isPrimeMR(n // g): return n // g
            return findFactorRho(g)
            
def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k: ret[i] = k
        i += i % 2 + (3 if i % 3 == 1 else 1)
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k
    
    if n > 1: ret[n] = 1
    if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
    return ret

## return divisors of n as list
def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p]+1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)

## return the array s such that s[q] = the minimum prime factor of q
def sieve(x):
    s=[i for i in range(x+1)]
    p=2
    while p*p<=x:
        if s[p]==p:
            for q in range(2*p,x+1,p):
                if s[q]==q:
                    s[q]=p
        p+=1
    return s

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

## return (a,b,gcd(x,y)) s.t. a*x+b*y=gcd(x,y)
def extgcd(x,y):
    if y==0:
        return 1,0,x
    r0,r1,s0,s1 = x,y,1,0
    while r1!= 0:
        r0,r1,s0,s1=r1,r0%r1,s1,s0-r0//r1*s1
    return s0,(r0-s0*x)//y,x*s0+y*(r0-s0*x)//y


## return x,LCM(mods) s.t. x = rem_i (mod_i), x = -1 if such x doesn't exist
## verified by ABC193E
## https://atcoder.jp/contests/abc193/tasks/abc193_e
def crt(rems,mods):
    n=len(rems)
    if n!=len(mods):
        return NotImplemented
    x,d=0,1
    
    for r,m in zip(rems,mods):
        a,b,g=extgcd(d,m)
        x,d=(m*b*x+d*a*r)//g,d*(m//g)
        x%=d

    for r,m in zip(rems,mods):
        if r!=x%m:
            return -1,d

    return x,d

## returns the maximum integer rt s.t. rt*rt<=x
## verified by ABC191D
## https://atcoder.jp/contests/abc191/tasks/abc191_d
def intsqrt(x):
    if x<0:
        return NotImplemented
    rt=int(x**0.5)-1
    while (rt+1)**2<=x:
        rt+=1
    return rt
