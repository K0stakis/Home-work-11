# 1) Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати
# тільки обʼєкти класу int або float

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self.__x = value
        else:
            raise TypeError

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self.__y = value
        else:
            raise TypeError

    def __str__(self):
        return f'Point [{self.__x}:{self.__y}]'

point_1 = Point(2,8)
point_2 = Point(6,4)
point_3 = Point(9,6)


# 2) Створіть класс Triangle (трикутник), який задається (ініціалізується) трьома точками
# (обʼєкти классу Point). Реалізуйте перевірку даних, аналогічно до класу Line. Визначет метод,
# що містить площу трикутника.

class Line:
    _begin = None
    _end = None
    def begin_getter(self):
        return self._begin

    def begin_setter(self, value):
        if isinstance(value, Point):
            self._begin = value
        else:
            raise TypeError

    begin = property(begin_getter, begin_setter)

    def end_getter(self):
        return self._end

    def end_setter(self, value):
        if isinstance(value, Point):
            self._end = value
        else:
            raise TypeError

    end = property(end_getter, end_setter)

    def __init__(self, point1, point2):
        self.begin = point1
        self.end = point2

    @property
    def length(self):
        diffx = self.begin.x - self.end.x
        diffy = self.begin.y - self.end.y
        return (diffx ** 2 + diffy ** 2) ** 0.5

    @length.setter
    def length(self, value):
        raise NotImplementedError

line_1 = Line(point_1, point_2)
line_2 = Line(point_2, point_3)
line_3 = Line(point_3, point_1)


class Triangle:
    def __init__(self, line1, line2, line3):
        if isinstance(line1, Line) and isinstance(line2, Line) and isinstance(line3, Line):
            self._line1 = line1
            self._line2 = line2
            self._line3 = line3
        else:
            raise TypeError

    @property
    def line1(self):
        return self._line1

    @line1.setter
    def line1(self, value):
        if not isinstance(value, Line):
            raise TypeError
        self._line1 = value

    @property
    def line2(self):
        return self._line2

    @line2.setter
    def line2(self, value):
        if not isinstance(value, Line):
            raise TypeError
        self._line2 = value

    @property
    def line3(self):
        return self._line3

    @line3.setter
    def line3(self, value):
        if not isinstance(value, Line):
            raise TypeError
        self._line3 = value

    def semi_perimeter(self):
        if line_1.end == line_2.begin and line_2.end == line_3.begin and line_3.end == line_1.begin:
            return (self.line1.length + self.line2.length + self.line3.length) / 2
        else:
            print("The ends of the lines do not match!")
            raise NameError
    def area(self):
        s = self.semi_perimeter()
        res = (s * (s - self.line1.length) * (s - self.line2.length) * (s - self.line3.length)) ** 0.5
        return res

    def __str__(self):
        return f"{self.area()}"

triangle1 = Triangle(line_1, line_2, line_3)
print(f"area --> {triangle1}")