def poly(x, roots):

	P = 1

	for n in roots: 
		P *= (x - n)
	return P

def test_poly():

	assert(poly(2, [1, 1, 1])) == 1
	assert(poly(5, [2, 2])) == 9
	assert(poly(3, [1, 2, 3])) == 0
	assert(poly(8, [2, 4, 6])) == 48

test_poly()