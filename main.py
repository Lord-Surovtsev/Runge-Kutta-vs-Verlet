import RungeKutta
import Verlet

if __name__ == "__main__":
	t = 0
	dt = input("dt: ")
	vx = 1
	vy = 2
	x = 0
	y = 0
	Uv = Verlet.InitializeVerlet(x, y, vx, vy, dt)
	Urk = RungeKutta.InitializeRungeKutta(x, y, vx, vy, dt)
	while(1):
		k = str(raw_input());
		if '' != k:
			break

		Uv = Verlet.Iterate(Uv, t, dt)
		Urk = RungeKutta.Iterate(Urk, t, dt)

		print "---------------"
		print "t ", t
		print "xRK ", Urk[0]
		print "yRK ", Urk[1]
		print "xV ", Uv[0]
		print "yV ", Uv[1]
		print "dx ", Urk[0] - Uv[0]
		print "dy ", Urk[1] - Uv[1]
		t += dt

