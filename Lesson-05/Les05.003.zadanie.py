# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
summa: int = 0
count: int = 0
persons = []
with open('text_05_003.txt', 'r', encoding='UTF-8') as my_file:
    for line in my_file:
        tokens = line.split()
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Сотрудники имеющие оклад менее 20000: {persons}")
print(f"Средняя величина дохода: {result}")