# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Зарплата': wage, 'Премия': bonus}

class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())

if __name__ == '__main__':
    me = Position('Алексей', 'Ковалев', 'Ведущий специалист', 25000, 5000)
    me2 = Position('Алексей', 'Ковалев', 'Начальник', 35000, 10000)

    print(me.get_full_name())
    print(me._income)
    print(f'ИТОГО: {me.get_total_income()}')
    print(me2.get_full_name())
    print(me2._income)
    print(f'ИТОГО: {me2.get_total_income()}')