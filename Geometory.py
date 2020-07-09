# Library for Geometory
# tested by https://atcoder.jp/contests/ttpc2015/tasks/ttpc2015_h

# Sample usage
# p=[(x[i],y[i]) for i in range(n)]
#
# CrossProduct(*p[1],*p[2]) : returns cross product of vectors (x1,y1),(x2,y2) = x1*y2-x2*y1
# IsInside(a,b,*p[i],*p[j],*p[k]) : returns if (a,b) inside the triangle with verteces (xi,yi),(xj,yj),(xk,yk)
# Surface(*p[i],*p[j],*p[k])) : returns the area of the triangle with verteces (xi,yi),(xj,yj),(xk,yk)


def CrossProduct(x1,y1,x2,y2):
    rt=x1*y2-x2*y1
    return rt
    
def IsInside(x,y,a1,b1,a2,b2,a3,b3):
    p1=CrossProduct(a2-a1,b2-b1,a1-x,b1-y)
    p2=CrossProduct(a3-a2,b3-b2,a2-x,b2-y)
    p3=CrossProduct(a1-a3,b1-b3,a3-x,b3-y)
    if p1<0:
        p1*=-1
        p2*=-1
        p3*=-1
    if p1>0 and p2>0 and p3>0:
        return True
    else:
        return False

def Surface(a1,b1,a2,b2,a3,b3):
    A,B=a2-a1,b2-b1
    C,D=a3-a1,b3-b1
    return abs(A*D-B*C)/2

