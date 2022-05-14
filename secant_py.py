def secant (x0, x1, n, fx):
	def f(x):
		f = eval(fx)
		return x**2 - 4

	for i in range(1, n):
		fx0 = f(x0)
		fx1 = f(x1)

		i = x0 - (fx0 / ( (fx0 - fx1) / (x0 - x1)))

		x0 = x1
		x1= i
		print('The root is', i, 'found in', n,'iterations')
secant(0, 10, 30,'x**2 - 4')