import sys
sys.setrecursionlimit(10**7)
mo=10**9+7
n=10**5

fct=[0]*n
invfct=[0]*n
fct[0]=1
invfct[0]=1

def bi_pow(x,y):
    if y==1:
        return x%mo
    if y%2==0:
        return bi_pow(x,y//2)**2%mo
    else:
        return x*(bi_pow(x,y//2)**2)%mo

def fact(n):
    rt=fct[n]
    if rt!=0:
        return rt
    return n*fact(n-1)%mo

def invfact(n):
    invfct[n]=bi_pow(fact(n),mo-2)
    return invfct[n]

def fill_invfact(n):
    invfct[n]=invfact(n)
    for i in range(1,n):
        invfct[n-i]=invfct[n-i+1]*(n-i-1)%mo

def comb(x,y):
    if y<0 or y>x:
        return 0
    else:
        return fact(x)*invfact(x-y)*invfact(y)%mo
