# https://atcoder.jp/contests/arc020/tasks/arc020_3
 
def db_f(a,l,m):
    x=a
    rt=0
    cd=1
    D=pow(10,len(str(a)),m)
    k=l.bit_length()
    for i in range(k):
        if (l>>i)&1:
            rt+=x*cd
            cd*=D
            cd%=mo
        x=x*D+x
        x%=m
        
        D=D*D%m
    return rt
