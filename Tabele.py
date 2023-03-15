from random import randint
l1 = ['Kuba', 'Kinga', 'Maurycy', 'Tymek', 'Eryk', 'Maternox', 'Marten', 'Jędrek', 'Patryk', 'Mikołaj', 'Pawłowski']
print("💗 MATCHMAKING 💗")
print()
for i in range(2):
  valuestr = randint(0, 10)
  print(l1[valuestr], end=" ")
print()
print()

for i in range(1):
  value = randint(0, 100)
  print(f"{value}%")