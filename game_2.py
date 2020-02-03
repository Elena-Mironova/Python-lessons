import random
worlds_list = ('автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', 'шайба', 'олимпиада', 'снег')

secret_word = random.choice(worlds_list)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))
# immutable


errors_counter = 0
while True:
    letter = input('введите Одну русскую букву: ')
    if len(letter) != 1 or not letter.isalpha():
        continue

    if letter in secret_word:
        pass
    else:
        errors_counter += 1
        print('ошибок допущено:', errors_counter)
        if errors_counter == 8:
            print('вы проиграли ;(')
            break
    print(''.join(gamer_word))

print('пробуйте играть еще!')