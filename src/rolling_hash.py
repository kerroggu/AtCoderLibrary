def rolling_hash(a,m,mo=10**9+7): # return list of rolling_hash values of [a[i:i+m] for i in range(n-m+1)]
    n=len(a)
    z=pow(2,101,mo)
    pz=[]
    zm=1
    for i in range(m):
        pz+=zm,
        zm=zm*z%mo
    pz=pz[::-1]
    ha=0
    for i in range(m):
        ha=(ha+a[i]*pz[i])%mo
    
    rt=[ha]
    for i in range(n-m):
        ha=(ha*z-a[i]*zm+a[i+m])%mo
        rt+=ha,
    return rt
