import pycosat
import matplotlib.pyplot as plt
%matplotlib inline
N= 50
M=30
C=[]
for i in range(0,N):
    s = 0
    alfa = 2*i
    for j in range(0,M):

        f = tcnfgen(alfa,N)
        q,const= formulate(f,N)
        b = wq.opt()
        b.qubo = q
        X=b.sa()

        if np.dot(X,np.dot(q,X))+const==0:
            s = s+1
    C.append([2*i/N,(M-s)/M])
plt.plot([x[0] for x in C],[y[1] for y in C])
