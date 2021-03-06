#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

_list = [['Зима', ['12', '1', '2']], ['Весна', ['3', '4', '5']], ['Лето', ['6', '7', '8']],['Осень', ['9', '10', '11']]]
_dict = {'Зима': ['12', '1', '2'],'Весна': ['3', '4', '5'],'Лето': ['6', '7', '8'],'Осень': ['9', '10', '11']}

while True:
    m = input('Введите номер месяца: ')
    if m not in sum(_dict.values(), []):
        print('Неверный номер месяца. Введите еще раз')
        continue

    break

for s, n in _list:
    if m in n:
        print('В списоке, месяц с номером', m,'это', s)

for s, n in _dict.items():
    if m in n:
        print('В словарь, месяц с номером', m,'это', s)