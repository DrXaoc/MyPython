# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

file = open("text_05_005.txt", 'w', encoding='utf-8')
str_text = ('2  5  6  8  9  10  15  60  82')
file.writelines(str_text)
file.close()

with open('text_05_005.txt', 'r') as my_file:
    my_num = str_text.split()
    print(sum(map(int, my_num)))