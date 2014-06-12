import math
E=EllipticCurve(GF(211),[2,4])
E
c=[]
s=[]
bini=106
bini=bin(bini)
bini=bini[2:len(bini)]
bini='00'+bini
bini=list(bini)
c.append(0)
d=len(bini)
bini=list(reversed(bini))
for i in range(d-1):
    c.append(math.floor((int(bini[i])+int(bini[i+1])+c[i])/2))
    s.append(int(bini[i])+c[i]-2*c[i+1])
s
P=E([0,2])
Q=P
for i in reversed(range(len(s)-1)):
    Q=2*Q
    if(s[i]==1): Q=Q+P
    if(s[i]==-1): Q=Q-P
Q
Elliptic Curve defined by y^2 = x^3 + 2*x + 4 over Finite Field of size 211
[0.0, 1.0, 0.0, 1.0, 0.0, -1.0, 0.0, 1.0]
(2 : 4 : 1)