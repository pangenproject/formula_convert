import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('pycosatvswq.csv', delimiter=',', skip_header=10,
                     skip_footer=10, names=['alpha', 'wq', 'pycosat'])
fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("100 variables 2-SAT")
ax1.set_xlabel('clause Density')
ax1.set_ylabel('% satisfiability ')

ax1.plot(data['alpha'], data['wq'], color='r', label='wq')
ax1.plot(data['alpha'], [1-x for x in data['pycosat']], color='b', label='pycosat')


fig.show()
