import time

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not((side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_c + side_b > side_a)):
            print("Треугольник с данными сторонами не существует")
            exit(1)

    def square_calculated(self):
        p = self.perimeter_calculated() / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** (0.5)

    def perimeter_calculated(self):
        return self.side_a + self.side_b + self.side_c

    def print_side(self):
        return f'Длинна стороны a: {self.side_a}\nДлинна стороны b: {self.side_b}\nДлинна стороны c: {self.side_c}\n'


tr = Triangle(4, 9, 6)
print(f'Площадь = {tr.square_calculated()}')
print(f'Периметр = {tr.perimeter_calculated()}')
print(tr.print_side())
