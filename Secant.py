from math import *
import matplotlib.pyplot as mp
import numpy as np

def s_method(f, Xn_2, Xn_1, epsilon = 1.0e-7, N = 100, store = False):
	fn_Xn_2 = f(Xn_2)
	fn_Xn_1 = f(Xn_1)
	n = 2

if store:
	info = [(Xn_1, fn_Xn_1)]
while abs(fn_Xn_1) > epsilon and n < N:
	Xn = Xn_1 - float(fn_Xn_1) * (Xn_1 - Xn_2) \
	/ (fn_Xn_1 - fn_Xn_2)
	Xn_2 = Xn_1
	fn_Xn_2 = f(Xn_2)
	Xn_1 = Xn
	fn_Xn_1 = f(Xn_1)
	if store: 
		info.append((Xn_1, fn_Xn_1))
		n += 1
	if store:
		return Xn_1, info
	else:
		return Xn_1, n, fn_Xn_1

		def _Secant():
			f = lambda x: x**5 - sin(x)
			x0 = 1
			x1 = 2
			epsilon = 1.0e-15
			N = 100
			store = True
			x, info = s_method(f, x0, x1, epsilon, N, store)
			info = np.transpose(info)
			x_values = info[0]
			fn_values = info[1]			
			print('x**5 - sin(x)')
			for i in range(len(x_values)):
				print('Secant: ~[x: %s, f(x): %s, n: %d]' % (x_values[i], fn_values[i], i))
				mp.figure()
				mp.semilogy(fn_values, '-bo')
				mp.xlabel('Iteration Number')
				mp.ylabel('f(x)')
				mp.title('Secant method for x**5 - sin(x)')
				mp.show()
				if __name__ == '__main__':
					_Secant()










 