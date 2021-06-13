# 3. Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся вложенный список. Для объектов
# класса реализовать метод сложения и вычитания матриц, а также умножения, деления матрицы на число и user-friendly вывода
# матрицы на экран.
import random
class Matrix:

    def __init__(self, matrix):
        self.__matrix = matrix

    def __add__(self, other):
        mas = []
        for i in range(len(self.__matrix)):
            tmp = []
            for j in range(len(self.__matrix[0])):
                tmp.append(self.__matrix[i][j] + other.__matrix[i][j])
            mas.append(tmp)
        return Matrix(mas)

    def __sub__(self, other):
        mas = []
        for i in range(len(self.__matrix)):
            tmp = []
            for j in range(len(self.__matrix[0])):
                tmp.append(self.__matrix[i][j] - other.__matrix[i][j])
            mas.append(tmp)
        return Matrix(mas)

    def __mul__(self, num):
        mas = []
        for i in range(len(self.__matrix)):
            tmp = []
            for j in range(len(self.__matrix[0])):
                tmp.append(self.__matrix[i][j] * num)
            mas.append(tmp)
        return Matrix(mas)

    def __truediv__(self, num):
        mas = []
        for i in range(len(self.__matrix)):
            tmp = []
            for j in range(len(self.__matrix[0])):
                tmp.append(self.__matrix[i][j] / num)
            mas.append(tmp)
        return Matrix(mas)

    def show_matrix(self):
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[0])):
                print('%4d' % self.__matrix[i][j], end='')
            print()
        print()


arr = Matrix([[2, -3, 1], [5, 4, -2]])
mas = Matrix([[4, 0, -2], [0, 1, -8]])
arr.show_matrix()
mas.show_matrix()
a = arr.__add__(mas)
a.show_matrix()

