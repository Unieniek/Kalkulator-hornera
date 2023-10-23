import math

wspolczyniki = []
dzielniki = []
podzielne = []
wyrazy = []
power = int(input("Wpisz najwyższą potęgę wielomianu: "))

for i in range (0, power+1):
    if ((power)-i)>0:
        var = input(f"Wpisz liczbę przy x^{(power)-i} : ")
        wspolczyniki.append(int(var))
    else:
        var = input(f"Wpisz wyraz wolny: ")
        wspolczyniki.append(int(var))

if wspolczyniki[-1]>0:
    for i in range(1, wspolczyniki[-1]+1):
        if wspolczyniki[-1]%i == 0:
            dzielniki.append(i)
            dzielniki.append(-i)
else:
    for i in range(1, (-1 * wspolczyniki[-1])+1):
        if wspolczyniki[-1]%i == 0:
            dzielniki.append(i)
            dzielniki.append(-i)


print(f"Dzielniki wyrazu wolnego to: {dzielniki}")
l = 0
for i in range(0, len(dzielniki)):
    a = dzielniki[i]*wspolczyniki[0]
    if wspolczyniki[0]!=1:
        wyrazy.append(f"{wspolczyniki[0]}x^{power-1}")
    else:
        wyrazy.append(f"x^{power-1}")
    for j in range(1, len(wspolczyniki)):
        a += wspolczyniki[j]
        if j < (len(wspolczyniki)-1):
            if j < (power-1):
                if ((power-1) - j) > 1:
                    if a!=0:
                        wyrazy.append(f"{a}x^{(power-1) - j}")
                else:
                    if a!=0:
                        wyrazy.append(f"{a}x")
            else:
                if a != 0:
                    wyrazy.append(f"{a}")
            a = a * int(dzielniki[i])
        l += 1
        if l == len(wspolczyniki)-1:
            if a == 0:
                podzielne.append(dzielniki[i])
                l = 0
                if dzielniki[i]>0:
                    wyrazystr = ") + (".join(str(element) for element in wyrazy)
                    print(f"Podzielność przez (x - {dzielniki[i]}): [({wyrazystr})]")
                else:
                    wyrazystr = ") + (".join(str(element) for element in wyrazy)
                    print(f"Podzielność przez (x + {-dzielniki[i]}): [({wyrazystr})]")

                wyrazy.clear()
            else:
                #print(f"jest niepodzielne przez: {dzielniki[i]}")
                l = 0
                b=0
                wyrazy.clear()

if podzielne == []:
    print("Wielomian jest niepodzielny przez liczbę całkowitą")
else:
    print(f"podzielne przez: {podzielne}")
