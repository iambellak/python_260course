import numpy as np

def calc_poly(x,roots):

	p = 1

	for i in range(len(roots)):
		p *= (x - roots[i])
	return p
def test_poly(x,roots):
	p=1

	assert calc_poly(x, roots) == np.prod([p*(x-roots[i]) for i in range(len(roots))]), "Calculation is wrong"

def main():
	
	roots = [1,3,7]
	x = 4	
	
	p=1
	exp = np.prod([p*(x-roots[i]) for i in range(len(roots))])
	print("Expected polynomial :",exp)
	print("Polynomial calculated by the function :",calc_poly(x,roots))
    
	test_poly(x,roots)

main()
