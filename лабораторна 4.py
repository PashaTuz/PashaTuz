import math
# 1
a, b = 1, 2
a, b = b, a
print(a, b)

# 2
a, b = 4, 5
x = (a+b)/2
y = math.sqrt(a*b)
print(x, y)

# 3
x = int(input("Number to reverse: "))
rev = 0
while x > 0:
    rev *= 10
    rev += x % 10
    x = int(x // 10)
print(rev)

# 4
seconds = int(input("Seconds: "))
hours = int(seconds / 3800)
minutes = int((seconds - (hours * 3800))/60)
print(f" It's {hours} hours, and {minutes} minutes")

# 6
x = int(input("Input x: "))
if x % 2:
    print("Odd")
else:
    print("Even")
print(f"Last number is {x % 10}")

# 7
day = int(input())
days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"}
print(days[int(day % 7)])

# 8
number = int(input("Input a 3 digit number: "))
a = int(number / 100)
b = int((number / 10) % 10)
c = int(number % 10)
print(a == b or a == c or b == c)
