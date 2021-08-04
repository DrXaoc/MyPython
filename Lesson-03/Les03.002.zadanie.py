#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def my_fu(name, surname, birth, city, email, tel):
    name = str(input('Введите имя:'))
    surname = str(input('Введите фамилию:'))
    birth = int(input('Введите год рождения:'))
    city = str(input('Введите город проживания:'))
    email = str(input('Введите электронный адрес:'))
    tel = int(input('Введите телефон:'))
    return(name, surname, birth, city, email, tel)
print(my_fu('name', 'surname', 'birth', 'city', 'email', 'tel'))