ans=0
l,r=0,0
tmp=1
while r<n:
    if tmp*s[r]<=k:  # 条件を満たすならrを1進める
        tmp*=s[r]
        r+=1
        ans=max(r-l,ans)
    else:
        if l<r:  # 条件を満たさず、l<rならlを1進める
            tmp//=s[l]
            l+=1
        else:  # lがrを追い越さないように。l=rならrを進める。
            tmp*=s[r]
            r+=1
print(ans)
