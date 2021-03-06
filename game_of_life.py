# -*- coding: utf-8 -*-
"""Game of Life

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rjiuZ-d5Lw-WA6FAd6IpDjU2ZvL7sWCh
"""

#Game of Life

#karoları oluşturmak için yazılan fonk.

import matplotlib.pyplot as plt

def plotMat(kare):
  plt.imshow(kare, cmap='binary') #binary=siyah-beyaz,
  plt.show()

#random bir matrix oluşturuldu.
import numpy as np

length = 50
size = (length,length)

A = np.random.randint(0, high=2, size=size, dtype=int)

print(A)
plotMat(A)

#Kuralları içeren bir fonksiyon yazıldı.

def step(A):
    for r in range(1, length - 1):
      for c in range(1, length - 1):
          # print(A[r][c+1] - A[r][c])
          # print(A[r][c])
        sum = A[r][c+1] + A[r][c-1] + A[r-1][c] + A[r+1][c]
          # print(sum)
        if sum > 2:
            A[r][c] = 1
        elif sum < 2:
            A[r][c] = 0
    return A

print(step(A))
plotMat(step(A))

#Bunu 30 kez döngüye alarak bir örüntü elde etmek istedik. Ama yalnızca 2. döngüdekini alıp 30 kez yazdı. Yani ikinci döngüyü fonksiyona ekleyerek 
#üçüncü döngüyü oluşturup bu şekilde devam ettiremedik.

for i in range(30):
  plotMat(step(A))

