from SpringReaction import *

def Iterate(U, t, dt, x0, y0, l0, stiffness):
	sx, sy = Force(U[0], U[1], x0, y0, l0, stiffness)
	res = [0] * len(U)
	res[2] = U[0]
	res[3] = U[1]
	res[0] = 2 * U[0] - U[2] + (0 + sx) * dt**2
	res[1] = 2 * U[1] - U[3] - (9.8 + sy) * dt**2
	return res

def InitializeVerlet(x, y, vx, vy, dt):
	res = [0] * 4
	res[2] = x - vx * dt + 0
	res[3] = y - vy * dt - 9.8 * dt * dt / 2
	res[0] = x
	res[1] = y
	return res

if __name__ == "__main__":
	t = 0
	dt = 0.05
	vx = 1
	vy = 2
	
	x = 0
	y = 0

	x0 = -1
	y0 = 0
	l0 = 1
	stiffness = 2
	U = InitializeVerlet(x, y, vx, vy, dt)
	while(0 <= U[1]):
		U = Iterate(U, t, dt, x0, y0, l0, stiffness)
		print "t ", t, " U ", U
		t += dt
