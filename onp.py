# ONP - Odwrócona notacja polska

# Kolejki: Fifo/Lifo (First in first out / Last in first out) (Stos/Stack)

# ONP
# 12 7 5 - / 4 2 5 * + - (działań musi być o jedno mniej od liczb)
# Może być kartkówka

# Zamiana normalnego działania na ONP:
# 7 + 8 * 5 => 7 8 5 * +
# ((5 - 7) * 3) * (8 - 5) * (4 + 1)
# stos: ( ( - ) | (*) | (-) | * ( ) 
# wyjście: 5 7 | 5 7 - | 5 7 - 3 * 8 5 - * 4 1 + *

# piorytety:
# () => 0
# + i - => 1
# * i : => 2
# ^ => 3



# Algorytm na obliczanie ONP:

# ciag = input()
# stos = []
# for i in ciag:
#   if i.isdigit(): stos.append(int(i))
#   else:
#     b, a = stos.pop(), stos.pop()
#     if i == "+": stos.append(a + b)
#     elif i == "-": stos.append(a - b)
#     elif i == "*": stos.append(a * b)
#     elif i == "/": stos.append(a // b)
#   print(stos)
