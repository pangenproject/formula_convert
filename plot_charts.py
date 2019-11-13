import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('pycosatvswq.csv', delimiter=',', skip_header=10,
                     skip_footer=10, names=['x', 'y', 'z'])
fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("alpga")
ax1.set_xlabel('alpga')
ax1.set_ylabel('% ')

ax1.plot(data['x'], data['y'], color='r', label='the data')
ax1.plot(data['x'], [1-x for x in data['z']], color='b', label='the data')


fig.show()
