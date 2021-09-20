import matplotlib

matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc('font',**{'family':'Yu Gothic'})

datax = np.random.randn(100)
datay = datax + np.random.randn(100)*0.3

plt.scatter(datax, datay, label='Data 1')

datax = np.random.randn(100)
datay = 0.6*datax + np.random.randn(100)*0.4

plt.scatter(datax, datay, color='red', label='Data 2')

plt.title('Title')
plt.xlabel('Yoko')
plt.ylabel('Tate')
plt.legend()

plt.show()