# Обчислюємо факторіал числа n за допомогою рекурсії
# @param n – число, для якого треба розрахувати факторіал
# @return факторіал числа n
def factorial(n):
    if n < 2:
        return 1  # Базовий випадок
    else:
        return n * factorial(n - 1)  # Рекурсивний випадок


num = int(input("Введіть додатне ціле число: "))
result = factorial(num)
print(f"Факторіал числа {num} дорівнює {result}")