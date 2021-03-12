"""
Визначити значення змінної x, що позначає деяку довжину в одиницях p, замінити
величиною цієї ж довжини в метрах."""
from enum import Enum
class measure (Enum):
    decimetre = 1
    kilometre = 2
    metre = 3
    millimetre = 4
    centimetre = 5
while True:
    try:
        x = float(input('length:'))
        p = measure[input('measure:')]
        break
    except(ValueError, KeyError):
        print("введіть допустимі значення")
        
if p == measure(1):
    print("metres in decimetre", x/10)
if p == measure(2):
    print("metres in kilometre", x*1000)
if p == measure(3):
    print("x:", x)
if p == measure(4):
    print("metres in milimetre", x/1000)
if p == measure(5):
    print("metres in centimetre", x/100)

