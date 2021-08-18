# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open('text_05_002.txt', encoding='UTF-8')
line = 0
for x in file:
    line += 1
    flag = 0
    word = 0
    for j in x:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0
    print('Строка ', line, '-', word, 'слова.')
print('Всего в файле ', line, 'строки.')
file.close()