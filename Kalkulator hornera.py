import math
coef = [] #współczynniki
dividers = [] #dzielniki
dividable = [] #podzielne
equations = [] #wyrazy
power = input("Input highest power besides 'x': ") #potęga

def get_super(x):
    normal = "0123456789"
    super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

def isint(arg, string):
    try:
        arg = int(arg)
        return arg
    except:
        while arg.isdigit() == False:
            print("Your input is not a number")
            arg = input(string)
        arg = int(arg)
        return arg

power = isint(power, "Input highest power besides 'x': " )

for i in range (0, power+1):
    if ((power)-i)>0:
        var = input(f"Input a number next to x{get_super(str((power)-i))} : ")
        var = isint(var, f"Input a number next to x{get_super(str((power)-i))} : ")
        coef.append(int(var))
    else:
        var = input("Input free expression: ")
        var = isint(var, "Input free expression: ")
        coef.append(int(var))

if coef[-1]>0:
    for i in range(1, coef[-1] + 1):
        if coef[-1]%i == 0:
            dividers.append(i)
            dividers.append(-i)
else:
    for i in range(1, (-1 * coef[-1]) + 1):
        if coef[-1]%i == 0:
            dividers.append(i)
            dividers.append(-i)

print(f"Dividers of a free expression are: {dividers}")
#add variable to determnine length of a list
l = 0
#check every object in dzielniki
for i in range(0, len(dividers)):
    #variable used for saving data
    a = dividers[i] * coef[0]
    #if first object besides the highest power is not equal to 1 then append it as a number
    if coef[0]!=1:
        equations.append(f"{coef[0]}x{get_super(str(power - 1))} ")
    #if it is -1 append it with a minus
    elif coef[0] == -1:
        equations.append(f"- {coef[0]}x{get_super(str(power - 1))} ")
    #if it is 1 the append it without the number
    else:
        equations.append(f"x{(get_super(str(power - 1)))} ")
    #check every combination for every divider
    for j in range(1, len(coef)):
        #save data in a
        a += coef[j]
        #check until last number
        if j < (len(coef) - 1):
            if j < (power-1):
                if ((power-1) - j) > 1:
                    if a!=0:
                        if a > 0:
                            equations.append(f"+ {a}x{(get_super(str((power - 1)-j)))} ")
                        elif a < 0:
                            equations.append(f"- {-a}x{get_super(str((power - 1) - j))} ")
                else:
                    if a!=0:
                        if a > 0:
                            equations.append(f"+ {a}x ")
                        elif a < 0:
                            equations.append(f"- {-a}x ")
            else:
                if a != 0:
                    if a > 0:
                        equations.append(f"+ {a}")
                    elif a<0:
                        equations.append(f"- {-a}")
            a = a * int(dividers[i])
        l += 1
        if l == len(coef)-1:
            if a == 0:
                dividable.append(dividers[i])
                l = 0
                if dividers[i]>0:
                    wyrazystr = "".join(str(element) for element in equations)
                    print(f"Final equation is: (x - {dividers[i]})*({wyrazystr})")
                else:
                    wyrazystr = "".join(str(element) for element in equations)
                    print(f"Final equation is: (x + {-dividers[i]})*({wyrazystr})")

                equations.clear()
            else:
                l = 0
                b=0
                equations.clear()

if dividable == []:
    print("Polynomial is not dividable by a whole number")
else:
    print(f"Polynomial is dividable by: {dividable}")