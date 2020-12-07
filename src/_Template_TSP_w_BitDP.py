## Traveling Salesman Problem with BitDP. O(k^2 * 2^k)
## verified by PAST-3 M
## https://atcoder.jp/contests/past202005-open/tasks/past202005_m

init_d=bfs(g,s)

dist=[]
for i in range(k):
    d=bfs(g,t[i])
    dist+=[d]
 
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
for i in range(k):
    ans=min(ans,dp[i][-1])
