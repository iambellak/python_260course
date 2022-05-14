q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

#to get 'a' => q[0][0]
print(q[0][0])


#to get ['d', 'e', 'f'] => q[1]
print(q[1])

# to get 'h' => q[-1][-1]
print(q[-1][-1])


# to get 'd' => q[1][0]
print(q[1][0])

# q[-1] means last list which is ['g', 'h']
print(q[-1][-2])

print()


for i in q:
	for j in range(len(i)):
		print i[j]