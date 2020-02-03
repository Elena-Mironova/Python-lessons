import random
worlds_list = ('автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', 'шайба', 'олимпиада', 'снег')

secret_word = random.choice(worlds_list)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))
# immutable


while True:
    letter = input('введите ОДНУ русскую букву: ')
    if len(letter) != 1 or not letter.isalpha():
        continue
    print(letter)