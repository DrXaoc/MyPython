#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
list = [500, 'Алексей', 88.5, False, -5546, True, 'Zadanie']
print(list)
for i in list:
    print(i, type(i))