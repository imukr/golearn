'''
Всі ви, можливо, стикалися з ребусами "Знайди слово". Вони існують як текстові варіанти, так і як програми для
мобільних додатків. Нагадаємо коротко суть ребуса. У великому квадраті з набором букв необхідно знайти слово по
горизонталі та інколи по вертикалі.

game
Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова,
що шукається в рядку ребуса.

Параметри функції:

riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у
зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.

'''


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    count = 0
    for char in riddle:
        if char == start_letter:
            if not reverse:
                return riddle[count:count + word_length]
            else:
                print(count)
                return riddle[count:count - word_length:-1]
        count += 1
    return ''
    print(riddle)
