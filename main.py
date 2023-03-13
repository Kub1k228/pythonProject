from random import randint
from matplotlib import pyplot as plt
import numpy as np


def randsprite(n,m):
    a = np.empty((n, m))
    for i in range(n):
        for j in range(m):
            a[i][j] = randint(0, 1)
    k = randint(-1, 1)
    print(k)
    if k == -1 or k == 0 :
      for i in range (n):
          for j in range (m//2):
              a[i][m - j-1] = a[i][j]
    if k == 1 or k == 0 :
      for i in range (n//2):
          for j in range (m):
              a[n-i-1][j] = a[i][j]
    return a

arr_draw = np.empty((10,10))
arr_draw = randsprite(10,10)
voida1 = [1],[1],[1],[1],[1],[1],[1],[1],[1],[1]
void2 = np.empty((2,120))
for i in range (120):
    void2[1][i] = 1
    void2[0][i] = 1

for i in range (10):
    a = [1], [1]
    a = randsprite(10, 10)
    arr_draw = np.concatenate((arr_draw, voida1), axis=1)
    arr_draw = np.concatenate((arr_draw, a), axis=1)


for i in range (10):
    arr = [1],[1]
    arr = randsprite(10,10)
    for j in range(10):
        a = [1], [1]
        a = randsprite(10, 10)
        arr = np.concatenate((arr, voida1), axis=1)
        arr=np.concatenate((arr,a),axis=1)
    arr_draw = np.concatenate((arr_draw,void2),axis=0)
    arr_draw  = np.concatenate((arr_draw,arr),axis=0)

plt.imshow(arr_draw,cmap = 'gray')
plt.show()
