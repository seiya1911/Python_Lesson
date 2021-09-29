import numpy as np
import pandas as pd
import os
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

os.chdir(r"/Users/seiyanishikawa/Documents/python_scripts")

df = pd.read_csv('sample2.csv')

df.plot()
print('次に進むにはグラフウィンドウを閉じてください')
plt.show()

df.plot.bar(stacked=True)
print('次に進むにはグラフウィンドウを閉じてください')
plt.show()

df.plot.scatter('Japanese', 'English')
print('次に進むにはグラフウィンドウを閉じてください')
plt.show()

df['Total'] = df.sum(axis=1)

df['Total'].plot.hist()
print('次に進むにはグラフウィンドウを閉じてください')
plt.show()