# # Цикл while
# # Задавать вопросы, пока пользователь не введет правильный ответ
# name = input('Кто создатель python? ')
# while name != 'Гвидо':
#     print('НЕ верно')
#     name = input('Кто создатель python? ')
# print('Верно')

# 1. Вывод чисел от 0 до 100
# 2. Вывод чисел от 0 до n
# 3. Вывод четных чисел от 0 до n
number = 0
# while number <= 100:
#     print(number)
#     #number = number + 1
#     number += 1
n = int(input('Введите n: '))
while number <= n:
    if number % 2 != 0:
        print(number)
    number += 1

