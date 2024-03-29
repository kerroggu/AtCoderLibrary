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
# https://atcoder.jp/contests/abc187/tasks/abc187_f
# jはiの表すBit集合の部分集合を渡る。i,jの表すBit集合をS,Uとすると、dp[S]をdp[S/U] & dp[U] で更新。O(3^n)

N=1<<n
dp=[1 if check(i) else n for i in range(N)] 
for i in range(N):
    j=i
    while j>0:        
        dp[i]=min(dp[i],dp[j]+dp[i^j])
        j-=1
        j&=i

        
# TSP by Bit DP     ------------------------------------------------------------------
# https://atcoder.jp/contests/abc190/tasks/abc190_e
# https://atcoder.jp/contests/past202005-open/tasks/past202005_m
#
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


## Traveling Salesman Problem with BitDP. O(k^2 * 2^k)
## verified by PAST-3 M
## https://atcoder.jp/contests/past202005-open/tasks/past202005_m

dp=[[inf]*(1<<k) for i in range(k)]
for i in range(k):
    dp[i][1<<i]=init_d[t[i]]

for i in range(1<<k):
    for fr in range(k):
        for to in range(k):
            if fr!=to and (i>>fr)&1 and (i>>to)&1:
                prev=i&~(1<<to) # now at "fr" and has visted bit(i) - "to"
                #show((fr,to),bin(i+(1<<k))[3:],(dp[fr][prev],dist[fr][t[to]],dp[to][i]),bin(prev+(1<<k))[3:])
                if dp[fr][prev]+dist[fr][t[to]]<dp[to][i]:
                    dp[to][i]=dp[fr][prev]+dist[fr][t[to]]
                    #show(bin(i)[2:],bin(prev)[2:],((bef,j),dist[bef][t[j]]),dp)
ans=inf
for i in range(k):ans=min(ans,dp[i][-1])


# 期待値DP     ------------------------------------------------------------------
# https://atcoder.jp/contests/past202012-open/tasks/past202012_k

for i,c in enumerate(t[::-1]):
    if c=='#':
        z+=1<<i
h=w=4
D=h*w
d=[0]*(1<<D)

areas=[[p+i for i in [-1,0,1,-w,w]if 0<=p+i<D and ((p+i)//w==p//w or (p+i)%w==p%w)] for p in range(D)]
for x in range(1,1<<D):
    ans=inf
    for t in range(D): # t = target, q = No of out of space
        q=5-len(areas[t])
        c=5
        rt=q/c
        m=1-q/c
        
        hit=0
        for p in areas[t]:
            if x&(1<<p):
                rt+=(d[(x^(1<<p))]+1)/c
                hit+=1
            else:
                rt+=1/c
                m-=1/c
        if hit!=0: # to avoid 0 divide
            ans=min(rt/m,ans)
    d[x]=ans

print(d[z])

# 部分列DP     ------------------------------------------------------------------
# https://atcoder.jp/contests/past202206-open/tasks/past202206_k

def count_subsequence(a,w=26,mo=998244353):
    n=len(a)
    d=[0]*n
    p=[[-1]*(n+1) for i in range(w)]
    for i in range(n-1,-1,-1):
        for j in range(w):
            p[j][i]=p[j][i+1] if j!=a[i] else i
    
    for j in range(w): # set 1 for 1 character substring
        if p[j][0]!=-1:
            d[p[j][0]]=1
    
    for i in range(n):
        for j in range(w):
            nx=p[j][i+1]
            if nx!=-1:
                d[nx]+=d[i]
                d[nx]%=mo
    return sum(d),p
 
