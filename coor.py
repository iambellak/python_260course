a = 1
b = 5
n = 8            
h= float(b-a)/float(n)
List = []
for i in range(n+1):
	List.append(a+i*h)
print (List)