# 1
s = input()
print(len(s))
# 2
t = ""
if len(s) < 2:
    print()
else:
    for i in range(0, 2):
        t += s[i]
    for i in range(len(s)-2, len(s)):
        t += s[i]
    print(t)
# 3
t = s[1:]
c = s[0]
print(t.find(c))
while t.find(c) > -1:
    t = t.replace(c, "$")
print(c+t)
# 4

if len(s) % 4 == 0:
    t = ""
    for i in range(len(s)-1, -1, -1):
        t += s[i]
    print(t)
else:
    print("довжина не кратна 4")
# 5
s = input("Введіть послідовність слів за допомогою ', ': ")
w = s.split(", ")
w = set(w)
w = list(w)
w.sort()
print(w)
