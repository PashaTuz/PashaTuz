integer = []
real_numbers = []
string = ''
boolean = True
for i in range(1, 5):
    integer.append(int(input('Integer {}: '.format(i))))
for i in range(1, 3):
    real_numbers.append(float(input('Дійсне число-{}: '.format(i))))
string = input('Запишіть випадкове число:')
print('Next')
print('Відформатовані цілі числа:')
for number in integer:
    print('Integer: ', '%5.0f' % number)
print('Next')
print('Дійсні числа')
print('Числа з плаваючою крапкою')
for number in real_numbers:
    print('З плаваючою точкою: ', '{:9}'.format(number))
print('Числа з нерухомою точкою')
for number in real_numbers:
    print('Фіксована точка: ', f'{number:5.2f}')
print('Next')
print('Форматований рядок (3 символи в 1 рядку)')
for i in range(0, int(len(string)/3) + 1):
    print(string[i*3:(i*3 + 3)])
print('Next')
print('Логічне значення (True):')
print(boolean)
print('Next')