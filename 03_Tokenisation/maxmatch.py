import sys

dict = []
with open ("dictionary.txt") as dicti:
	for line in dicti:
		dict.append(line.strip())

content = sys.stdin.readlines()




#but with tail recursion i think?

def maxMatch(sentence, progress):

        if len(sentence) == 0:
                return progress

        for i in range(len(sentence)-1, 0, -1):
                firstword = sentence[0:i+1]
                remainder = sentence[i+1:]

                if firstword in dict:
                        return maxMatch(remainder, progress + " " + firstword)


        firstword = sentence[0]
        remainder = sentence[1:]

        return maxMatch(remainder, progress + " " + firstword)




for line in content:
	print(maxMatch(line.strip(), ""))
