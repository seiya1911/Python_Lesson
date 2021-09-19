import matplotlib

matplotlib.use('tkagg')
import matplotlib.pyplot as plt

matplotlib.rc('font', **{'family':'Yu Gothic'})

plt.plot([1,2,3], 'k-', label='系列1')
plt.plot([2,3,4], 'r--', label='系列2')
plt.plot([3,4,5], 'b--o', label='系列3')

plt.title('タイトル')
plt.xlabel('横軸')
plt.ylabel('縦軸')
plt.legend()
plt.show()