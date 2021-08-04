# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_fu():
    a, b, c = map(int, input('Введите 3 числа через пробел:').strip().split())
    return sum(sorted((a, b, c), reverse=True)[:2])

print(my_fu())
