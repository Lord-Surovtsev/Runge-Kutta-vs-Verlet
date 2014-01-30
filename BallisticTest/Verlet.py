def Iterate(U, t, dt):
	res = [0] * len(U)
	res[2] = U[0]
	res[3] = U[1]
	res[0] = 2 * U[0] - U[2] + 0
	res[1] = 2 * U[1] - U[3] - 9.8 * dt * dt
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
	U = InitializeVerlet(x, y, vx, vy, dt)
	while(0 <= U[1]):
		U = Iterate(U, t, dt)
		print "t ", t, " U ", U
		t += dt
