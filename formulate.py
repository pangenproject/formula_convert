import numpy

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
