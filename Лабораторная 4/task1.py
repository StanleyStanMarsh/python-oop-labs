class GameObject:
    """Класс, описывающий абстрактный объект в компьютерной 2D игре"""
    def __init__(self, x: float, y: float):
        """
        Инициализирует игровой объект GameObject с заданными координатами.

        Так как в условной игре не предполагается произвольное изменение положения объектов,
        нужно оставить только возможность их передвигать относительно текущих координат,
        поэтому поля self._x и self._y обяъвляются protected.

        :param x: координата по оси x.
        :param y: координата по оси y.

        Пример:

        >>> obj = GameObject(1.1, 2.2)
        """
        self._x = x
        self._y = y
        self.visibility = True

    @property
    def x(self) -> float:
        """
        Возвращает координату x объекта.

        :return: координата по оси x.

        Пример:

        >>> obj = GameObject(1.1, 2.2)
        >>> obj.x
        1.1
        """
        return self._x

    @property
    def y(self) -> float:
        """
        Возвращает координату y объекта.

        :return: координата по оси y.

        Пример:

        >>> obj = GameObject(1.1, 2.2)
        >>> obj.y
        2.2
        """
        return self._y

    def move(self, x_increment: float, y_increment: float) -> None:
        """
        Перемещает объект на указанные приращения координат.

        :param x_increment: приращение по координате x.
        :param y_increment: приращение по координате y.

        Пример:

        >>> obj = GameObject(1.1, 2.2)
        >>> obj.move(1, 2)
        """
        self._x += x_increment
        self._y += y_increment

    def killed(self) -> None:
        """
        Устанавливает флаг видимости объекта в False.

        Пример:

        >>> obj = GameObject(1.1, 2.2)
        >>> obj.killed()
        """
        self.visibility = False

    def __repr__(self) -> str:
        """
        Показывает, как может быть инициализирован экземпляр.

        :return: строковое представление объекта для отладки.

        Пример:

        >>> obj = GameObject(1.1, 2.2)
        GameObject(x=1.1, y=2.2, visibility=True)
        """
        return f"GameObject(x={self.x}, y={self.y}, visibility={self.visibility})"

    def __str__(self) -> str:
        """
        Представление экземпляра, для удобного вопсриятия пользователем.

        :return: строковое представление объекта для пользователя.

        Пример:

        >>> obj = GameObject(1.1, 2.2)
        Игровой объект GameObject: (1.1, 2.2)
        """
        return f"Игровой объект {self.__class__.__name__}: ({self.x}, {self.y})"


class Player(GameObject):
    """Класс, наследующийся от класса GameObject, описывает объект игрока в компьютерной 2D игре"""
    def __init__(self, x: float, y: float, health: float, ammo: float):
        """
        Инициализирует игровой объект Player с заданными координатами, значением здоровья и боеприпасов.

        При инициализации вызывается конструктор базового класса GameObject

        :param x: координата по оси x.
        :param y: координата по оси y.
        :param health: значение здоровья игрока.
        :param ammo: значение количества боеприпасов игрока.

        Пример:

        >>> player = Player(1.1, 2.2, 100, 50)
        """
        super().__init__(x, y)
        self.health = health
        self.ammo = ammo

    def killed(self) -> None:
        """
        "Убивает" игрока. Метод отличается от метода базового класса тем, что также обнуляет
        шкалы здоровья и боеприпасов.

        Пример:

        >>> player = Player(1.1, 2.2, 100, 50)
        >>> player.killed()
        """
        self.visibility = False
        self.health = 0
        self.ammo = 0

    def __repr__(self) -> str:
        """
        Показывает, как может быть инициализирован экземпляр.

        :return: строковое представление объекта для отладки.

        Пример:

        >>> player = Player(1.1, 2.2, 100, 50)
        Player(x=1.1, y=2.2, health=100, ammo=50)
        """
        return f"Player(x={self.x}, y={self.y}, health={self.health}, ammo={self.ammo})"

    def __str__(self) -> str:
        """
        Представление экземпляра, для удобного вопсриятия пользователем.

        :return: строковое представление объекта для пользователя.

        Пример:

        >>> player = Player(1.1, 2.2, 100, 50)
        Игрок Player: (1.1, 2.2), здоровье: 100, боезапас: 50
        """
        return f"Игрок {self.__class__.__name__}: ({self.x}, {self.y}), здоровье: {self.health}," \
               f" боезапас: {self.ammo}"


if __name__ == "__main__":
    # Write your solution here

    obj = GameObject(1.1, 2.2)
    obj.killed()
    print(obj)

    player = Player(1.1, 2.2, 100, 50)
    player.move(4, 6)
    player.killed()
    print(player)
