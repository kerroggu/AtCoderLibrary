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
