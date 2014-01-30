from math import sqrt
def Force(x, y, x0, y0, l0, stiffness):
	dx = x - x0
	dy = y - y0
	h = sqrt(dx**2 + dy**2)
	diff = l0 - h
	offx = (diff * dx / h) * stiffness
	offy = (diff * dy / h) * stiffness

	return (offx, offy)
