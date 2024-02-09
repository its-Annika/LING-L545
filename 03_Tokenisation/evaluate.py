

import sys
import re

results = []
with open ("predicted.tokenisation.txt") as test:
	for line in test:
		results.append(line.strip())


target = []
with open ("tokenised.test.txt") as tar:
	for line in tar:
		target.append(line.strip())


originals = []
with open("original.test.txt") as org:
	for line in org:
		originals.append(line.strip())


totalPossible = len(originals)
storage = []

storage.append(["original","actual","predicted","match?"])


counter = 0
for i in range(totalPossible):

	match = "not a match"
	if re.match(results[i], target[i]):
		counter += 1
		match = "match"
	
	
	storage.append([originals[i],target[i],results[i],match])



for a, b, c, d in storage:
	print(a + "\t" + b + "\t" + c + "\t" + d) 

print("percentage correct: " + str((counter/totalPossible) * 100) + "%" + "\t\t\t") 
