

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

counter = 0
for i in range(totalPossible):

	match = "no"
	if re.match(results[i], target[i]):
		counter += 1
		match = "yes"
	
	
	storage.append([originals[i],target[i],results[i],match])



for a, b, c, d in storage:
	print("# text = " + a)
	print("# predicted = " + b)
	print("# actual = " + c)
	print("# match = " + d)
	print( "\n") 

print("percentage correct: " + str((counter/totalPossible) * 100) + "%" + "\t\t\t") 
