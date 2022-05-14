print '%12s %12s' %('Fahrenheit', 'Celsius')
print '---------------------------'

fp = open('file.txt', 'r')

fp.readline()
fp.readline()
fp.readline()

for line in fp:
	F = float(line.split()[2])
	C = (5 / 9.) * (F - 32)
	print '%12.4f %12.4f' %(F, C)
fp.close()
print '---------------------------'