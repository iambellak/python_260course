def newton(fn, x, tol = 0.0001, maxiter = 1000):
    for i in range(maxiter):
        xnew = x - fn[0](x)/fn[1](x)
        if abs(xnew - x) < tol: break
        x = xnew
    return xnew, i

y = [lambda x:2*x**3 - 9.5*x +7.5, lambda x: 6*x**2 - 9.5*x + 7.5, lambda x: 6*x**2 - 9.5]

x, n = newton(y, 5)
print('The root is: %f at %d iteration.' %(x, n))
print('The root is', x, 'found in', n, 'iterations')
