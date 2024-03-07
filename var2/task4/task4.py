"""
Создать новый двумерный массив, исключив из переданного массива совпадающие столбцы.
Совпадающие столбцы – столбцы, у которых все соответствующие элементы равны друз другу).
При формировании нового массива оставить только первый из каждого набора совпадающих столбцов.
"""


def unique_matrix(matrix: list) -> list:
    # rotate matrix to clear rows instead cols
    rotated_matrix = list(map(list, zip(*matrix)))
    #
    matrix_set = set()
    new_matrix = list()

    for row in rotated_matrix:
        str_row = str(row)
        # Skip duplicates
        if str_row in matrix_set:
            continue
        # Add to new matrix
        matrix_set.add(str_row)
        new_matrix.append(row)

    # rotate back
    new_matrix = list(map(list, zip(*new_matrix)))
    return new_matrix


if __name__ == '__main__':
    test_index = int(input("Введите номер теста: "))

    # input
    with open(f"input/input{test_index:02}.txt", 'r', encoding='utf-8') as file:
        data = list(map(lambda line: list(map(int, line.split())), file.readlines()))

    # task
    print("Входные данные:  " + str(data))
    data = unique_matrix(data)
    print("Выходные данные: " + str(data))

    # output
    with open(f"output/output{test_index:02}.txt", 'w', encoding='utf-8') as file:
        file.write("\n".join(map(lambda row: " ".join(map(str, row)), data)))
