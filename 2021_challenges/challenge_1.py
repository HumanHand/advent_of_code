count = 0

with open("input.txt") as input :
	for i in range(len(input)) :
		if count is 0 :
			print("Depth: " + i)
			count = 1
		if i > depths[i - 1] :
			print("Depth: " + i + " (Increased)")
		elif i < depths[i - 1] :
			print("Depth: " + i + " (Decreased)")
		else :
			print("Depth: " + i + " (No difference)")	
