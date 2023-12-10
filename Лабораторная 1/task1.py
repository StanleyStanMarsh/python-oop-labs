import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Dog:
    def __init__(self, name: str, age: int):
        """
        Инициализирует объект Dog с заданным именем и возрастом.

        Если значение age отрицательное, возраст устанавливается равным 1.

        :param name: Имя собаки.
        :param age: Возраст собаки.

        Пример:
        >>> dog = Dog("Buddy", 2)
        """
        if age < 0:
            self.age = 1
        else:
            self.age = age
        self.name = name
        self.hunger_level = 100

    def grow_up_by_year(self) -> None:
        """
        Увеличивает возраст собаки на один год.

        Пример:
        >>> dog = Dog("Buddy", 2)
        >>> dog.grow_up_by_year()
        """
        ...

    def feed(self, food_satiation: int) -> None:
        """
        Кормит собаку, снижая уровень ее голода на заданное количество food_satiation.

        :param food_satiation: Величина, на которую будет снижен уровень голода.

        Пример:
        >>> dog = Dog("Max", 3)
        >>> dog.feed(50)
        """
        ...

    def is_hungry(self) -> bool:
        """
        Проверяет, голодна ли собака, основываясь на ее уровне голода.

        :return: Истинно, если собака голодна (уровень голода > 0), ложно в противном случае.

        Пример:
        >>> dog = Dog("Charlie", 5)
        >>> dog.is_hungry()
        True
        """
        if self.hunger_level > 0:
            return True
        return False


class Candle:
    def __init__(self, flavor: str, color: str, height: int):
        """
        Инициализирует объект Candle с заданным вкусом, цветом и высотой.

        Если высота меньше 1, то высота устанавливается равной 1.

        :param flavor: Аромат свечи.
        :param color: Цвет свечи.
        :param height: Высота свечи.

        Пример:
        >>> candle = Candle("Vanilla", "White", 5)
        """
        self.flavor = flavor
        self.color = color
        if height < 1:
            self.height = 1
        else:
            self.height = height
        self.flame = True

    def light_up(self) -> None:
        """
        Функция делает свечу зажженной.

        Пример:
        >>> candle = Candle("Vanilla", "White", 5)
        >>> candle.light_up()
        """
        ...

    def put_out(self) -> None:
        """
        Функция делает свечу потушенной.

        Пример:
        >>> candle = Candle("Lavender", "Purple", 3)
        >>> candle.put_out()
        """
        ...

    def is_flaming(self) -> bool:
        """
        Проверяет горит ли сейчас свеча.

        :return: True if the candle is lit, False otherwise.

        Пример:
        >>> candle = Candle("Rose", "Red", 4)
        >>> candle.is_flaming()
        True
        """
        return self.flame


class Car:
    def __init__(self, color: str, model: str, year: int):
        """
        Инициализирует объект Car заданным цветом, моделью и годом выпуска.

        Если год не находится в пределах допустимого диапазона (с 1885 по 2023 год), год устанавливается равным 2000.

        :param color: Цвет машины.
        :param model: Модель машины.
        :param year: Год выпуска машины.

        Пример:
        >>> car = Car("Blue", "Tesla", 2022)
        """
        self.color = color
        self.model = model
        if year > 2023 or year < 1885:
            self.year = 2000
        else:
            self.year = year
        self.active_engine = False

    def start_engine(self) -> None:
        """
        Заводит двигатель машины.

        Пример:
        >>> car = Car("Blue", "Tesla", 2022)
        >>> car.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Глушит двигатель машины.

        Пример:
        >>> car = Car("Red", "Toyota", 2010)
        >>> car.stop_engine()
        """
        ...

    def repaint(self, new_color: str) -> None:
        """
        Функция изменяет цвет автомобиля.

        :param new_color: Новый цвет автомобиля.

        Пример:
        >>> car = Car("Silver", "BMW", 2015)
        >>> car.repaint("Black")
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
