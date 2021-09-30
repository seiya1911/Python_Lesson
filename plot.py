import matplotlib
matp;lotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rc('font', **{'family':'Yu Gothic'})

steps = 100
order = 4
maxx = 2

datalist = np.zeros((steps, order))

legend_label = []

x = np.linspace(0, maxx, steps)

for j in range(1, order+1):
    datalist[:,j-1] = x**j
    legend_label.append(str(j) + '**n')

plt.plot(x, datalist)
plt.title('x **n')
plt.xlabel('x')
plt.ylabel('x**n')
plt.legend(legend_label)
plt.show()
