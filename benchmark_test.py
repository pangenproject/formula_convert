import random
import numpy

N = 10**3
M = 10**3

import random
import numpy

N = 10**3
M = 10**3

def tcnfgen(m,k):
    cnf = []
    
    def wzero(k):
        t = random.randint(-k+1,k)
        s = sgn(t)
        if s<= 0:
            t = t-1
        return t
    
    def sgn(k):
        if(k>0):
            return 1
        elif(k==0):
            return 0
        elif(k<0):
            return -1
    
    def unique(l,k):
        t = wzero(k)
        while(t in l or t.reverse() in l):
            t = wzero(k)
        return t

    for i in range(m):
        x = wzero(k)
        
        y = wzero(k)
        while abs(y) == abs(x):
            y = wzero(k)
        while([x,y] in cnf):
            x = wzero(k)
            y = wzero(k)
            while abs(y) == abs(x):
                y = wzero(k)
        

        cnf.append([x,y])

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

import datetime
start = datetime.datetime.now()
print("script execution stared at:", start)
b = wq.opt()
b.qubo = q
b.sa()
print("script run times")
end = datetime.datetime.now()
print("Script execution ended at:", end)
total_time = end - start
print("Script totally ran for :", total_time)


