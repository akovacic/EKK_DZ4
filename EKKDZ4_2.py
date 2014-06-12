krivulje=[]
for i in range (17):
    for j in range(17):
        if ((4*(i**3)+27*(j**2))  % 17 != 0):
            E=EllipticCurve(GF(17), [i,j])
            if (E.order()==20):
                if (E not in krivulje): krivulje.append(E)
for i in range(len(krivulje)):
    krivulje[i]