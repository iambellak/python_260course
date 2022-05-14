def count_pairs(dna, pair):
	count = 0
	for i in range(len(dna) - 1):
		if dna[i] == pair[0] and dna[i + 1] == pair[1]:
			count += 1
	return count

print(count_pairs('ACTGCTATCCAATT', 'AT'))

def count_substr(dna, string):
	count = 0
	for i in range(len(dna) - 1):
		if dna[i:i+len(string)] == string:
			count += 1
	return count

print(count_substr('ACGTTACGGAACG', 'ACG'))
