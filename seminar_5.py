'''Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
'''

'''Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения'''

class Square:
    def __init__(self, lenght, width = None):
        self.lenght = lenght

        if width:
            self.width = width
        else:
            self.width = lenght


    def square(self):
        return self.lenght * self.width


    def perimiter(self):
        return (self.lenght + self.width) * 2

    def __add__(self, other):
        new_lenght = self.lenght + other.lenght
        new_width = self.width + other.width
        return Square(new_lenght, new_width)

    def __sub__(self, other):
        if self.lenght - other.lenght < 0 or self.width - other.width < 0:
            raise ValueError
        else:
            new_lenght = self.lenght - other.lenght
            new_width = self.width - other.width
            return Square(new_lenght, new_width)

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __lt__(self, other):
        return self.square() <= other.square()

    def __le__(self, other):
        return self.square() >= other.square()


square_1 = Square(10,6)
square_2 = Square(2,1)
square_3 = square_1 + square_2
square_4 = square_1 - square_2

print(square_3.perimiter())
print(square_4.perimiter())

print(square_1 > square_2)
print(square_1 < square_2)
print(square_1 == square_2)
print(square_1 != square_2)
print(square_1 >= square_2)
print(square_1 <= square_2)