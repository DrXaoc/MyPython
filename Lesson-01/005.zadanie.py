x = int(input('Введите выручку:'))
b = int(input('Введите издержки:'))
if x > b:
    print('Ваша рентабельность',x/b)
    i = int(input('Введите кол-во сотрудников:'))
    print('Прибыль на сотрудника',((x-b)/i))
elif a == b:
    print('Ваша фирма работает в',(b-x))
else:
    print('Ваша фирма убыточна на',(b-x))

