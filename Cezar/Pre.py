# # Funkcja ord() - zwraca kod ascii dla danego znaku (A-Z)
# print(ord("B"))

# # Funkcja chr() - zwraca znak dla danego kodu ascii (65-90)
# print(chr(83))

# # można łączyć....
# print(chr(ord("C")))
# print(chr(ord("C") + 1))

# # napisz alfabet za pomocą pętli for
# for i in range(65, 91):
#   print(chr(i), end="")

# # jak wydobyć literki z napisu...
# napis = "POLSKA"
# print(len(napis)) # len - długość napisu
# print(napis[0])
# print(napis[1])

# # napisz pętlę wyciągającą z napisu literki

# napis = input()
# #napis = napis.replace(" ", "") # zamiana liter w tekście
# for i in range(len(napis)):
#   print(napis[i])

# # napisz pętle wyciągającą kody ascii z napisu

# napis = input()
# for i in range(len(napis)):
#   print(ord(napis[i]))

# zaszyfruj napis Cezarem w kluczu = 3

# napis = input()
# szyfr = ""
# for i in range(len(napis)):
#   szyfr += chr(65 + (ord(napis[i]) - 65 + 3) % 26)
# print(napis, szyfr)

# program który doda dwa ułamki

# 1 podejście - źłe
# a = int(input())
# c = int(input())
# print()
# b = int(input())
# d = int(input())

# w = c
# k = d
# suma = 0
# while d > 0:
#   r = c%d
#   c=d
#   d=r
#   suma += 1
# NWW = (w * k / c)
# licznik_a = (NWW // b) * a
# licznik_b = (NWW // d) * c

# print(f"{a}/{b} + {c}/{d} = {licznik_a+licznik_b}/{NWW}")


# 2 podejście - prawidłowe
# a = int(input())
# b = int(input())
# print()
# c = int(input())
# d = int(input())

# x = b
# y = d
# iloczyn = x*y
# while y>0:
#   x, y = y, x%y
# nww = iloczyn // x

# e = (nww // b) * a
# f = (nww // d) * c
# g = e + f
# cała = g//nww
# h = g%nww

# print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww} = {cała} {h}/{nww}")