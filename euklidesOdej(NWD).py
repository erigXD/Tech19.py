a = int(input())
b = int(input())

while a != b:
  if a < b:
    b = b - a
  elif a > b:
    a = a - b
    print(a)
    