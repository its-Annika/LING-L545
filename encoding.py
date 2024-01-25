#read in lines
import sys
lines = sys.stdin.readlines()
import unicodedata


#get regex
import re

#invalid storage
from collections import defaultdict
invalid = defaultdict(lambda:0)

#valid storage
valid = ""

for line in lines:
	
	#normalized the spaces
	cleanLine = ""
	for character in line:
		if unicodedata.category(character) == 'Fs':
			invalid[ord(character)] += 1
		elif unicodedata.category(character) == 'Zs' and character != " " and character != "\n":
			invalid[ord(character)] += 1
			cleanLine += " " 
		else:
			cleanLine += character

	#replaces invalid characters that are not spaces
	if re.search("[^a-zA-ZäÄöÖüÜß!;.?\"\'\s]", cleanLine):
		for character in cleanLine:
			if re.match("[^a-zA-ZäÄöÖüÜß!;.?\"\'\s]", character):
				invalid[character] += 1
		
			
	else:
		if not line.isspace() :
			valid += cleanLine	
	 
 
sys.stdout.write(valid)

for x in invalid.keys():
	sys.stderr.write(str(x) + "\t" + str(invalid[x]) + "\n")
