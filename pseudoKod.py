---Python
a = int(input())
b = int(input())
while a != b:
  if a > b:
    a -= b
  if b > a:
    b -= a
print(a)

a = int(input())
b = int(input())
while b > 0:
  temp = a
  a = b
  b = x % b
print(a)



---Pseudo
dopóki a =/ b
  jeżeli a>b
    a = a - b
  jeżeli b > a
    b = b - a
wypisz a

dopóki b > 0
    temp = a
    a = b
    b = temp mod b
wypisz a

Legenda:
=/ - przekreślony =
dopóki - while
jeżeli - if
wypisz - print
mod - modulo(%)
  
  
