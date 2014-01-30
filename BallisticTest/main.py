import RungeKutta
import Verlet

import matplotlib.pyplot as plt

if __name__ == "__main__":
	t = 0
	dt = input("dt: ")
	maxt = input("maxt: ")
	vx = 1
	vy = 2
	x = 0
	y = 0
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
		Uv = Verlet.Iterate(Uv, t, dt)
		Urk = RungeKutta.Iterate(Urk, t, dt)
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

	plt.plot(xrk, yrk, label = r'$Ronge-Kutta$')
	plt.hold(True)
	plt.plot(xv, yv, label = r'$Verlet$')
	plt.legend(loc = 'lower left')
	plt.hold(False)
	plt.show()
	
