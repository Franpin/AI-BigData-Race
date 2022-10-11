import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#读取原始数据
X = []
f = open('task3.txt')
lineIndex = 1
for v in f:
    if lineIndex > 1:
        X.append([float(v.split()[1]), float(v.split()[2])])
    else:
        pass
    lineIndex += 1
#转化为numpy array
X = np.array(X)

#类簇的数量
n_clusters = 10

#需要选手补全部分
#################################################################






#################################################

plt.title('China')
plt.show()
