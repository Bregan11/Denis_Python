# Создание базового класса "Фигура" и его наследование для создания классов
# "Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
# такие как вычисление площади и периметра, а классы-наследники будут иметь
# специфичные методы и свойства.

class Shape:
    """
    Базовый класс для геометрических фигур.
    Определяет общие методы для вычисления площади и периметра,
    которые должны быть реализованы в классах-наследниках.
    """

    def calculate_area(self):
        """
        Абстрактный метод для вычисления площади фигуры.
        Должен быть переопределен в классах-наследниках.
        """
        raise NotImplementedError("Метод 'calculate_area' должен быть реализован в подклассе.")

    def calculate_perimeter(self):
        """
        Абстрактный метод для вычисления периметра фигуры.
        Должен быть переопределен в классах-наследниках.
        """
        raise NotImplementedError("Метод 'calculate_perimeter' должен быть реализован в подклассе.")

    def __str__(self):
        """
        Возвращает строковое представление фигуры.
        """
        return "Это общая геометрическая фигура."

class Square(Shape):
    """
    Класс, представляющий квадрат. Наследует от Shape.
    """

    def __init__(self, side):
        """
        Конструктор класса Square.
        :param side: Длина стороны квадрата (число).
        """
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("Длина стороны квадрата должна быть положительным числом.")
        self._side = side

    def calculate_area(self):
        """
        Вычисляет площадь квадрата.
        """
        return self._side * self._side

    def calculate_perimeter(self):
        """
        Вычисляет периметр квадрата.
        """
        return 4 * self._side

    def __str__(self):
        return f"Квадрат со стороной {self._side}"

class Rectangle(Shape):
    """
    Класс, представляющий прямоугольник. Наследует от Shape.
    """

    def __init__(self, length, width):
        """
        Конструктор класса Rectangle.
        :param length: Длина прямоугольника (число).
        :param width: Ширина прямоугольника (число).
        """
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина прямоугольника должна быть положительным числом.")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина прямоугольника должна быть положительным числом.")
        self._length = length
        self._width = width

    def calculate_area(self):
        """
        Вычисляет площадь прямоугольника.
        """
        return self._length * self._width

    def calculate_perimeter(self):
        """
        Вычисляет периметр прямоугольника.
        """
        return 2 * (self._length + self._width)

    def __str__(self):
        return f"Прямоугольник длиной {self._length} и шириной {self._width}"

class Circle(Shape):
    """
    Класс, представляющий круг. Наследует от Shape.
    """
    
    PI_APPROX = 3.14159

    def __init__(self, radius):
        """
        Конструктор класса Circle.
        :param radius: Радиус круга (число).
        """
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Радиус круга должен быть положительным числом.")
        self._radius = radius

    def calculate_area(self):
        """
        Вычисляет площадь круга.
        """
        return self.PI_APPROX * (self._radius * self._radius)

    def calculate_perimeter(self):
        """
        Вычисляет периметр (длину окружности) круга.
        """
        return 2 * self.PI_APPROX * self._radius

    def __str__(self):
        return f"Круг с радиусом {self._radius}"

# Пример использования классов
if __name__ == "__main__":
    try:
        # Создание экземпляров различных фигур
        square = Square(5)
        rectangle = Rectangle(4, 6)
        circle = Circle(3)

        # Вывод информации о фигурах
        print(square)
        print(f"Площадь: {square.calculate_area()}")
        print(f"Периметр: {square.calculate_perimeter()}\n")

        print(rectangle)
        print(f"Площадь: {rectangle.calculate_area()}")
        print(f"Периметр: {rectangle.calculate_perimeter()}\n")

        print(circle)
        print(f"Площадь: {circle.calculate_area():.2f}") # Округляем для красоты
        print(f"Периметр: {circle.calculate_perimeter():.2f}\n")

        # Пример полиморфизма: функция, работающая с любым объектом Shape
        def display_shape_characteristics(shape: Shape):
            """
            Выводит характеристики переданной фигуры.
            :param shape: Объект класса Shape или его наследника.
            """
            print(f"Характеристики: {shape}")
            try:
                print(f"  Площадь: {shape.calculate_area():.2f}")
                print(f"  Периметр: {shape.calculate_perimeter():.2f}")
            except NotImplementedError as e:
                print(f"  Ошибка: {e}")
            print("-" * 30)

        print("\n--- Демонстрация полиморфизма ---")
        display_shape_characteristics(square)
        display_shape_characteristics(rectangle)
        display_shape_characteristics(circle)

        # Попытка создать фигуру с некорректными данными
        # invalid_square = Square(-2) # Вызовет ValueError
        # invalid_circle = Circle(0) # Вызовет ValueError

        # Попытка создать экземпляр базового класса и вызвать абстрактный метод
        # generic_shape = Shape()
        # generic_shape.calculate_area() # Вызовет NotImplementedError

    except ValueError as e:
        print(f"Ошибка создания фигуры: {e}")
    except NotImplementedError as e:
        print(f"Ошибка реализации: {e}")
