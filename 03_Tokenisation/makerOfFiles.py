import sys

content = sys.stdin.readlines()

#store things
originalSentences = []
tokenisedSentences = []
uniqueForms = []


currentContent = []

for line in content:

	#if there's "# text = ", dump the content of the last sentence and grab the new sentence
	if "# text = " in line:
		tokenisedSentences.append(' '.join(currentContent))
		currentContent = []
		originalSentences.append(line[8:].strip())
		
	#if there's no tab, we don't care
	elif "\t" not in line:
		continue

	#grab the second colum, store the surface form and update the types
	else:
		surfaceForm = line.split("\t")[2]
		currentContent.append(surfaceForm)
		
		if surfaceForm not in uniqueForms:
			uniqueForms.append(surfaceForm)

#catch the last line
tokenisedSentences.append(' '.join(currentContent))

#write things :)
with open("original.txt", "w+") as origin:
	for line in originalSentences:
		if len(line.strip()) != 0:
			origin.write(line + "\n")


with open("tokenised.txt", "w+") as token:
	for line in tokenisedSentences:
		if len(line.strip()) != 0:
			token.write(line + "\n")

with open("dictionary.txt", "w+") as unique:
	for line in uniqueForms:
		if len(line.strip()) != 0:
			unique.write(line + "\n")

