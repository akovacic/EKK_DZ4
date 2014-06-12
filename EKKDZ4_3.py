import math
p=191
m=int(math.ceil(2*(p**0.25)))
E=EllipticCurve(GF(p), [1,4])
P=E([24,10])
Q=int((p+1+math.floor(2*math.sqrt(p))))*P
listaAdicija=[]
for j in range(m):
    listaAdicija.append(j*P)
for i in range(m):
    if (listaAdicija.count(Q-i*(m*P))):
        m
        i
        listaAdicija.index(Q-i*(m*P))
        int(math.floor(2*math.sqrt(p)))
        t=i*m+listaAdicija.index(Q-i*(m*P))-int(math.floor(2*math.sqrt(p)))
t
order=p+1-t
order
8
1
3
27
-16
208