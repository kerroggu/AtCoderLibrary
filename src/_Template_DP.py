# keta DP ------------------------------------------------------------------

d=I()
s=input()
n=len(s)

dp=[[[0]*(n+1) for j in range(d)] for i in range(2)]
#dp[f][j][i] = (f;=flag if n>x, # of x; s.t. x%d=j, saw up to i
dp[0][0][0]=1

for i in range(n):
    c=int(s[i])
    for j in range(d):
        for x in range(10):
            dp[1][(j+x)%d][i+1]+=dp[1][j][i]
            if x<c:
                dp[1][(j+x)%d][i+1]+=dp[0][j][i]
            if x==c:
                dp[0][(j+x)%d][i+1]+=dp[0][j][i]
            dp[1][(j+x)%d][i+1]%=mo


# DP     ------------------------------------------------------------------

# Bit subgroup DP     ------------------------------------------------------------------
# https://atcoder.jp/contests/abc187/tasks/abc187_f
n,m=LI()
g,_=GI(n,m)
chk=[None]*(1<<n)

def is_cg(x):
    if chk[x]!=None:return chk[x]
    s=[j for j in range(n) if (x>>j)&1]
    N=len(s)
    for i in range(N):
        for j in range(i+1,N):
            if (s[i],1)not in g[s[j]] or (s[j],1)not in g[s[i]]:
                return False
    chk[x]=True
    return True

N=1<<n
dp=[n]*N

for i in range(N):
    if is_cg(i):dp[i]=1
    j=i
    while j>0:
        dp[i]=min(dp[i],dp[j]+dp[i^j])  # split group i to subset i and i/j
        j-=1
        j&=i

print(dp[-1])
