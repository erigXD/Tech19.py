# Ankieta
# p = int(input())
# q = int(input())

# if (q >= p * 1.3):
#   print("TAK")
# else:
#   print("NIE")

# Pętle
# print(list(range(10)))
# print(list(range(2,10)))
# print(list(range(12,10,-1)))
# print(list(range(start,stop,step)))
# print(list(range(1,11,3)))

# for i in range(10):
#   print(i, end="\t")


# for i in range(0,10,2):
#   print(i**2, end=" ")

# L = [1,2,3,4,5,6]
# print(L[1:4:2])

# pętla liczb dwucyfrowych od 10 do 21
# for i in range(10,22):
#   print(i, end=" ")
  
# pętla liczb dwucyfrowych nieparzystych od 15 do 31
# for i in range(15,32,2):
#   print(i, end=" ")
  
# pętla liczb dwucyfrowych malejąco (step ujemny)
# for i in range(99,9,-1):
#   print(i, end=" ")

# pętla liczb dwucyfrowych malejąco (step dodatni)
# for i in range(10,100,1):
#   print(109-i, end=" ")
  
# pętla liczb trzycyfrowych podzielnych przez 20
# for i in range(100,1000,20):
#   print(i, end=" ")


# Zad 1
# n = int(input())
# for i in range(n):
#   print(i**3 + 3, end=" ")

# Zad 2
# for i in range(105,1000,15):
#   print(i, end=" ")

# Zad 3
# n = int(input())
# for i in range(1,n+1):
# if n % i == 0:
#   print(i, end=" ")

# Zad 4
# suma=0
# for i in range(10,100):
#   suma = suma + i
#   print(suma, end=" ")

# Zad 5
# n = int(input())
# suma = n*(n+1)//2

# for i in range(n-1):
#   x = int(input())
#   suma = suma - x
# print(suma)

# print(n*(n+1)/2) # ciąg paskala

# # to samo ale w pętli
# suma = 0
# for i in range(1,n+1):
#   suma = suma + i
#   print(suma)

# Zad 6
# from time import * # Importowanie funkcji z bibliotek. * oznacza importowanie wszystkiego z biblioteki.
# Ciąg Fibonacciego:
# n = int(input())
# a = 1
# b = 1
# print(a, end=" ")
# print(b, end=" ")
# for i in range(n-1):
#   a, b = b, a+b
#   print(b, end=" ")

# POST - utrwalenie pętli

# Pętle for liczb trzycyforowych podzielnych przez 13 (2 sposoby)
# for i in range(104,1000,13):
#   print(i, end=" ")

# for i in range(100,1000):
#   if i % 13 == 0:
#     print(i, end=" ")

# Pętle for liczb dwucyfrowych parzystych (3 sposoby)
# for i in range(10,100,2):
#   print(i, end=" ")

# for i in range(10,100):
#   if i % 2 == 0:
#     print(i, end=" ")

# for i in range(5,50):
#   print(i*2, end=" ")
    
# Pętle for potęg cyfr: WY: 0, 1, 4, 9, 16 .. 81 (2 sposoby printa)
for i in range(10):
  print(i**2, end=" ")

for i in range(10):
  print(f"i^2 = {i**2}")

for i in range(10):
  print(i, "^2=", i**2, sep="")

for i in range(10):
  print(str(i) + "^2=" + str(i**2))
