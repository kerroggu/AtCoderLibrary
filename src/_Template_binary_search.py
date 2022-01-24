# Typical bugs/TIPS
# conditionの向きが逆
# ngの初期値の大きさが不十分
# okの初期値の小ささが不十分
# 検索地がintでない場合の数値誤差
# 検索地がintでない場合には打ち切りを、許容誤差ではなく回数で切るとよい場合も。mid=(ok*ng)**0.5 とした方がよい場合も。
# 中央値の検索は、>=kを1，<kを-1として、和が正にできるかで判定。平均の検索は A[i] - k の総和を0以上にできるかを判定。

# function to check if x satisfies the condition
def check(x):
    if is_ok(x):
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
    #print((ok,ng),mid,check(mid))
ans=ok
    
# [ ok | ng ] is the boundary of the condition
