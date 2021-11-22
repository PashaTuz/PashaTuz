# 1
for i in range(1, 10):
    print(i, end="")
print()
# 2
for i in range(9, 0, -1):
    print(i, end="")
print()
# 3
for i in range(5, 14, 2):
    print(i, end="")
print()
# 4
s = 0
while True:
    x = int(input())
    if x == 0:
        break
    s += x
print(s)
# 5
x = int(input())
rev = 0
while x > 0:
    rev *= 10
    rev += x % 10
    x = int(x // 10)
print(rev)
# 6
t = int(input())
f = 1
for i in range(1, t+1):
    f *= i
print(f"Factorial of {t} equals {f}")