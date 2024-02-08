Step 1: give your .conllu file to makerOfFiles.py
	
	cat x.conllu | python3 makerOfFiles.py

This will make the original.txt, tokenised.txt, and dictionary.txt files.


Step 2: creating testing and training data

	head -<80%> original.txt > original.train.txt
	tail -<20%> original.txt > original.test.txt
	head -<80%> tokenised.txt > tokenised.train.txt
        tail -<20%> tokenised.txt > tokenised.test.txt
