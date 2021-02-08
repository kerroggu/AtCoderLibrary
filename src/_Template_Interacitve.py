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
