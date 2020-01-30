# #break
# name = None
# while True:
#       name = input('Кто создатель python? ')
#       if name == 'Гвидо':
#           break
#       print('НЕ верно')
# print('Верно')

# # continue
# number = 0
# n = int(input('Введите n: '))
# while number <= n:
#     if number % 2 == 0:
#         number += 1
#         continue
#     print(number)
#     number += 1

#while-else
number = 0

while number <= 100:
    print(number)
    number += 1
    # if number == 33:
    #     break
else:
    print('else - end')
print('end')
