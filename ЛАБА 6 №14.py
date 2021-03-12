"""
Розробити програму, яка вводить номер деякого року нашої ери і друкує
його назву по давньояпонському календарю."""
from enum import Enum
while True:
    try:
        year = int(input("year: "))
        if year < 0:
            print("enter year > 0 ")
        break
    except(ValueError, KeyError):
        print("enter only numbers")
class colour(Enum):
    Green = 1
    Red = 2
    Yellow = 3
    White = 4
    Black = 5
class animal(Enum):
    Mouse = 1
    Cow = 2
    Tiger = 3
    Rebbit = 4
    Dragon = 5
    Snake = 6
    Hourse = 7
    Sheep = 8
    Monkey = 9
    Chiken = 10
    Dog = 11
    Pig = 12
clear_years = year - 1984
age = clear_years % 60
c = age // 12
a = age % 12
print(colour(c + 1).name, animal(a + 1).name)

