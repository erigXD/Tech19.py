# wygeneruj liste 20 losowych liczb z przedziału (1, 20)

from random import randint

L = [randint(1, 20) for i in range(20)]
print(L)

# znalezc maxa
print(max(L))
# ile razy występuje wartosc minimalna
print(L.count(min(L)))
# znajdz vice-max
for i in range(L):
  
  
  