import math


def square(side):
    area = side ** 2
    return math.ceil(area)


side_length = float(input("Введите сторону квадрата: "))

area_result = square(side_length)

print(f"Площадь квадрата: {area_result}")
