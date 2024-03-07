"""
Перевернуть числа в списке между первым максимальным элементом списка и последним минимальным, слева направо, например:

{ 2, 11, 8, 11, 2, 3, 2, 2, 6, 7, 2, 3, 5, 10 } → { 2, 11, 7, 6, 2, 2, 3, 2, 11, 8, 2, 3, 5, 10 }
"""


def reverse_min_max(nums: list) -> None:
	# index init
	index_min = 0
	index_max = 0

	# find min, max
	for i, num in enumerate(nums):
		if num <= nums[index_min]:
			index_min = i
		if num > nums[index_max]:
			index_max = i

	# borders check
	l, r = (index_min, index_max) if index_min < index_max else (index_max, index_min)

	# swap
	for deltaIndex in range(1, (r-l) // 2 + 1):
		nums[l + deltaIndex], nums[r - deltaIndex] = nums[r - deltaIndex], nums[l + deltaIndex]


if __name__ == '__main__':
	test_index = int(input("Введите номер теста: "))

	# input
	with open(f"input/input{test_index:02}.txt", 'r', encoding='utf-8') as file:
		data = list(map(int, file.readline().split()))

	# task
	print("Входные данные:  " + str(data))
	reverse_min_max(data)
	print("Выходные данные: " + str(data))

	# output
	with open(f"output/output{test_index:02}.txt", 'w', encoding='utf-8') as file:
		file.write(" ".join(map(str, data)))
