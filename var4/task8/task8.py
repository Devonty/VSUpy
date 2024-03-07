lower_alf = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
upper_alf = set("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")


def is_start_with_upper(word: str):
    return word[0] in upper_alf and set(word[1:]) <= lower_alf


def f1(fio_parts: list) -> bool:
    flag = len(fio_parts) == 3

    for fio_part in fio_parts:
        flag = flag and is_start_with_upper(fio_part)

    return flag


def f2(fio_parts: list) -> bool:
    flag = len(fio_parts) == 2
    flag = flag and is_start_with_upper(fio_parts[0])
    flag = flag and fio_parts[1][1] == fio_parts[1][3] == '.'
    flag = flag and fio_parts[1][0] in upper_alf and fio_parts[1][2] in upper_alf
    return flag


def fio_filter(fio: str) -> bool:
    fio_parts = fio.split()
    return f1(fio_parts) or f2(fio_parts)


if __name__ == '__main__':
    test_index = int(input("Введите номер теста: "))

    # input
    with open(f"input/input{test_index:02}.txt", 'r', encoding='utf-8') as file:
        data = list(map(str.strip, file.readlines()))

    # task
    print("Входные данные:  " + str(data))
    data = list(filter(fio_filter, data))
    print("Выходные данные: " + str(data))

    # output
    with open(f"output/output{test_index:02}.txt", 'w', encoding='utf-8') as file:
        file.write("\n".join(map(str, data)))
