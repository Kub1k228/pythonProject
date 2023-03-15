from random import randint
from matplotlib import pyplot as plt
import numpy as np


def randsprite(n,m):
    a = np.empty((n, m))
    for i in range(n):
        for j in range(m):
            a[i][j] = randint(0,1)
    for i in range(n):
        startpos = randint(1,1024)

        for j in range(m):
            color = randint(startpos - 50, startpos + 50)
            if(a[i][j]==1):
                a[i][j] = color
    k = randint(-1, 1)
    if k == -1 or k == 0 :
      for i in range (n):
          for j in range (m//2):
              a[i][m - j-1] = a[i][j]
    if k == 1 or k == 0 :
      for i in range (n//2):
          for j in range (m):
              a[n-i-1][j] = a[i][j]

    return a


n = 33
m = 33
arr_draw = np.empty((n,m))
arr_draw = randsprite(n,m)
voida1 = np.full((n,1),1024)
void2 = np.empty((2,m * (m+2)))
for i in range (m * (m+2)):
    void2[1][i] = 1024
    void2[0][i] = 1024

for i in range (m):
    a = [1], [1]
    a = randsprite(n, m)
    arr_draw = np.concatenate((arr_draw, voida1), axis=1)
    arr_draw = np.concatenate((arr_draw, a), axis=1)


for i in range (n):
    arr = [1],[1]
    arr = randsprite(n,m)
    for j in range(m):
        a = [1], [1]
        a = randsprite(n, m)
        arr = np.concatenate((arr, voida1), axis=1)
        arr=np.concatenate((arr,a),axis=1)
    arr_draw = np.concatenate((arr_draw,void2),axis=0)
    arr_draw  = np.concatenate((arr_draw,arr),axis=0)

plt.imshow(arr_draw,cmap = 'CMRmap')
plt.show()
