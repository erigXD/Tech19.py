# kod hufmana

W = "ABCCCDDDDDEFGGGHHIJJ"
E = "AB3C5DEF3G2HI2J"
H = ""

ilosc = 1
for i in range(len(W)-1):
  if W[i] == W[i+1]:
    ilosc += 1
  else:
    if ilosc > 1:
      H += str(ilosc)
    H += W[i]
    ilosc = 1
if ilosc > 1:
  H += str(ilosc)
  H += W[len(W)-1]

print(W)
print(H)





# pseudokod

W = "ABCCCDDDDDEFGGGHHIJJ"
E = "AB3C5DEF3G2HI2J"
H = ""

ilosc = 1
dla i w zakresie(len(W)-1)
  jeżeli W[i] = W[i+1]
    ilosc = ilosc + 1
  w przeciwnym razie
    jeżeli ilosc > 1
      H = H + W[i]
      ilosc = ilosc + 1
jeżeli ilosc > 1
  H = H + str(ilosc)
  H = H + W[len(W)-1]

wypisz(W)
wypisz(H)