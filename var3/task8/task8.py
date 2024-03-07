"""
Для набора прямоугольников, стороны которых параллельны OX и OY,заданных координатами 2-х диагональных вершин,
найти все прямоугольники, которые не перекрываются никакими другими прямоугольниками
(т.е. если вырезать прямоугольники нужного размера и раскладывать по координатам на листе бумаги,
то нужные прямоугольники не буду накладываться на другие прямоугольники, но могут касаться сторонами).
"""

from var3.task8.Rectangle import Rectangle
from var3.task8.RectangleUtils import are_collide


def get_collide_list(rectangles: list) -> list:
	"""
	:param rectangles: list of rectangles
	:return: list of bool, True means, that rectangle don't collide
	"""
	collide_list = [True for _ in range(len(rectangles))]
	for i in range(len(rectangles)):
		for j in range(i + 1, len(rectangles)):
			if are_collide(rectangles[i], rectangles[j]):
				collide_list[i] = False
				collide_list[j] = False

	return collide_list


if __name__ == '__main__':
	test_index = int(input("Введите номер теста: "))

	# input
	with open(f"input/input{test_index:02}.txt", 'r', encoding='utf-8') as file:
		data = list(map(lambda line: Rectangle(*map(int, line.split())), file.readlines()))

	# task
	print("Входные данные:  " + str(data))
	data = list(
		map(lambda pair: pair[1], filter(lambda pair: pair[0], zip(get_collide_list(data), data))))
	print("Выходные данные: " + str(data))

	# output
	with open(f"output/output{test_index:02}.txt", 'w', encoding='utf-8') as file:
		file.write("\n".join(map(str, data)))
