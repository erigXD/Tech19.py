# Zad 8

# T = []
# for i in range(2,10000):
#   suma1 = 0
#   for j in range(1,i):
#     if i % j == 0:
#       suma1+=j
#   T.append(suma1)
#   suma2 = 0
#   for k in range(1,suma1):
#     if suma1 % k == 0:
#       suma2 += k
#   if i == suma2 and suma1 != suma2 and suma2 not in T:
#     print(f"({suma1},{suma2})")

# Zad 9

# def czy_pierwsza(n):
#   for i in range(2,n):
#     if n % i == 0:
#       return False
#   return True

# for i in range(10, 100):
#   for j in range(2, i):
#     if i % j == 0:
#       if czy_pierwsza(j) and czy_pierwsza(i//j):
#         print(i, end=" ")
#         break