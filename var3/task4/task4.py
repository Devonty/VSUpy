"""
Для набора точек на плоскости найти такие три точки,
для которых площадь треугольника с вершинами в данных точках будет максимальна.
В случае существования нескольких подходящих троек точек – выбрать произвольную.
"""


def get_square(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> float:
    # Sabc=1/2 |(x2 – x1)(y3 –y1) – (x3 – x1)(y2 – y1)|
    return abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2.


def get_points_max_square(points: list) -> tuple:
    result = None
    square_max = -1

    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for k in range(j + 1, len(points)):
                p1, p2, p3 = points[i], points[j], points[k]
                square_tmp = get_square(*p1, *p2, *p3)
                if square_max < square_tmp:
                    square_max = square_tmp
                    result = (p1, p2, p3)

    return result


if __name__ == '__main__':
    test_index = int(input("Введите номер теста: "))

    # input
    with open(f"input/input{test_index:02}.txt", 'r', encoding='utf-8') as file:
        data = list(map(lambda line: tuple(map(int, line.split())), file.readlines()))

    # task
    print("Входные данные:  " + str(data))
    data = get_points_max_square(data)
    print("Выходные данные: " + str(data))
    # Square
    if data:
        print("Square: " + str(get_square(*data[0], *data[1], *data[2])))

    # output
    with open(f"output/output{test_index:02}.txt", 'w', encoding='utf-8') as file:
        file.write("\n".join(map(lambda p: str(p[0]) + " " + str(p[1]), data)))
