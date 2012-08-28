import random

character_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

compare = "METHINKS I AM A WEASLE"

candidates = []
for a in range(0,100):
	candidates.append(
		"".join(
			[character_array[random.randint(0, 25)] for x in range(0, 21)]))

for x in range (0, 100):
	for index, candidate in enumerate(candidates):
		score = 0
		for i in range(0, len(candidate)):
			if (candidate[i] == compare[i]):
				score += 1
		print candidate, ": ", score

		if score == 0:
			candidates.remove(candidate)
		else:
			mutate = random.random() < .10
			for i in range(0, len(candidate)):
				if (mutate):
					candidate[i] == character_array[random.randint(0,25)]
					candidates.append(candidate)
				
			breed = random.random() < .30
			if breed:
				candidate_array = "".split(candidate)
				candidate_array[0:len(candidate)/2] = candidates[index-1][0:len(candidate)/2]
				candidates.append(candidate)
