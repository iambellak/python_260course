from math import sin, cos, pi, sqrt

def pathlength(x, y):

	I = 0

	for i in range(1, len(x)):
	   dL_sq = (x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2
	   I += sqrt(dL_sq)
	return I

def points(n):

	x = [0.5 * cos(2 * pi * i/n) for i in range(n + 1)]
	y = [0.5 * sin(2 * pi * i/n) for i in range(n + 1)]
	return x, y

nlist = [2 ** k for k in range(2, 11)]

for i in nlist:
	x, y = points(i)
	approx = pathlength(x, y)

	print 'For %4d points on the circle, pi approximates to %.8f giving and error of %.8f' % (i, approx, pi - approx)