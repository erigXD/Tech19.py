# PRE
# from math import gcd # Greater Common divisor (NWD)
# print(gcd(12,16)) # NWD

# 1. Wybór 2 dużych liczb pierwszych
p = 97
q = 101
print(p,q)
# 2. Stworzenie funkcji Eulera F = (p-1) * (q-1) i znalezienie n = p*q
F = (p - 1) * (q - 1)
n = p * q
print(n)
print(F)
# 3. Znalezienie klucza publicznego e: NWD(F, e) = 1
from math import gcd
for i in range(2,F):
  if gcd(i,F) == 1:
    e = i
    break
print(e,n)
# 4. Wygenerowanie klucza prywatnego d: d * e mod F = 1 (odwrotność modulo)
for j in range(2,n):
  if (j * e) % F == 1:
    d = j
    break
print(d,n)

# Przykład działania kodowania znaku x:
# c = x ** e mod n (na szyfrogram)
# t = c ** d mod n (na tekst jawny)
msg = input()
szyfrogram = ""
for i in msg:
  szyfrogram += chr((ord(i)**e) % n)
print(szyfrogram)

jawny = ""
for j in szyfrogram:
  jawny += chr((ord(j) ** d)%n)
print(jawny)


#pseudokod

p = 97
q = 101
wypisz(p,q)

F = (p - 1) * (q - 1)
n = p * q
wypisz(n)
wypisz(F)

F1 = F
dla i w zakresie(2,F)
  dopóki b > 0
    temp = F1
    F1 = i
    i = temp mod i
  jeżeli F1 = 1
    e = i
    przerwij
wypisz(e,n)

dla j w zakresie(2,n)
  jeżeli (j * e) mod F = 1
    d = j
    przerwij
wypisz(d,n)

szyfrogram = ""
dla i w msg:
  szyfrogram = szyfrogram + chr((ord(i)**e) mod n)
wypisz(szyfrogram)

jawny = ""
dla j w szyfrogram:
  jawny = jawny + chr((ord(j) ** d) mod n)
wypisz(jawny)
