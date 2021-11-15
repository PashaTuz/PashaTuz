#1 задача
a = []
for x in range(4):
    while True:
        try:
            a.append(int(input(f"Ведіть ціле {x+1}-е число -\n")))
            break
        except:
            print("Не вірно")
            for namber in a:
                print(namber)
print(max(a))

#2 задача
year = int(input('Ведіть рік - '))
if year % 400 == 0:
     print('366')
elif year % 100 == 0:
     print('365')
elif year % 4 == 0:
     print('366')
else:
     print('365')

#3 задача
a =input()
b =input()
c =input()
if a + b > c:
    bool=True
if a + b < c:
    bool=False
import math
print()

#4 задача
for i in range(101):
    if not i % 7:
        continue
    print(i)
#5 задача
f = 1
n = int(input())
while n > 1:
     f = f * n
     n = n - 1
print(f)

#6 задача
width = int(input('ширина годинника: '))
side_height = width // 2

for i in range(0, side_height):
    line = "*" * (width - (i * 2))
    print(line.center(width))

print("*".center(width))

for i in range(1, side_height + 1):
    line = "*" * ((i * 2) + 1)
    print(line.center(width))
# 7задача
for num in range(1, 101):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            print(num)
            break



