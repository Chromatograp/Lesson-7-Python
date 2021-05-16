print('Задание 1.')


class Matrix:
    def __init__(self, var_1, var_2):
        self.var_1 = var_1
        self.var_2 = var_2

    def __str__(self):
        """
        Цикл выводит построчно встроенные списки:
        :return: выводит результат.
        """
        return str('\n'.join(['\t'.join([str(n) for n in i]) for i in self.var_1]))

    def __add__(self):
        """
        Цикл выводит значения из каждого списка и вставляет в новый список, затем складывает каждое число результата:
        :return: построчно выводит значения, полученные в новой матрице.
        """
        new_matrix = [[0, 0], [0, 0]]

        for i in range(len(self.var_1)):
            for n in range(len(self.var_1[i])):
                new_matrix[i][n] = self.var_1[i][n] + self.var_2[i][n]
        return str('\n'.join(['\t'.join([str(n) for n in i]) for i in new_matrix]))


m1 = Matrix([[1, 5], [3, 9]], [[3, 4], [5, 8]])
print('Матрица')
print(m1.__str__())
print('Сумма двух заданных матриц')
print(m1.__add__())
