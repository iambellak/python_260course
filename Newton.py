from math import * 
import matplotlib.pyplot as mp
import numpy as np
import sys

def Newton(fn, x, df_dx, epsilon = 1.0E-7, N = 100, store = False):
	fn_Val = fn(x)
	n = 0

	if store: convergence = [(x, fn_Val)]
	while abs(fn_Val) > epsilon and n <= N:
		dfdx_Val = float(df_dx(x))
		if abs(dfdx_Val) < 1e-14:
			raise ValueError("Newton: fn'(%g)=%g" % (x, dfdx_Val))
			x = x - fn_Val/dfdx_Val
			n += 1
			fn_Val = fn(x)
			if store: convergence.append((x, fn_Val))
			if store:
				return x, convergence
			else:
				return x, n, fn_Val

				def Newton_plot(fn, x0, df_dx, xmin, xmax, epsilon = 1.0E-13):
					for i in x0:
						x, convergence = Newton(fn, i, df_dx, epsilon, N = 100, store = True)
						iterations = range(len(convergence))
						roots = [convergence[i][0] for i in iterations]
						mp.plot(iterations, roots, 'r-')
						if sys.argv[1] == 'case1' or sys.argv[1] == 'case2':
							mp.title('Convergence of x toward a root %g for x**6 * sin(pi * x)' % i)
						else:
							mp.title('Convergence of x toward a root %g' % x)
							mp.xlabel('Iterations')
							mp.ylabel('Root')
							mp.savefig("Roots_output%s.png" % i) 
							values = [abs(convergence[i][1]) for i in iterations] # |fn(x_n)|
							mp.figure()
							mp.plot(iterations, values, 'r-')
							if sys.argv[1] == 'case1' or sys.argv[1] == 'case2':
								mp.title('Convergence of fn(x) toward zero for x**6 sin(pi*x)')
							else:
								mp.title('Convergence of fn(x) toward zero')
								mp.xlabel('Iterations')
								mp.ylabel('abs(fn(x))')
								mp.savefig("Values_output%s.png" % i)
								mp.show()
								fig.show()
								import pprint;
								pprint.pprint(convergence)
								print()
								return x, convergence
				
								def sech(x):
									return 2*cosh(x) / (cosh(2 * x) + 1)

									def _test():
										fs = lambda x : x**6 * sin(pi*x) # #x**4 - 16 #x**5 - sin(x) #x - sin(x) #
										ds = lambda x : 6*x**5 * sin(pi*x) + x**6 * pi * cos(pi*x) #sech(x)**2 - 10*x**9 #4*x**3 #5*x**4 - cos(x) #1 - cos(x) #
										if sys.argv[1] == 'case1':
											x0 = np.sort([-2.6, -1.2, 1.5, 1.7, 0.6])
											xmin = min(x0)
											xmax = max(x0)
										elif sys.argv[1] == 'case2':
											x0 = np.sort([-2, -1, 0, 1, 2])
											xmin = min(x0)
											xmax = max(x0)
					
											def h(x):
												return x**6*sin(pi*x)

												def dh(x):
													return 6*x**5 * sin(pi*x) + x**6*pi*cos(pi*x)
													x, convergence = Newton_plot(h, x0, dh, xmin, xmax, epsilson = 1.0E-20)
													print ('finding root of x**6 * sin(pi*x) in [%s, %s]' % (xmin, xmax))
													import pprint;
													pprint.pprint(x)
													print()

													def main():
														if sys.argv[1] == 'case1' or sys.argv[1] == 'case2':
															_test()
															sys.exit(0)
														elif len(sys.argv) < 5:
															print ('usage tip: %s fn dfdx xmin xmax' % (sys.argv[0]))
															sys.exit(-1)
														else:
															fp = sys.argv[1]
															fn = eval('lambda x:' + fp)
															df_dx = eval('lamda x:' + sys.argv[2])
															xmin = float(sys.argv[3])
															xmax = float(sys.argv[4])
															x0 = np.sort([xmin, xmax])
															x, convergence = Newton_plot(fn, x0, df_dx, xmin, xmax, epsilon = 1.0E-7)
															print()
															print ('finding root of %s in [%s, %s]' % (fp, xmin, xmax))
															print()
															if _name_ == '_main_':
																main()
																
			
				