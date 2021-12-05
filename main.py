# 1
x = []
for i in range(1, 31):
    x.append(i**2)
print(x)
# 2
a = int(input())
b = int(input())
c = int(input())
exam_st_date = (a, b, c)
print(f"Дата іспиту: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")
# 3
a = input("Введіть відокремлені числа: ")
while "," in a:
    a = a.replace(",", " ")

a = a.split()
b = tuple(a)
print(a, b)
# 4
x = [1, 2, 3, 4]
y = [1, 5]

banner = False
for i in x:
    if banner is False:
        for j in y:
            if i == j:
                banner = True
                break
    else:
        break
if banner is True:
    print("є ідентичні цінності")
else:
    print("немає однакових цінностей")
# 5
l = [[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]
voyager = 0
for i in l:
    voyager += i[0]
    voyager -= i[1]
print(f"There is {voyager} sleepyheads")
