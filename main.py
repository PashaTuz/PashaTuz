# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Hello World-Привет мир')
print('Today we will count examples-Сегодгя мы считать примеры')
print('But for this we need to write a few codes-Но для етого нам нужно написать несколько кодов')
print('Well then lets start - Ну тогда начнем')
prodolzhit = 'y'
while prodolzhit == 'y':
    a_num = float(input("Первое число ="))
    oper = input("Введите операцыю = ")
    b_num = float(input("Второе число ="))
    if oper == '+':
        print(a_num + b_num)
    elif oper == '-':
        print(a_num - b_num)
    elif oper == '*':
        print(a_num * b_num)
    elif oper == '/':
        print(a_num / b_num)
    else:
        print('ERROR')
    prodolzhit = input('Ведите 'y' ,что бы продолжыть, или любую другуюклавишу,что бы завершыть')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
