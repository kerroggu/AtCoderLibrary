## verified by DISCO2020-E
## https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_e

def solve(n,mode='Sub'):
    if mode!='Sub': # set a test case in the following block
        s='BRRRBB'
        n=len(s)//2

    def judge(x):
        if len(x)!=n:
            return 'Error'
        b=[s[i] for i in x]
        an=['Red','Blue'][b.count('B')>b.count('R')]
        return an
    
    c=[0]
    def query(x):
        c[0]+=1
        if c[0]>210 or len(set(x))!=n or min(x)<0 or max(x)>=2*n: ## query condition check
            0/0

        print('?',*[i+1 for i in x])
        sys.stdout.flush()
        
        if mode=='Sub': # for Submission
            y=input()
        else: # for Test
            y=judge(x)
        return y[0]

## verified by ABC269-E
## https://atcoder.jp/contests/abc269/tasks/abc269_e    
    def solve(n,mode='Sub'):
    if mode!='Sub': # set a test case in the following block
        R=5
        C=2
        
    def judge(a,b,c,d):
        if (c,d)==(1,n):
            rt=b-a+1 - (a<=R<=b)
        else:
            rt=d-c+1 - (c<=C<=d)
        return rt
 
    def query(a,b,c,d):
        x=[a,b,c,d]
        print('?',*[a,b,c,d],flush=True)
        sys.stdout.flush()
        
        if mode=='Sub': # for Submission
            y=I()
        else: # for Test
            y=judge(*x)
        return y
    
    D=10
    l,r=1,n
    for i in range(D):
        m=l+r>>1
        y=query(l,m,1,n)
        if m-l+1!=y:
            r=m
        else:
            l=m+1
    ans=[l]
    
    return ans

n=I()
ans=solve(n)
print('!',*ans,flush=True)
