'''
Дуже часто люди у своїх повідомленнях не ставлять великі літери, особливо це стало масовим явищем в еру мобільних.
пристроїв. Розробіть функцію capital_text, яка прийматиме на вхід рядок з текстом і повертатиме рядок з відновленими
великими літерами.

Функція повинна:

зробити великою першу літеру в рядку, попри прогалини
зробити великою першу літеру після точки, попри прогалини
зробити великою першу літеру після знака оклику, попри прогалини
зробити великою першу літеру після знака питання, попри прогалини
'''

def capital_text(s):
    flag = None
    result = s
    for count in range(len(s)):
        if s[count] != ' ':
            result = result[0:count] + result[count].upper() + result[count + 1: len(result)]
            break
    for count in range(len(s)):
        if result[count] == "." or result[count] == "!" or result[count] == "?":
            flag = True
            continue
        if count < len(s) and result[count] == " " and flag == True:
            continue
        if flag == True:
            result = result[0:count] + result[count].upper() + result[count + 1: len(result)]
            flag = False

    return result

print (capital_text('ubv u. bv idf!fbi ibi?'))