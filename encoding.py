#read in lines
import sys
lines = sys.stdin.readlines()

#get regex
import re

#invalid storage
from collections import defaultdict
invalid = defaultdict(lambda:0)

#valid storage
valid = ""

for line in lines:

	if re.search("[^a-zA-ZäÄöÖüÜß!:;.?\"\'\s]", line):
		for character in line:
			if re.match("[^a-zA-ZäÄöÖüÜß!.?\"\']", character):
				invalid[character] += 1
			
	else:
		if not line.isspace() :
			valid += line
			print(line)	
	 
 
sys.stdout.write(valid)

for x  in invalid.keys():
	sys.stderr.write(x + "\t" + str(invalid[x]) + "\n")
