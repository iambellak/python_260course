from math import sin,pi

def f(t,T):
	if(0 < t < T/2):
		return 1
	elif(abs(t-T/2)<0.001):
		return 0
	else:
		return -1

def s(t,n,T):
	val=0.0
	for i in range(1,n+1):
		val+=sin(2*(2*i -1)*pi*t/T)/(2*i -1)
		return val*4/pi

for alpha in [0.01,0.25,0.49]:
	print ("For alpha =", alpha)
	t=alpha*2*pi
	for n in [1,3,5,10,30,100]:
		print("For N=", n, "Error is:", f(t,2*pi)-s(t,n,2*pi))

