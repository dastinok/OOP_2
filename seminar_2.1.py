
class Archive:
    _instance = None
    _archive = []

    def __new__(cls, name: str, age: int):
        instance = super().__new__(cls)
        if cls._instance:
            cls._archive.append(cls._instance)
        cls._instance = instance
        instance.archive = cls._archive
        return cls._instance

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Игро {self.name} ({self.age} лет). {[pl.name for pl in self.archive]}'

    def __repr__(self):
        return f'{self.name} {self.name}'

def main():
    player1 = Archive('Вут', 56)

    print(player1)

    player2 = Archive('Пип', 14)

    print(player2)

if __name__ == '__main__':
    main()