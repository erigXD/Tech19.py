# Zad 1 

a = int(input())
b = int(input())
if (a + b) % 2 == 0:
  print("TAK")
else:
  print("NIE")

# Zad 2

import math
a = float(input())
g = float(input())
if a+g/2 > math.sqrt(a+g):
  print("TAK")
else:
  print("NIE")

# Zad 3

k = int(input())
l = int(input())
m = int(input())
if k == l and k == m and m == l:
  print("NIE, wszystkie liczby są równe")
else:
  if k == l:
    print("TAK: k i l")
  else:
    if k == m:
      print("TAK: k i m")
    else:
      if m == l:
        print("TAK: l i m")

# Zad 4

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b and a < c and a < d:
  print("Najmniejsza to + a")
else:
  if b < a and b < c and b < d:
    print("Najmniejsza to + b")
  else:
    if c < a and c < b and c < d:
      print("Najmniejsza to + c")
    else:
      if d < a and d < b and d < c:
        print("Najmniejsza to + d")
      else:
        print("Jest kilka najmniejszych liczb")

# Zad 5

a = int(input())
b = int(input())
c = int(input())
if b - c < a < b + c or a - c < b < a + c or a - b < c < a + b:
  print("TAK")
else:
  print("NIE")

# Zad 6

a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b:
  print("Da się zbudować trójkąt")
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 : 
  print("Prostokątny")
else:
  if a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2 : 
    print("Rozwartokątny")
  else:
    if a**2 + b**2 > c**2 or b**2 + c**2 > a**2 or c**2 + a**2 > b**2 : 
      print("Ostrokątny")
    else: 
      print("Nie da się zbudować trójkątu")
