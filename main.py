from random import randint
from matplotlib import pyplot as plt
import numpy as np


def randsprite(n,m):
    a = np.empty((n, m))
    for i in range(n):
        for j in range(m):
            a[i][j] = randint(0, 1)
    for i in range (n):
        for j in range (m//2):
            a[i][m - j-1] = a[i][j]
    for i in range (n//2):
        for j in range (m):
            a[n-i-1][j] = a[i][j]
    return a


arr = np.empty((100,100))
a = np.empty((5,5))
for i in range (20):
    a=randsprite(5,5)
    arr = np.concatenate(arr,a)

plt.imshow(arr,cmap = 'gray')
plt.show()