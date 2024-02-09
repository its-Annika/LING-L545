Step 1: give your .conllu file to makerOfFiles.py
	
	cat x.conllu | python3 makerOfFiles.py

This will make the original.txt and tokenised.txt files.


Step 2: create testing and training data

	head -<80%> original.txt > original.train.txt
	tail -<20%> original.txt > original.test.txt

	head -<80%> tokenised.txt > tokenised.train.txt
	tail -<20%> tokenised.txt > tokenised.test.txt


Step 3: create dictionary.txt

	cat tokenised.train.txt | gsed 's/ /\n/g' | sort | uniq > dictionary.txt


Step 4: run the model and store the tokenized sentences in predicted.tokenisation.txt 

	cat original.train.txt | python3 maxmatch.py > predicted.tokenisation.txt 


Step 5: evaluate the model with evaluate.py and save the results in model.results.tsv

	python3 evaluate.py > model.results.tsv

	
