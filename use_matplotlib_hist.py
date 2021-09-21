import use_matplotlib_hist

matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc('font', **{'family':'Yu Gothic'})

data = np.random.randn(1000)
plt.hist(data, bins=20)

plt.title('histgram')
plt.xlabel('data')
plt.ylabel('frequence')

plt.show()