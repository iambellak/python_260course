def find_Nprimes(N):
	nums = range(2, N + 1)

	prime_set = []

	for p in range(len(nums)):
		if nums[p] != 0:
			prime_set.append(nums[p])
			for i in range(nums[p], N + 1, nums[p]):
				nums[i - 2] = 0
	return prime_set

print find_Nprimes(100)