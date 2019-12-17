import math
a = float(input('Введите а: '))
x = float(input('Введите х: '))
b = 0
i = 0
listG = []
listF = []
listY = []
listX = []
listA = []
count = int(input('Сколько считать? '))
m = float(input('Какой  шаг? '))
var = int(input('введи значение: '))

while count >= 0:
    if count == 0:
        con = str(input('продолжить счет:'))
        if con == 'да':
            count = int(input('Сколько считать? '))
            m = float(input('Какой  шаг? '))
        else:
                    print('Все!')
    if var == 1:
        for i in range(count):
            if (-(a*a)+a*x+6*x*x) == 0:
                print('Введены неверные данные')
            else:
                G = (-(10*(18*a*a+11*a*x-24*x*x))/(-(a*a)+a*x+6*x*x))
                listG.append(G)
                listX.append(x)
                listA.append(a)
                x+=m
                a+=m
    elif var == 2:
        for i in range(count):
            z = math.cos(21*a*a-34*a*x+9*x*x)
            if math.isclose(z,b,abs_tol=0.000001):
                print('Введены неверные данные')
            else:
            else:
                F = math.cos(21*a*a-34*a*x+9*x*x)
                listF.append(F)
                listX.append(x)
                listA.append(a)
                a+=m
                x+=m
    elif var == 3:
        for i in range(count):
            if (3*a*a-25*a*x+8*x*x+1) <= 0:
                print('Введены неверные данные')
            else:
                 Y = math.log(3*a*a-25*a*x+8*x*x+1)/math.log(10)
                 listY.append(Y)
                 listX.append(x)
                 listA.append(a)
                 x+=m
                 a+=m
    count -= 1

    if count == 0:
        vivod = str(input('Как выводить?(строка\таблица) '))
        if vivod == 'строка':
            if var == 1:
                 print(listG)
                 print('Максимальный в G:')
                 print(max(listG))
                 print('Минимальный в G:')
                 print(min(listG))
            if var == 2:
                 print(listF)
                 print('Максимальный в F:')
                 print(max(listF))
                 print('Минимальный в F:')
                 print(min(listF))
            else:
                 var == 3
                 print(listY)
                 print('Максимальный в Y:')
                 print(max(listY))
                 print('Минимальный в Y:')
                 print(min(listY))
else:
        mda = 0
        if var == 1:
            for i in listG:
                print('a = ' + str(listA[mda]) + ' x = ' + str(listX[mda]) + ' G = ' + str(listG[mda]))
                i += 1
                mda += 1
        if var == 2:
            for i in listF:
                print('a = ' + str(listA[mda]) + ' x = ' + str(listX[mda]) + ' F = ' + str(listF[mda]))
                i += 1
                mda += 1
        if var == 3:
            for i in listY:
                print('a = ' + str(listA[mda]) + ' x = ' + str(listX[mda]) + ' Y = ' + str(listY[mda]))
                i += 1
                mda += 1
