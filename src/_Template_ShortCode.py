################## input ##################

###  n\n a1 a2 a3\n -> n=n,a=[a1,a2,a3]
n,*a=map(int,open(0).read().split())

###  x\n y\n z\n -> a=[x,y,z]
*a,=map(int,open(0))


################## combination ##################

###  (n,k)
w=1
for i in range(k):w=w*(n-i)*pow(i+1,-1,M)%M
print(w)
