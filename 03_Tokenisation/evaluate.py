
from Levenshtein import ratio
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
percentageCorrect = 0
for i in range(totalPossible):

	match = "no"
	if re.match(results[i], target[i]):
		counter += 1
		match = "yes"

	correctRatio = ratio(results[i], target[i])
	percentageCorrect += correctRatio

	storage.append([originals[i],target[i],results[i],match, correctRatio])


for a, b, c, d, e  in storage:
	print("# text = " + a)
	print("# actual = " + b)
	print("# predicted = " + c)
	print("# match = " + d)
	print("# percent correct = %2.2f" %(e*100) + "%")
	print( "\n") 

print("percentage of correct matches: " + str((counter/totalPossible) * 100) + "%") 
print("overall correctness: %2.2f" %((percentageCorrect/totalPossible) * 100) + "%")
