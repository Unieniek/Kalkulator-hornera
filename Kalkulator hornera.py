import math

wspolczyniki = []
dzielniki = []
podzielne = []
power = int(input("Wpisz najwyższą potęgę przy x: "))

for i in range (0, power+1):
    var = input(f"Wpisz współczynnik przy x do potęgi {i}: ")
    wspolczyniki.append(int(var))

print(wspolczyniki)
for i in range(1, wspolczyniki[0]):
    if wspolczyniki[0]%i == 0:
        dzielniki.append(i)
        dzielniki.append(-i)

print(dzielniki)
l = 1
for i in range(0, len(dzielniki)):
    a = dzielniki[i]*wspolczyniki[-1]
    for j in range(1, len(wspolczyniki)):
        a += wspolczyniki[j]
        a = a * dzielniki[i]
        l += 1
        if l == len(wspolczyniki):
            if a == 0:
                podzielne.append(a)
            else:
                print(f"jest niepodzielne przez: {dzielniki[i]}")
            
print(f"podzielne przez: {podzielne}")
