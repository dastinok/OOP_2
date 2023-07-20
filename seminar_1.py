'''Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)'''
import datetime


class MyString(str):
    """Строка документации для класса my_string"""
    def __new__(cls, value, name):
        instance = super().__new__(cls,value)
        instance.name = name
        instance.date = datetime.datetime.now()
        return instance

    @staticmethod
    def __doc__():
        return """Строка документации для класса my_string"""

frs_str = MyString('dfgdfgdfg', 'autor')
print(frs_str.date)

str_st = MyString('dfg', 'sdfs')


help(str_st)


