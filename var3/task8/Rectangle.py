class Rectangle(object):
	def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.normalize_points()

	def normalize_points(self):
		if self.x1 > self.x2:
			self.x1, self.x2 = self.x2, self.x1
		if self.y1 > self.y2:
			self.y1, self.y2 = self.y2, self.y1

	def __str__(self) -> str:
		return f"{self.x1} {self.y1} {self.x2} {self.y2}"

	def __repr__(self) -> str:
		return f"Rectangle({self.x1}, {self.y1}, {self.x2}, {self.y2})"

