myint = []
for x in range(4):
    while True:
        try:
            myint.append(int(input(f"Ведіть ціле {x+1}-е число -\n")))
            break
        except:

            print("Не вірно")



myfloat = []
for b in range(2):
    while True:
        try:
            myfloat.append(float(input(f"Ведіть дійсне {b+1}-е число -\n")))
            break
        except:
             print("Не вірно")

myboolean = True
while True:
    try:
        myboolean = int(input("Введіть 0 або 1\n"))
        if myboolean == 1 or myboolean == 0:
            myboolean = bool(myboolean)
            break
        print("Не вірно")
        continue
    except:
        print("Неправильно")


for namber in myint:
    print(namber)
for namber in myfloat:
    print(namber)
for namber in  bool:
    print(namber)
#print(" x={0}; y={1}".format(x, y))

 #print(" x=%d; y=%d" % (x, y))
