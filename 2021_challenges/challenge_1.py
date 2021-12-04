count = 0

with open("input.txt") as input :
	for i in range(len(input)) :
		if count is 0 :
			print("Depth: " + i)
			count = 1
			continue
		elif i > depths[i - 1] :
			change = "(Increased)"
		elif i < depths[i - 1] :
			chane = "(Decreased)"
		print("Depth: " + i + " " + change)
