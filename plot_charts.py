import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

data = np.genfromtxt('battleAVG.csv', delimiter=',', 
                      names=['alpha', 'dw', 'wq', 'pycosat'])
fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("100 variables 2-SAT")
ax1.set_xlabel('clause Density')
ax1.set_ylabel('% satisfiability ')

ax1.plot(data['alpha'], data['dw'], color='r', label='dw')
#ax1.plot(data['alpha'], data['wq'], color='b', label='wq')
ax1.plot(data['alpha'], data['pycosat'], color='y', label='pycosat')
plt.legend(title='Compared')
fig.show()
