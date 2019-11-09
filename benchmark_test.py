import random
import numpy

N = 10**4
M = 10**4

def tcnfgen(m,k,horn=1):
    cnf = []
    def unique(l,k):
        t = random.randint(-k,k)
        while(t in l):
            t = random.randint(-k,k)
        return t
    r = (lambda : random.randint(0,1))
    for i in range(m):
        x = unique([],k)
        y = unique([x],k)
        z = unique([x, y],k)
        if horn:
            cnf.append([x,y])
        else:
            cnf.append([(x,r()), (y,r())])
    return cnf
a = tcnfgen(M,N)



X = 0
Y = 1

def formulate(cnfs, N):
    qubo = numpy.zeros(shape=(N,N))
    const = 0
    for cnf in cnfs:
        i, j = abs(cnf[X])-1, abs(cnf[Y])-1
        if cnf[X] > 0 and cnf[Y] > 0:
            const = const + 1
            qubo[i,i] = qubo[i,i] -1
            qubo[j,j] = qubo[j,j] -1
            qubo[i,j] = qubo[i,j] + 1/2
            qubo[j,i] = qubo[j,i] + 1/2
        elif cnf[X] > 0 and cnf[Y] < 0:
            qubo[j,j] = qubo[j,j] + 1
            qubo[i,j] = qubo[i,j] + 1/2
            qubo[j,i] = qubo[j,i] + 1/2
        elif cnf[X] < 0 and cnf[Y] > 0:
            qubo[i,i] = qubo[i,i] + 1
            qubo[i,j] = qubo[i,j] - 1/2
            qubo[j,i] = qubo[j,i] - 1/2
        elif cnf[X] < 0 and cnf[Y] < 0:
            qubo[i,j] = qubo[i,j] + 1/2
            qubo[j,i] = qubo[j,i] + 1/2
    return qubo
q= formulate(a,N)

b = wq.opt()
b.qubo = q
b.sa()
