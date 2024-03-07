from unittest import TestCase

from var2.task8.task8 import mirror_matrix


class TestMirrorMatrix(TestCase):
	def test_mirror_matrix1(self):
		data = [
			[1, 2, 3, 4],
			[1, 2, 3, 4],
			[1, 2, 3, 4],
		]
		data = mirror_matrix(data)

		expected = [
			[1, 1, 1],
			[2, 2, 2],
			[3, 3, 3],
			[4, 4, 4],
		]
		self.assertEqual(expected, data)

	def test_mirror_matrix2(self):
		data = [
			[1],
			[1],
			[1]
		]
		data = mirror_matrix(data)

		expected = [
			[1, 1, 1]
		]
		self.assertEqual(expected, data)

	def test_mirror_matrix3(self):
		data = [
			[1, 2],
			[3, 4]
		]
		data = mirror_matrix(data)

		expected = [
			[1, 3],
			[2, 4]
		]
		self.assertEqual(expected, data)

	def test_mirror_matrix_empty_check(self):
		data = [
			[]
		]
		data = mirror_matrix(data)

		expected = [
			[]
		]
		self.assertEqual(expected, data)