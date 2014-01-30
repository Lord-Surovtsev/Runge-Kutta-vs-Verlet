from SpringReaction import *

def F(U, dt, x0, y0, l0, stiffness):
	sx, sy = Force(U[0], U[1], x0, y0, l0, stiffness)
	res = [0] * len(U)
	res[0] = U[2]
	res[1] = U[3]
	res[2] = 0 + sx
	res[3] = -9.8 + sy
	return res

def Mult(U, dt):
	res = [0] * len(U)
	for i in range(len(U)):
		res[i] = U[i] * dt
	return res

def Sum(U, dU):
	res = [U[i] + dU[i] for i in range(len(U))]
	return res


def Iterate(U, t, dt, x0, y0, l0, stiffness):
	k1 = Mult(F(U, t, x0, y0, l0, stiffness), dt)
	k2 = Mult(F(Sum(U, Mult(k1, 0.5)), t + 0.5 * dt, x0, y0, l0, stiffness), dt)
	k3 = Mult(F(Sum(U, Mult(k2, 0.5)), t + 0.5 * dt, x0, y0, l0, stiffness), dt)
	k4 = Mult(F(Sum(U, k3), t + dt, x0, y0, l0, stiffness), dt)

	res = [U[i] + 1.0/6.0 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(len(U))]
	return res

def InitializeRungeKutta(x, y, vx, vy, dt):
	res = [0] * 4
	res[0] = x
	res[1] = y
	res[2] = vx
	res[3] = vy
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
	U = InitializeRungeKutta(x, y, vx, vy, dt);
	
	while (0 <= U[1]):
		U = Iterate(U, t, dt, x0, y0, l0, stiffness);
		print "t ", t, " U ", U
		t += dt
