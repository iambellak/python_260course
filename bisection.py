import sys

def f(x):
	return 2*x - 3   

eps = 1E-5
a, b = 0, 10

fa = f(a)
if fa*f(b) > 0:
	print 'f(x) does not change sign in [%g,%g].' % (a, b)
	sys.exit(1)

i = 0   
while b-a > eps:
	i += 1
	m = (a + b)/2.0
	fm = f(m)
	if fa*fm <= 0:
		b = m  
	else:
		a = m 
		fa = fm
	print 'Iteration %d: interval=[%g, %g]' % (i, a, b)
    
x = m          
print 'The root is', x, 'found in', i, 'iterations'
print 'f(%g)=%g' % (x, f(x))
