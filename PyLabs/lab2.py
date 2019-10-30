import math
a = float(input('Введите а: '))
x = float(input('Введите х: '))
b = 0
var = int(input('введи значение:'))
if var == 1:
    G = -(10*(18*a*a+11*a*x-24*x*x))/(-(a*a)+a*x+6*x*x)
    if (-(a*a)+a*x+6*x*x) == 0:
        print('Введены неверные данные')
    else:
        print(G)
elif var == 2:
    z = math.cos(21*a*a-34*a*x+9*x*x)
    if math.isclose(z,b,abs_tol=0.000001):
        print('Введены неверные данные')
    else:
        F = math.cos(21*a*a-34*a*x+9*x*x)
        print(F)
elif var == 3:
     if (3*a*a-25*a*x+8*x*x+1) <=0: 
        print('Введены неверные данные')
     else:	
        Y =math.log(3*a*a-25*a*x+8*x*x+1)/math.log(10)
        print(Y)
    
