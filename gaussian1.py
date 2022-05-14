from math import pi, exp, sqrt

# name all of the values with the values that were given

m = 0

s = 2.0

x = 1.0

# list the formula for f

f = 1 / (sqrt(2 * pi) * s) * exp(-0.5 * ((x - m) / s) ** 2)

# print the solution
print "For m = %g and s = %g, f(%g) = %.12f" %(m, s, x, f)