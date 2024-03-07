"""
Реализовать функции кодирования и декодирования текста циклическим сдвигом букв алфавита.
Величина сдвига передается вторым параметром в данные функции.
Например, если величина сдвига равна 2, то все буква А меняется В, Б – на Г, В – на Д, …, Ю – на А, Я – на Б.
Такая же логика действует для замены латинских букв. Меняться должны как прописные,
так и строчные буквы (при этом прописные буквы остаются прописными, а строчные – строчными).
Подсказка: в программе в виде строковой константы должен быть задан русский и латинский алфавит и все манипуляции
с текстом производятся работой с данной константой (ни в коем случае программа не должна содержать отдельные условные
операторы для замены каждой буквы).
"""

alphabets = [
    "abcdefghijklmnopqrstuvwxyz",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
]


def code_char(ch: str, k: int):
    global alphabets
    for alphabet in alphabets:
        if ch in alphabet:
            i = alphabet.index(ch)
            i = (i + k) % len(alphabet)
            return alphabet[i]

    return ch


def encrypt_text(text: str, k: int) -> str:
    return "".join(map(lambda ch: code_char(ch, k), text))


def decode_text(text: str, k: int) -> str:
    return "".join(map(lambda ch: code_char(ch, -k), text))


if __name__ == '__main__':
    test_index = int(input("Введите номер теста: "))

    # input
    with open(f"input/input{test_index:02}.txt", 'r', encoding='utf-8') as file:
        data = file.read()

    # task
    k = int(input("Введите сдвиг: "))
    print("\nВходные данные:\n" + str(data))
    data = encrypt_text(data, k)
    print("\nШифрованный текст:\n" + str(data))
    data = decode_text(data, k)
    print("\nДешифрованный текст:\n" + str(data))

    # output
    with open(f"output/output{test_index:02}.txt", 'w', encoding='utf-8') as file:
        file.write(data)
