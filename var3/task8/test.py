from unittest import TestCase

from var3.task8.RectangleUtils import are_collide
from var3.task8.Rectangle import Rectangle


class TestRectangleCollide(TestCase):
	def test_are_collide1(self):
		rect1 = Rectangle(0, 0, 10, 10)
		rect2 = Rectangle(0, 0, 10, 10)

		result = are_collide(rect1, rect2)
		expected = True
		self.assertEqual(expected, result)

	def test_are_collide2(self):
		rect1 = Rectangle(0, 0, 10, 10)
		rect2 = Rectangle(10, 10, 20, 20)

		result = are_collide(rect1, rect2)
		expected = False
		self.assertEqual(expected, result)

	def test_are_collide3(self):
		rect1 = Rectangle(0, 0, 10, 10)
		rect2 = Rectangle(3, 3, 6, 6)

		result = are_collide(rect1, rect2)
		expected = True
		self.assertEqual(expected, result)

	def test_are_collide4(self):
		rect1 = Rectangle(10, 10, 0, 0)
		rect2 = Rectangle(6, 6, 3, 3)

		result = are_collide(rect1, rect2)
		expected = True
		self.assertEqual(expected, result)
