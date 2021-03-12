
#Написати програму, яка визначає загальну кількість годин доби (змінна hour)
#і загальну кількість хвилин доби (змінна minute), які пройшли до моменту
#поточної секунди доби (змінна second). Наприклад, якщо second = 11111
#(second = 3 * 3600 + 5 * 60 + 11), то hour = 3 і minute = 5. 4

second=int(input("введите секунды "))
hour = second//3600
second=second-hour*3600
minutes = second//60
second = second % 60
print ('%d: %d: %d' % (hour, minutes, second))
