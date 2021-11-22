# 1
l = []
for i in range(1, 31):
    l.append(i**2)
print(l)
# 2
exam_st_date = (11, 12, 2014)
print(f"Exam date is: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}!")
# 3
s = input("Введіть окремі числа: ")
while "," in s:
    s = s.replace(",", " ")

s = s.split()
st = tuple(s)
print(s, st)
# 4
x = [1, 2, 3, 4]
y = [1, 5]

flag = False
for i in x:
    if flag is False:
        for j in y:
            if i == j:
                flag = True
                break
    else:
        break
if flag is True:
    print("Є однакові цінності")
else:
    print("Немає однакових цінностей")
# 5

l = [[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]
p = 0
for i in l:
    p += i[0]
    p -= i[1]
print(f"існує {p} сонями")
