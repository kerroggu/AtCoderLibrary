# Library for Geometory
# tested by https://atcoder.jp/contests/ttpc2015/tasks/ttpc2015_h
# tested by https://atcoder.jp/contests/abc151/tasks/abc151_f

# Sample usage
#
# CrossProduct(x1,y1,x2,y2) : returns cross product of vectors (x1,y1),(x2,y2) = x1*y2-x2*y1
# IsInside(a,b,x1,y1,x2,y2,x3,y3) : returns if (a,b) inside the triangle with verteces (x1,y1),(x2,y2),(x3,y3)
# Surface(x1,y1,x2,y2,x3,y3) : returns the area of the triangle with verteces (x1,y1),(x2,y2),(x3,y3)
# Center_of_3points(x1,y1,x2,y2,x3,y3): returns the center of the 3 points and the distance
# Rotate2D(x,y,q): rotate (x,y) by q (radian) and returns the coordinates


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

def Center_of_3points(x1,y1,x2,y2,x3,y3):
    cx = ((y1-y3)*(y1**2 -y2**2 +x1**2 -x2**2) -(y1-y2)*(y1**2 -y3**2 +x1**2 -x3**2)) / (2*(y1-y3)*(x1-x2)-2*(y1-y2)*(x1-x3))
    cy = ((x1-x3)*(x1**2 -x2**2 +y1**2 -y2**2) -(x1-x2)*(x1**2 -x3**2 +y1**2 -y3**2)) / (2*(x1-x3)*(y1-y2)-2*(x1-x2)*(y1-y3))
    r=((x1-cx)**2+(y1-cy)**2)
    return cx,cy,r
 
def Rotate2D(x,y,q):
    s=x*math.cos(q)-y*math.sin(q)
    t=x*math.sin(q)+y*math.cos(q)
    return (s,t)
