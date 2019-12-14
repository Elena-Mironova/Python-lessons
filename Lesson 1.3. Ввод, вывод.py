# строка целиком
#print('Привет, меня зовут Кеша мне 2 года')
# у нас есть две переменные
# name = 'Кеша'
# age = 2
# # как вывести строку вместе с переменными в терминал?
# print(name, age)
#
# # / (через Сепаратор)
# print(name, age, sep='/')
#
# # end
# print(name)
# print(age)
#
# print('-------------------->')
# print(name, end=';')
# print(age, end=';')
# print('end', end=';')


##ввод данных
#result = input()
#print('Пользователь ввел', result)

# name = input('Как вас зовут?: ')
# print(type (name))
# age = input('Сколько вам лет?: ')
# print(type (age))
# is_love = input('Вы любите python&?: ')
# print(type(is_love))

age = int (input('Сколько вам лет?: '))
period = 20

age_period = age + period
print('Через', period, 'вам будет', age_period)