import RungeKutta
import Verlet

import matplotlib.pyplot as plt

if __name__ == "__main__":
	t = 0
	dt = input("dt: ")
	maxt = input("maxt: ")
	vx = input("vx: ")
	vy = input("vy: ")
	x = input("x: ")
	y = input("y: ")
	x0 = input("x0: ")
	y0 = input("y0: ")
	l0 = input("l0: ")
	stiffness = input("stiffness: ")
	Uv  = Verlet.InitializeVerlet(x, y, vx, vy, dt)
	Urk = RungeKutta.InitializeRungeKutta(x, y, vx, vy, dt)
	xrk = []
	yrk = []
	xv  = []
	yv  = []
	print "t ", 2 * vy / 9.8
	print "S ", 2 * vy / 9.8 * vx
	xrk.append(Urk[0])
	yrk.append(Urk[1])
	xv.append(Uv[0])
	yv.append(Uv[1])
	while(t < maxt):
		Uv = Verlet.Iterate(Uv, t, dt, x0, y0, l0, stiffness)
		Urk = RungeKutta.Iterate(Urk, t, dt, x0, y0, l0, stiffness)
		'''
		print "---------------"
		print "t ", t
		print "xRK ", Urk[0]
		print "yRK ", Urk[1]
		print "xV ", Uv[0]
		print "yV ", Uv[1]
		print "dx ", Urk[0] - Uv[0]
		print "dy ", Urk[1] - Uv[1]
		'''
	        xv.append(Uv[0])
		yv.append(Uv[1])
		xrk.append(Urk[0])
		yrk.append(Urk[1])
	        
		'''	
		k = str(raw_input());
		if '' != k:
			break
		'''
		
		t += dt

	t = range(len(xrk))
	plt.plot(t, xrk, label = r'$Ronge-Kutta: x(t)$')
	plt.hold(True)
	plt.plot(t, xv, label = r'$Verlet: x(t)$')
	plt.legend(loc = 'lower left')
	plt.hold(False)
	plt.show()
	
	plt.plot(t, yrk, label = r'$Ronge-Kutta: y(t)$')
	plt.hold(True)
	plt.plot(t, yv, label = r'$Verlet: y(t)$')
	plt.legend(loc = 'lower left')
	plt.hold(False)
	plt.show()
