
#Написати програму, яка визначає значення кута в градусах
#(змінна corner) між станом годинникової стрілки на початку
#доби і її станом в hour годин, minute хвилин і second секунд
#(0 ≤ hour ≤ 11; 0 ≤ minute; second ≤ 59). 

hour=int(input('введите число '))
minute=int(input('введите число '))
second=int(input('введите число '))
x= 0.0083
second_all = hour*3600 + minute*60 + second
corner = second_all * x
if(0<=hour<=11)and(0<=minute<=59)and(0<=second<=59):
    x=0.0083
    second_all=hour*3600+minute*60+second
    corner = second_all * x
else:print('нужно вводить число ')
print(corner)
