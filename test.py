# Zad 1

# a = int(input("Podaj licznik:"))
# b = int(input("Podaj mianownik:"))

# c = int(input("Podaj licznik:"))
# d = int(input("Podaj mianownik: "))

# ilocz = b*d
# x = b
# y = d

# while x!=y:
#   if y>x: 
#     y-=x
#   else:
#     x-=y

# wsp_mian = ilocz//x

# print(wsp_mian)

# e = int(input("Podaj licznik:"))
# f = int(input("Podaj mianownik: "))

# ilocz1 = wsp_mian*f
# w = wsp_mian
# k = f

# while w!=k:
#   if k>w: 
#     k-=w
#   else:
#     w-=k

# wsp_mian1 = ilocz1//w
# print(wsp_mian1)

# Zad 2

liczba_1 = 220
liczba_2 = 284

def dzielniki_wlasciwe(liczba):
  if liczba == 0:
    return None
    lista = []
    polowka = liczba // 2

for i in range(1, polowka + 1):
  if liczba % i == 0:
    lista.append(i)
    return lista
    dzielniki_1 = dzielniki_wlasciwe(liczba_1)
    dzielniki_2 = dzielniki_wlasciwe(liczba_2)

def sumuj(tablica):
  suma = 0
  for liczba in tablica:
    suma += liczba
    return suma
    suma_1 = sumuj(dzielniki_1)
    suma_2 = sumuj(dzielniki_2)

if liczba_1 == suma_2 and liczba_2 == suma_1:
  print('Podane liczby sa liczbami zaprzyjaznionymi')
  print('Liczba', liczba_1, 'to suma dzielników', dzielniki_2, 'liczby', liczba_2)
  print('Liczba', liczba_2, 'to suma dzielników', dzielniki_1, 'liczby', liczba_1)
else:
  print('Niestety, to nie są liczby zaprzyjaźnione')