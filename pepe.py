"""
Завдання №2
Дано цілі p та q. Вивести на екран всі дільники числа q, взаємно прості з 
p."""
p = int(input("Минимум: "))
q = int(input("Максимум: "))
a = []
for i in range(1,q+1):
    if q%i == 0:
        a.append(i)
b = []
for i in range(1,p+1):
    if p%i == 0:
        b.append(i)
b=set(b)
d= []
for i in range(len(a)):
    c = []
    for j in range(1,a[i]+1):
        if a[i]%j==0:
            c.append(j)
    c=set(c)
    
    if len(c & b) == 1:
        d.append(a[i])
print(d)
