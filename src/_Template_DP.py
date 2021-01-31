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


# Bit subgroup DP     ------------------------------------------------------------------
# https://atcoder.jp/contests/abc190/tasks/abc190_e
# 
n,m=LI()
g,_=GI(n,m)
chk=[None]*(1<<n)

def is_cg(x):
    if chk[x]!=None:return chk[x]
    s=[j for j in range(n) if (x>>j)&1]
    N=len(s)
    for i in range(N):

# TSP by Bit DP     ------------------------------------------------------------------
# https://atcoder.jp/contests/abc187/tasks/abc187_f
# https://atcoder.jp/contests/past202005-open/tasks/past202005_m

# k := 頂点数
# d[u][v] := u-v間の距離
# dp[i][S] := bit集合Sの頂点を訪れて頂点iに辿り着く場合の最小距離 (出発点が決まっている場合の初期化はdp[st][1<<st]=0)

N=1<<k
dp=[[inf]*N for i in range(k)]
for i in range(k):
    dp[i][1<<i]=0

for i in range(N):
    for u in range(k):
        for v in range(k):
            if (i>>u)&1&(i>>v)==0: # u,vがbit集合に含まれないケースは除外
                continue
            if d[u][v]!=None: # u->vの経路が使える場合、最短距離を更新
                dp[v][i]=min(dp[v][i],dp[u][i^(1<<v)]+d[u][v])

ans=min([dp[i][-1] for i in range(k)])
