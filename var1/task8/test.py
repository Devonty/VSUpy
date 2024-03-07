from unittest import TestCase
from var1.task8.task8 import reverse_min_max


class TestReverseMinMax(TestCase):
	def test_reverse_min_max1(self):
		data = [8, 8, 8, 1, 1, 1]
		expected = [8, 1, 1, 8, 8, 1]
		reverse_min_max(data)
		self.assertEqual(expected, data)

	def test_reverse_min_max2(self):
		data = [1, 2, 3, 4]
		expected = [1, 3, 2, 4]
		reverse_min_max(data)
		self.assertEqual(expected, data)

	def test_reverse_min_max3(self):
		data = [1, 1, 1, 8, 8, 8]
		expected = [1, 1, 1, 8, 8, 8]
		reverse_min_max(data)
		self.assertEqual(expected, data)

	def test_reverse_min_max4(self):
		data = [1, 5, 5, 6, 6, 9]
		expected = [1, 6, 6, 5, 5, 9]
		reverse_min_max(data)
		self.assertEqual(expected, data)

	def test_reverse_min_max5(self):
		data = [1, 1, 5, 5, 6, 6, 9, 9]
		expected = [1, 1, 6, 6, 5, 5, 9, 9]
		reverse_min_max(data)
		self.assertEqual(expected, data)

	def test_reverse_min_max_empty_check(self):
		data = []
		expected = []
		reverse_min_max(data)
		self.assertEqual(expected, data)
