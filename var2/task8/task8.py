"""
Создать новый двумерный массив элементов, развернув переданный массив вокруг главной диагонали (т.е. строки должны стать столбцами, а столбцы строками).
"""


def mirror_matrix(matrix: list) -> list:
	if not matrix or not matrix[0]:
		return [[]]
	#return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
	return list(map(list, zip(*matrix)))


if __name__ == '__main__':
	test_index = int(input("Введите номер теста: "))

	# input
	with open(f"input/input{test_index:02}.txt", 'r', encoding='utf-8') as file:
		data = list(map(lambda line: list(map(int, line.split())), file.readlines()))

	# task
	print("Входные данные:  " + str(data))
	data = mirror_matrix(data)
	print("Выходные данные: " + str(data))

	# output
	with open(f"output/output{test_index:02}.txt", 'w', encoding='utf-8') as file:
		file.write("\n".join(map(lambda row: " ".join(map(str, row)), data)))
