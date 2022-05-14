from scipy.integrate import quad
from scipy import exp, pi, cos, sin, log, sqrt

def diff2(f, x, h = 1E-6):

	r = (f(x - h) - 2 * f(x) + f(x + h)) / (h ** 2)
	return r
	
def adaptive_trapezint(f, a, b, eps = 1E-5):

	ddf = []

	for i in range(101):
		ddf.apend(abs(diff2(f, a + i * (b - a) / 100)))
		max_ddf = max(ddf)
		h = sqrt(12 * eps) * 1 / sqrt((b - a) * max_ddf)
		n = (b - a) / h
		s = (f(a) + f(b)) / 2

		for i in range(1, int(n)):
			s += f(a + i * h)
			s *= h
	return s

def verify(f, a, b, n):

	exact = quad(f, a, b)[0]
	approx = adaptive_trapezint(f, a, b)
	error = abs(exact - approx)

print 'Exact integral of %s between %.5f and %.5f  = %.5f' % (f.__name__, a, b, exact)
print 'Approximate answer = %.5f \nError = %.5f\n' % (approx, error)

f1 = (cos, 0, pi)
f2 = (sin, 0, pi)
f3 = (sin, 0, pi / 2)

functions = [f1, f2, f3] 

for f in functions:
	verify(f[0], f[1], f[2], 10) 

