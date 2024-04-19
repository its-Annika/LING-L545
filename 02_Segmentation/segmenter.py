import sys
import re

line = sys.stdin.readline()
	
while line: 

	tokens = line.strip().split(' ')
	
	#minimum sentence requirment = seubject + verb
	if len(tokens) < 2:
		tokens = []

	#if we've got a sentence-like thing

	for token in tokens:
	
		if not token:
			continue
		
		if token[-1] in '!?':
			sys.stdout.write(token + '\n')

		elif token[-1] == '.':

			#abreviations, elipsis, and initials 
			if token in ["D.C.", "ca.", "...", "Mio.", "St.", "Okd.", "No.", "Numbere"] or re.match("[A-Z][\.]", token):
				sys.stdout.write(token + ' ')

			#dates & numbers
			#if you've found a number, which is not a year
			elif re.match("[\.]*[1234567890][\.]*", token) and not re.match("[12][1234567890][1234567890][1234567890][\.]", token):
				sys.stdout.write(token + ' ')

			else:
				sys.stdout.write(token + '\n')
		else:
			sys.stdout.write(token + ' ')
	
	line = sys.stdin.readline()
