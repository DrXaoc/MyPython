#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_fu():
    try:
        delimoe = int(input('Введите делимое:'))
        delitel = int(input('Введите делитель:'))
    except ValueError:
        return
    if delitel == 0:
        print('На ноль делить нельзя!')
    else:
        rezultat = delimoe/delitel
        return rezultat
print(my_fu())