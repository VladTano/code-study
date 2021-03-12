
#Написати програму, яка за довжинами двох сторін деякого трикутника
#і кута (в градусах) між ними, знаходить довжину третьої сторони і
#площу цього трикутника.

import math
b = int(input('введите b '))
c = int(input('введите c '))
corner = int(input('введите угол '))
if (0<=corner<=360):
    a = math.sqrt((b**2) + (c**2) - 2 * b * c * math.cos(corner))
    print(a)
    p = (a + b + c)/3
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(S)

