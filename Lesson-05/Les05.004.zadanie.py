# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file_new = []
with open('text_05_004.txt', 'r', encoding='UTF-8') as file_obj:
    for x in file_obj:
        x = x.split(' ', 1)
        file_new.append(rus[x[0]] + '  ' + x[1])
    print(file_new)

with open('text_05_004_new.txt', 'w', encoding='UTF-8') as file_obj_2:
    file_obj_2.writelines(file_new)