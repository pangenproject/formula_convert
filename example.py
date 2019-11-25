import math
import numpy as np
import pycosat as pysat
import csv

N = 100
REPEAT = 20
list_results = []


def dw_solve(formulas, qubo):
    dw_instance = wq.opt()
    dw_instance.qubo = qubo
    dw_instance.dwavetoken = "DEV-283ae48a24e86ddd7654f48e223202dfd4a26ce0"
    spins_conf = dw_instance.dw()
    bin_vector_dw = [1 if spin == 1 else 0 for spin in spins_conf]

    return bin_vector_dw

def wq_solve(formulas, qubo):
    wildqat_instance = wq.opt()
    wildqat_instance.qubo = qubo

    bin_vector_wildqat = wildqat_instance.sa()

    return bin_vector_wildqat



for i in range(1, N):
    d = 0
    w = 0 
    p = 0
    alfa = 2 * i

    for j in range(0, REPEAT):

        cnf_formulas = tcnfgen(alfa, N)

        qubo, const = formulate(cnf_formulas, N)


        bin_vector_dw = dw_solve(cnf_formulas, qubo)
        if np.dot(bin_vector_dw, np.dot(qubo, bin_vector_dw)) + const == 0:
            d = d + 1

        bin_vector_wildqat = wq_solve(cnf_formulas, qubo)

        if np.dot(bin_vector_wildqat, np.dot(qubo, bin_vector_wildqat)) + const == 0:
            w = w + 1

        if pysat.solve(cnf_formulas) == 'UNSAT':
            p = p + 1

    results = [alfa/N, d/REPEAT, w/REPEAT, (REPEAT-p)/REPEAT]
    list_results.append(results)
    myFile = open('compare.csv', 'a')
    with myFile:
        writer = csv.writer(myFile)
        print(results)
        writer.writerows([results])
