# link do strony: oki.org.pl
A = int(input())
B = int(input())

if (A + B) != 100:
  print("SKANDAL")
elif A > B:
  print("Bitek")
elif B > A:
  print("Bajtek")
else:
  print("Remis")