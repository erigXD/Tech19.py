w = int(input())
k = int(input())
a = w
b = k
while b > 0:
  r = a%b
  a=b
  b=r
  # lub a, b = b, a % b
print(a) # NWD

print(w * k / a)

# WZÓR:
# a * b = NWD * NWW