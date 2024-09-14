import math

def min_boxes(q):
    return math.ceil(q / 5)

num_q = int(input("Введите количество предметов: "))
print(f"Минимальное количество коробок: {min_boxes(num_q)}")