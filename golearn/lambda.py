# 1 example
def normal_name(list_name):
    return list(map(lambda name: name.title(), list_name))

print(normal_name(["dan", "jane", "steve", "mike"]))

# 2 example
'''
Є список contacts, елементи якого - словники контактів наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Розробіть функцію get_emails, яка отримує у параметрі список list_contacts та повертає список,
який містить електронні адреси всіх контактів зі списку list_contacts. Використовуйте функцію map.


'''
def get_emails(list_contacts):
    return list(map(lambda mem: mem['email'], list_contacts))

# 3 example
'''
На початку четвертого модуля ми вирішували завдання виплат за комунальними платежами. 
Вони являли собою список payment з додатними та від'ємними значеннями. 
Створіть функцію positive_values та за допомогою функції filter відфільтруйте список payment за додатними значеннями,
 та поверніть його з функції.

payment = [100, -3, 400, 35, -100]
'''
def positive_values(list_payment):
    return list(filter(lambda pos: pos > 0, list_payment))

# 4 example
'''
Є список contacts, елементи якого - словники контактів наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Створіть функцію get_favorites(contacts), яка повертатиме список, який містить лише обрані контакти. 
Використовуйте при цьому функцію filter, щоб відфільтрувати по полю favorite лише обрані контакти.
'''
def get_favorites(contacts):
    return list(filter(lambda cont: cont['favorite'], contacts))

