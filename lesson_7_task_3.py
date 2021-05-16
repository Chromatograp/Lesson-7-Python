print('Задание 3.')


class Cell:
    def __init__(self, mesh_1, mesh_2):
        self.mesh_1 = mesh_1
        self.mesh_2 = mesh_2

    def __add__(self):
        return self.mesh_1 + self.mesh_2

    def __sub__(self):
        """
        Функция определяет наибольшее из введенных значений и вычитает из него наименьшее.
        :return: Возвращает результат.
        """
        if self.mesh_1 > self.mesh_2:
            return self.mesh_1 - self.mesh_2
        elif self.mesh_1 < self.mesh_2:
            return self.mesh_2 - self.mesh_1
        else:
            return f'Значения равны нулю.'

    def __mul__(self):
        return self.mesh_1 * self.mesh_2

    def __truediv__(self):
        return self.mesh_1 // self.mesh_2

    def make_order(self):
        """
        Функция сначала создает строку из символов "*" согласно количеству ячеек, оставшихся после реализации
        функции деления при слиянии двух клеток, затем при помощи цикла делит полученную строку на отрезки по
        5 символов и приводит результат в виде отдельных рядов.
        """
        str = Cell.__truediv__(self) * '*'
        n = 5
        new_str = [str[i: i + n] for i in range(0, len(str), n)]
        for i in new_str:
            print(i)


c = Cell(int(input('Введите количество ячеек в клетке 1: ')), int(input('Введите количество ячеек в клетке 2: ')))
print('Число ячеек общей клетки:')
print(c.make_order())

