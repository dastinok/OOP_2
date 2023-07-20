'''Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра'''

class Archive():
    """Строка документации для класса архив"""
    _instance = None
    count = 0
    archive_list = []

    def __new__(cls, name: str, number: int):
            if cls._instance is None:
                _instance = super().__new__(cls)


            return _instance

        #instance = super().__new__(cls, name, number)

        #instance.num_value = num_value
        #instance.str_value = str_value
        #instance.count_+=1
        #instance.old_instance = cls.instance if cls.instance.count_ == instance.count_ - 1




    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
        self.archive = Archive.archive_list
        self.archive_list.append((name, number))



arch_1 = Archive('eryt', 1)
arch_2 = Archive('bnmcx', 2)

print(Archive.archive_list)
help(arch_1)
