Running the Model

Step 1: give your .conllu file to makerOfFiles.py
	
	cat <file name >.conllu | python3 makerOfFiles.py

This will make the original.txt and tokenised.txt files.


Step 2: create testing and training data

	head -<80%> original.txt > original.train.txt
	tail -<20%> original.txt > original.test.txt

	head -<80%> tokenised.txt > tokenised.train.txt
	tail -<20%> tokenised.txt > tokenised.test.txt


Step 3: create dictionary.txt

	cat tokenised.train.txt | gsed 's/ /\n/g' | sort | uniq > dictionary.txt


Step 4: run the model and store the tokenized sentences in predicted.tokenisation.txt 

	cat original.test.txt | python3 maxmatch.py > predicted.tokenisation.txt  


Step 5: evaluate the model with evaluate.py and save the results in model.results.txt
	
	pip install levenshtein
	python3 evaluate.py > model.results.txt

	
--------------------------------------------------------------------------------------------
Model Match Accuracy: 4%

If only exact matches are considered, the model didn't perform well. Looking at the mismatches, there are at least two reasons 
for this. 

Problem Area #1: Out of Vocabulary Items

	# text = 德國Obermarsberg具有歷史性的市政廳建於13世紀，並在三十年戰爭後進行了修補。
	# predicted = 德國 Obermarsberg 具有 歷史性 的 市政廳 建 於 13 世紀 ， 並 在 三十 年 戰爭 後 進行 了 修補 。
	# actual = 德國 O b e r m a r s b e r g 具有 歷史 性 的 市 政 廳 建 於 1 3 世紀 ， 並 在 三 十 年 戰爭 後 進行 了 修 補 。
	# match = no
	# percent correct = 88.28%

	# text = 在1933年國社黨的掌權後，各處都想贏回舊殖民地。	
	# predicted = 在 1933 年 國社黨 的 掌權 後 ， 各處 都 想 贏回 舊殖民地 。
	# actual = 在 19 33 年 國 社 黨 的 掌權 後 ， 各 處 都 想 贏 回 舊 殖民地 。
	# match = no
	# percent correct = 92.68%

maxMatch doesn't acount for OOV items, instead they are outputed as a series of one character words, (Obermarsberg -> O b e r m a r s b e r g). 
OOV items can also include numbers, (1933 -> 19 33).


Problem Area #2: Defaulting to the longest words possible

	# text = 迪希邦登堡修道院被解散，後因宗教改革而變為廢墟。
	# predicted = 迪希邦登堡 修道院 被 解散 ， 後 因 宗教 改革 而 變 為 廢墟 。
	# actual = 迪 希 邦 登 堡 修 道 院 被 解 散 ， 後 因 宗教 改革 而 變 為 廢 墟 。
	# match = no
	# percent correct = 90.24%


	# text = 他也討論了布宜諾斯艾利斯的聯邦化、商業條約的延續以及任命軍隊的新將軍的事宜。
	# predicted = 他 也 討論 了 布宜諾斯艾利斯 的 聯邦化 、 商業 條約 的 延續 以及 任命 軍隊 的 新將軍 的 事宜 。
	# actual = 他 也 討論 了 布 宜 諾斯 艾 利 斯 的 聯邦 化 、 商業 條約 的 延 續 以及 任 命 軍隊 的 新 將軍 的 事 宜 。
	# match = no
	# percent correct = 91.94%

maxMatch defaults to the longest word possible, meaning that long words are prioritized, (迪希邦登堡 instead of 迪 希 邦 登 堡).
----------------------------------------------------------------------------------------------------
Model Edit Distance Accuracy: 94.19%

Despite the model's poor match performance, if correctness in terms of edit distance is considered, the model is overall accurate.
Consider the following:

	# text = 他也表示，“這樣一份文件的存在可能會帶來讓人難以接受的後果。”
	# predicted = 他 也 表示 ， “ 這樣 一 份 文件 的 存在 可能 會 帶來 讓 人 難 以 接受 的 後果 。 ”
	# actual = 他 也 表示 ， “ 這樣 一 份 文 件 的 存在 可能 會 帶來 讓 人 難 以 接受 的 後果 。 ”
	# match = no
	# percent correct = 99.07%


	# text = 在課上，國際社會科學自由大學的學生被告知了一場在羅馬舉辦的會議。
	# predicted = 在 課上 ， 國際 社會 科學 自由 大學 的 學生 被 告知 了 一 場 在 羅馬 舉辦 的 會議 。
	# actual = 在 課 上 ， 國際 社會 科學 自由 大學 的 學生 被 告知 了 一 場 在 羅馬 舉辦 的 會議 。
	# match = no
	# percent correct = 99.05%


	# text = 審查處理了所有令人不快的言論；但也讓公共生活變得乎無法參與。
	# predicted = 審查 處理 了 所有 令 人 不快 的 言論 ； 但 也 讓 公共 生活 變得 乎 無法 參與 。
	# actual = 審查 處理 了 所有 令 人 不 快 的 言論 ； 但 也 讓 公共 生活 變得 乎 無法 參與 。
	# match = no
	# percent correct = 98.99%

All of these predicted tokenisations differ from the actual tokensations by only one decision. So, while the model is very poor at producing
matches, it largly tokenises correctly.  

-----------------------------------------------------------------------------------------------------------------------------
