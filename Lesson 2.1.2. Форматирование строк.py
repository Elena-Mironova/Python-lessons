#! /usr/bin/env python
# -*- coding: utf-8 -*-

name = 'Leo'
age = 30
# 1. конкатенация
hello_str = 'Привет, ' + name + ' тебе ' + str(age) + ' лет'
print(hello_str)
# 2. %
hello_str = 'Привет %s тебе %d лет'%(name, age)
print(hello_str)
# 3. format
hello_str = 'Привет {} тебе {} лет'.format(name, age)
print(hello_str)

#задание
top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
# Поздравляем 1. ИВАНОВ 2. ПЕТРОВ 3. СИДОРОВ с успехом!
start = top5.find('1')
end = top5.find('4')

top3 = top5[start: end]

result = 'Поздравляем {} с успехом!'.format(top3.upper() )
print(result)