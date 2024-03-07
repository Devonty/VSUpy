from var3.task8.Rectangle import Rectangle


def are_collide(first: Rectangle, second: Rectangle) -> bool:
	x1 = max(first.x1, second.x1)
	x2 = min(first.x2, second.x2)
	y1 = max(first.y1, second.y1)
	y2 = min(first.y2, second.y2)
	return x1 < x2 and y1 < y2
