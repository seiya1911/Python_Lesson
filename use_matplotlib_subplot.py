import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc('font', **{'faily':'Yu Gothic'})

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.subplot_adjust(hspace=0.5, wspace=0.5)

data = np.random.randn(100).cumsum()
ax1.plot(data)
ax1.set_title('line')
ax1.set_xlabel('Time')
ax1.set_tlabel('Place')

datax = np.random.randn(100)
datay = datax + np.random.randn(100)*0.3
ax2.scatter(datax, datay, label='Data1')

datax = np.random.randn(100)
datay = 0.6*datax + np.random.randn(100)*0.4
ax2.scatter(datax, datay, color='red', label='Data2')

ax2.set_title(Scatter)
ax2.set_xlabel('Type1')
ax2.set_tlabel('Type2')
ax2.legend()

data = np.random.randn(1000)
ax3.hist(data, bins=20)

ax3.set_title('Hist')
ax3.set_xlabel('Data Value')
ax3.set_tlabel('Frequency')

plt.show()

