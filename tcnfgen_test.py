import pycosat
N= 100
M=100
C=[]
for i in range(0,N):

    for j in range(0,M):
        s = 0
        if pycosat.solve(tcnfgen(N-int(j/2),N))=='UNSAT':
            s = s+1
    C.append([i,(M-s)/M])
plt.plot([x[0] for x in C],[y[1] for y in C])
