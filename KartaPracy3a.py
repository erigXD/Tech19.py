# Zad 1
# n = int(input())

# for i in range(n):
#   print("*-|", end=" ")

# Zad 2
# n = int(input())

# for i in range(1, n+1):
#   print("*" * i, end="")
#   if i%2:
#     print("||", end="")
#   else:
#     print("--", end="")

# Zad 3
# n = int(input())
# for i in range(1,n+1):
#   print("*", end="")
#   if i % 2 == 0:
#     print("-"*i, end="")
#   else:
#     print("|"*i, end="")

# Zad 5
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     if j == n//2:
#       print("*", end="")
#     elif i == n//2:
#       print("-", end="")
#     else:
#       print(" ", end="")
#   print()

# Zad 6
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     if i + j == n-1:
#       print("?", end="")
#     elif i - j == 0:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()
    

# PRE - Tabliczka mnożenia

# for i in range(1,11):
#   for j in range(1,11):
#     print(i*j, end="\t") # \t - Tab
#   print() # enter

# PRE na 2 pętle:
# *
# **
# ***
# ****
# n = int(input())
# for i in range(n): # ilość wierszy
#   for j in range(i+1): # ilość kolumn
#     print("*", end="")
#   print()


# ****
# ***
# **
# *
# n = int(input())
# for i in range(n):
#   for j in range(n-i):
#     print("*", end="")
#   print()


#    *
#   **
#  ***
# ****
# n = int(input())
# for i in range(n):
#   for j in range(n-i-1):
#     print(" ", end="")
#   for k in range(n-i-1, n):
#     print("*", end="")
#   print()
  

# ****
#  ***
#   **
#    *
# n = int(input())
# for i in range(n):
#   for j in range(i):
#     print(" ", end="")
#   for k in range(i,n):
#     print("*", end="")
#   print()

# PRE (druga wersja)

# *
# **
# ***
# ****
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     if i >= j:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()

# ****
#  ***
#   **
#    *
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     if i <= j:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()

#    *
#   *
#  *
# *
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     if i+j == n-1 or i == n - j - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()

# ****
# ***
# **
# *
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     if i+j <= n - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()

#    *
#   **
#  ***
# ****
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     if i+j >= n - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# pass # Nie działa, ale nie ma błędu