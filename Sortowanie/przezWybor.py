# wygenerujcie losową listę 7 elementów z przedziału [1,20]

from random import randint
n = 17
T = [randint(1, 100) for i in range(n)]
print(T)

# 6 typów sortowań:
# Bąbelkowe
# Wybór (uczy na indexach działać)
# Kubełkowe
# Merge (podchodzi pod rekurencje)
# Scalanie
# Quick Sort

# Od najmniejszej do największej

for i in range(n):
  mi = i
  for j in range(i,n):
    if T[j] < T[mi]:
      mi = j
  T[i], T[mi] = T[mi], T[i]
print(T)