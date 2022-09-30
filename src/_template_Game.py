

for _ in range(I()):
    ans=0
    n=I()
    b=LI()
    b=[i%2 for i in b]
    X=b.count(0)
    Y=b.count(1)
    
    d=[[[None]*(Y+1) for i in range(X+1)]for a in range(2)]
    d[0][0][0]=1 # win
    d[1][0][0]=0 # lose
    for x in range(X+1):
        for y in range(Y+1):
            if (x,y)==(0,0):
                continue
            for a in range(2):
                if ((X+Y)-(x+y))%2==0: # Alice turn
                    nx=set()
                    if x-1>=0:
                        nx.add(d[a][x-1][y])
                    if y-1>=0:
                        nx.add(d[a^1][x][y-1])
                    
                    #show((a,x,y),nx,d)
                    if 1 not in nx:
                        d[a][x][y]=0
                    else:
                        d[a][x][y]=1
                else: # Bob turn
                    nx=set()
                    if x-1>=0:
                        nx.add(d[a][x-1][y])
                    if y-1>=0:
                        nx.add(d[a][x][y-1])
                    #show((a,x,y),nx,d)
                    if 0 in nx:
                        d[a][x][y]=0
                    else:
                        d[a][x][y]=1
    
    print(['Bob','Alice'][d[0][x][y]])
