friends = ['Max', 'Leo', 'Kate']

print(friends)

print(len(friends))

friends.append('Ron')
print(friends)
print(len(friends))

# Удаляем последний элемент в списке и выводим его на экран
print(friends.pop())
print(friends)

# очистить весь список
friends.clear()
print(friends)

friends = ['Max', 'Leo', 'Kate']
# удаление объекта из списка
friends.remove('Kate')
print(friends)
# удаление элемента по индексу
del friends[0]
print(friends)