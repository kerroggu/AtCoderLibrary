# function to check if x satisfies the condition
def check(x):
    if x==condition:
        rt=True
    else:
        rt=False
    return rt

# initial value
ok=0
ng=10**12

while abs(ok-ng)>1:
    mid=(ok+ng)//2
    if check(mid):
        ok=mid
    else:
        ng=mid

# [ ok | ng ] is the boundary of the condition
