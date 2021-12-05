# 1
a = input()
print(len(a))
t = ""
if len(a) < 2:
    print()
else:
    for i in range(0, 2):
        t += a[i]
    for i in range(len(a)-2, len(a)):
        t += a[i]
    print(t)
t = a[1:]
x = a[0]
print(t.find(x))
while t.find(x) > -1:
    t = t.replace(x, "!")
print(x+t)
if len(a) % 3 == 0:
    t = ""
    for i in range(len(a)-1, -1, -1):
        t += a[i]
    print(t)
else:
    print("довжина не кратна 3")
# 2
s = input("Введіть слова через ', ': ")
w = s.split(", ")
w = set(w)
w = list(w)
w.sort()
print(w)
