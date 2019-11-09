import pycosat
N= 100
M=100
C=[]
for i in range(0,N):
    s = 0
    for j in range(0,M):
        alfa = 2*i
        if pycosat.solve(tcnfgen(alfa,N))=='UNSAT':
            s = s+1
    C.append([i,(M-s)/M])
plt.plot([x[0] for x in C],[y[1] for y in C])
