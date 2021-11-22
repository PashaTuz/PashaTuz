# 1
s = input("input smthn з дужками: ")
t = ""
for i in range(0, len(s)):
    if s[i] == "'":
        t += '"'
    elif s[i] == '"':
        t += "'"
    else:
        t += s[i]
s = t
print(s)
# 2
s = input("input palindrome: ")
i, j = 0, len(s) - 1
flag = True  # Assuming word is a palindrome until proven wrong
t = s.lower()
while i < j and flag:
    if t[i] != t[j]:
        flag = False
        break
    i += 1
    j -= 1
print(flag)
# 3
s = input("input string розділити: ")
splitter = input("Input char для розділення: ")
res = []
while s.find(splitter) > -1:
    splitter_index = s.find(splitter)
    res.append(s[0:splitter_index])
    s = s[splitter_index+len(splitter):]  # Deleting string with splitter
res.append(s)
print(res)
# 4
s = input("введення послідовності слів: ")
first_index = 0
last_index = s.find(" ")
longest_word = s[first_index:last_index]
while last_index != -1:
    first_index += last_index + 1
    last_index = s[first_index:].find(" ")
    if len(s[first_index:first_index+last_index]) > len(longest_word):
        longest_word = s[first_index:first_index+last_index]
if len(s) - first_index > len(longest_word):
    longest_word = s[first_index:]
print(longest_word)
# 5
s = input("input integer: ")
res = 0
for i in s:
    if int(i) % 2 != 0:
        res += int(i)
print(res)
# 6
t = str(bin(int(s)))[2:]
res = 0
for i in t:
    res += int(i)
print(res)
# 7
directions = ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
n = 0
s = 0
w = 0
e = 0
for i in directions:
    if i == "NORTH":
        n += 1
    elif i == "SOUTH":
        s += 1
    elif i == "WEST":
        w += 1
    else:
        e += 1

x = abs(e-w)
y = abs(n-s)
if n > s:
    for i in range(0, s):
        directions.remove("NORTH")
        directions.remove("SOUTH")
else:
    for i in range(0, n):
        directions.remove("NORTH")
        directions.remove("SOUTH")

if e > w:
    for i in range(0, w):
        directions.remove("WEST")
        directions.remove("EAST")
else:
    for i in range(0, e):
        directions.remove("WEST")
        directions.remove("EAST")
print(directions)
# 8
w = ["", "b", "", "c"]
l = len(w)
r = []
for i in range(0, l):
    if w[i] == "":
        print("Пусто")
        break
    r.append(w[i])
    if i < l-1 and w[i+1] != "":
        if w[i][len(w[i])-1] != w[i+1][0]:
            break
print(r)
