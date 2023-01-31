'''
THEORY

Часто вам потрібно підрахувати кількість елементів у певній послідовності. Для цього зручно скористатися словником.

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1
print(mark_counts)  # {4: 4, 2: 2, 6: 3, 7: 2, 3: 2, 5: 2, 1: 3}
Таке завдання зустрічається досить часто і, щоб не писати одні та ті ж самі 6 рядків коду постійно, у collections додали спеціальний словник Counter:

import collections

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})
Але на цьому корисні властивості Counter не закінчуються. Він може вивести елементи за частотою появи:

import collections

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
print(mark_counts.most_common(1))  # [(4, 4)]
print(mark_counts.most_common(2))  # [(4, 4), (6, 3)]
Ще Counter може відняти кількість елементів одного Counter від другого поелементно:

from collections import Counter

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)  # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})


'''

'''
Є список IP адрес:

IP = [
    "85.157.172.253",
    ...
]
Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, де ключ це IP, а значення – кількість входжень у вказаний список.

Приклад:

{
    '85.157.172.253': 2,
    ...
}
Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP і кількістю його появ в списку.

Пример:

('66.50.38.43', 4)

'''

from collections import Counter


def get_count_visits_from_ip(ips):
    count_ips = Counter(ips)
    return count_ips

def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]

print(get_count_visits_from_ip(['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114', '76.98.129.245', '66.50.38.43', '248.95.93.236', '173.37.214.238', '76.98.129.245', '76.98.129.245', '85.157.172.253', '66.50.38.43', '66.50.38.43', '66.50.38.43']))
print(get_frequent_visit_from_ip(['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114', '76.98.129.245', '66.50.38.43', '248.95.93.236', '173.37.214.238', '76.98.129.245', '76.98.129.245', '85.157.172.253', '66.50.38.43', '66.50.38.43', '66.50.38.43']))
