import math
N= 20
Z=2
M= 20
C = []
Cavg = []
for i in range(1, N):
    s = 0
    t = 0
    m = 0
    alfa = 2*i
    dwAVG = 0
    wqAVG = 0
    for j in range(0, M):
        f = tcnfgen(alfa, N)
        q, const = formulate(f, N)
        b = wq.opt()
        b.qubo = q
        b.dwavetoken = "DEV-283ae48a24e86ddd7654f48e223202dfd4a26ce0"
        X = b.dw()
        a = wq.opt()
        a.qubo = q
        Y = a.sa()
        for i in range(0,Z):
          X = b.dw()
          X=[1 if x==1 else 0 for x in X]
          if np.dot(X, np.dot(q, X))+const == 0:
            s = s+1
            break

        X=[1 if x==1 else 0 for x in X]
        if np.dot(X, np.dot(q, X))+const == 0:
            s = s+1
        dwAVG = dwAVG + np.dot(X, np.dot(q, X))+const
        for i in range(0,Z):
          Y = a.sa()
          
          if np.dot(X, np.dot(q, X))+const == 0:
            t = t+1
            break


        if np.dot(Y, np.dot(q, Y))+const == 0:
            t = t+1
        wqAVG = wqAVG + np.dot(Y, np.dot(q, Y))+const
        if pycosat.solve(f) == 'UNSAT':
            m = m+1
            
       
    results = [alfa/N,s/M,(M-m)/M]
    resultsAVG = [dwAVG/M,wqAVG/N]
    C.append(results)
    C.append(resultsAVG)
    myFile = open('battle3.csv', 'a')
    myFileAVG = open('battleAVG.csv','a')
    with myFile:
        writer = csv.writer(myFile)
        print(results)
        writer.writerows([results])
        writer = csv.writer(myFileAVG)
        print(results)
        writer.writerows([resultsAVG])
