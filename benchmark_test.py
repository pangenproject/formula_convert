import pycosat
import matplotlib.pyplot as plt
# %matplotlib inline
import wildqat as wq
import random
import numpy as np
import csv

def tcnfgen(m, k):
    cnf = []

    def wzero(k):
        t = random.randint(-k + 1, k)
        s = sgn(t)
        if s <= 0:
            t = t - 1
        return t

    def sgn(k):
        if (k > 0):
            return 1
        elif (k == 0):
            return 0
        elif (k < 0):
            return -1

    def unique(l, k):
        t = wzero(k)
        while (t in l or t.reverse() in l):
            t = wzero(k)
        return t

    for i in range(m):
        x = wzero(k)

        y = wzero(k)
        while abs(y) == abs(x):
            y = wzero(k)
        while ([x, y] in cnf):
            x = wzero(k)
            y = wzero(k)
            while abs(y) == abs(x):
                y = wzero(k)

        cnf.append([x, y])

    return cnf






def formulate(cnfs, N):
    X = 0
    Y = 1
    qubo = np.zeros(shape=(N, N))
    const = 0
    for cnf in cnfs:
        i, j = abs(cnf[X]) - 1, abs(cnf[Y]) - 1
        if cnf[X] > 0 and cnf[Y] > 0:
            const = const + 1
            qubo[i, i] = qubo[i, i] - 1
            qubo[j, j] = qubo[j, j] - 1
            qubo[i, j] = qubo[i, j] + 1 / 2
            qubo[j, i] = qubo[j, i] + 1 / 2
        elif cnf[X] > 0 and cnf[Y] < 0:
            qubo[j, j] = qubo[j, j] + 1
            qubo[i, j] = qubo[i, j] + 1 / 2
            qubo[j, i] = qubo[j, i] + 1 / 2
        elif cnf[X] < 0 and cnf[Y] > 0:
            qubo[i, i] = qubo[i, i] + 1
            qubo[i, j] = qubo[i, j] - 1 / 2
            qubo[j, i] = qubo[j, i] - 1 / 2
        elif cnf[X] < 0 and cnf[Y] < 0:
            qubo[i, j] = qubo[i, j] + 1 / 2
            qubo[j, i] = qubo[j, i] + 1 / 2
    return qubo, const



N= 100
M= 10
C = []
for i in range(1, N):
    s = 0
    m = 0
    alfa = 2*i
    for j in range(0, M):
        f = tcnfgen(alfa, N)
        print(f)
        q, const = formulate(f, N)
        b = wq.opt()
        b.qubo = q
        X = b.sa()

        if np.dot(X, np.dot(q, X))+const == 0:
            s = s+1
        if pycosat.solve(tcnfgen(alfa, N)) == 'UNSAT':
            m = m+1

    C.append([2*i/N, (M-s)/M, (M-m)/M])
    myFile = open('pycosatvswq.csv', 'a')
    with myFile:
        writer = csv.writer(myFile)
        print([2*i/N], [(M-s)/M])
        writer.writerows([[2*i/N, (M-s)/M, (M-m)/M]])

# plt.plot([x[0] for x in C], [y[1] for y in C])

