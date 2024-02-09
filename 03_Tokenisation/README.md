Running the Model
---------------------------------------------------------------------------

Step 1: give your .conllu file to makerOfFiles.py
	
	cat <file name >.conllu | python3 makerOfFiles.py

This will make the original.txt and tokenised.txt files.



Step 2: create testing and training data

	head -<80%> original.txt > original.train.txt
	tail -<20%> original.txt > original.test.txt

	head -<80%> tokenised.txt > tokenised.train.txt
	tail -<20%> tokenised.txt > tokenised.test.txt

Find the percentages by finding the number of lines:
	
	cat original.txt | wc -l

and taking 80%/20% respectively




Step 3: create dictionary.txt

	cat tokenised.train.txt | gsed 's/ /\n/g' | sort | uniq > dictionary.txt



Step 4: run the model and store the tokenized sentences in predicted.tokenisation.txt 

	cat original.test.txt | python3 maxmatch.py > predicted.tokenisation.txt  



Step 5: evaluate the model with evaluate.py and save the results in model.results.txt
	
	pip install levenshtein
	python3 evaluate.py > model.results.txt


	
--------------------------------------------------------------------------------------------
Model Match Accuracy: 4%
------------------------------------------------------------------------------------------

If only exact matches are considered, the model didn't perform well. Looking at the mismatches, it seems that out of vocabulary (OOV)
items are the main problem.
 

	# text = 德國Obermarsberg具有歷史性的市政廳建於13世紀，並在三十年戰爭後進行了修補。
	# actual = 德國 Obermarsberg 具有 歷史性 的 市政廳 建 於 13 世紀 ， 並 在 三十 年 戰爭 後 進行 了 修補 。
	# predicted = 德國 O b e r m a r s b e r g 具有 歷史 性 的 市 政 廳 建 於 1 3 世紀 ， 並 在 三 十 年 戰爭 後 進行 了 修 補 。
	# match = no
	# percent correct = 88.28%

	# text = 在1933年國社黨的掌權後，各處都想贏回舊殖民地。	
	# actual = 在 1933 年 國社黨 的 掌權 後 ， 各處 都 想 贏回 舊殖民地 。
	# predicted = 在 19 33 年 國 社 黨 的 掌權 後 ， 各 處 都 想 贏 回 舊 殖民地 。
	# match = no
	# percent correct = 92.68%

	# text = 科朵拉·帕塞拉撤回了提供給西雅那銀行的報價，原因是“銀行對我們展現的怠慢態度”。
	# actual = 科朵拉 · 帕塞拉 撤回 了 提供 給 西雅那 銀行 的 報價 ， 原因 是 “ 銀行 對 我 展現 的 怠慢 態度 ” 。
	# predicted = 科 朵 拉 · 帕 塞 拉 撤 回 了 提供 給 西 雅 那 銀行 的 報 價 ， 原因 是 “ 銀行 對 我 們 展現 的 怠 慢 態度 ” 。
	# match = no
	# percent correct = 91.85%

maxMatch doesn't acount for OOV items, instead they are outputed as a series of one character words, (Obermarsberg -> O b e r m a r s b e r g, 科朵拉 -> 科 朵 拉). 
OOV items can also include numbers, (1933 -> 19 33).

----------------------------------------------------------------------------------------------------
Model Edit Distance Accuracy: 94.19%
---------------------------------------------------------------------------------------------------

Despite the model's poor match performance, if correctness in terms of edit distance is considered, the model is overall accurate.
Consider the following:

	# text = 他也表示，“這樣一份文件的存在可能會帶來讓人難以接受的後果。”
	# actual = 他 也 表示 ， “ 這樣 一 份 文件 的 存在 可能 會 帶來 讓 人 難 以 接受 的 後果 。 ”
	# predicted = 他 也 表示 ， “ 這樣 一 份 文 件 的 存在 可能 會 帶來 讓 人 難 以 接受 的 後果 。 ”
	# match = no
	# percent correct = 99.07%


	# text = 在課上，國際社會科學自由大學的學生被告知了一場在羅馬舉辦的會議。
	# actual = 在 課上 ， 國際 社會 科學 自由 大學 的 學生 被 告知 了 一 場 在 羅馬 舉辦 的 會議 。
	# predicted = 在 課 上 ， 國際 社會 科學 自由 大學 的 學生 被 告知 了 一 場 在 羅馬 舉辦 的 會議 。
	# match = no
	# percent correct = 99.05%


	# text = 審查處理了所有令人不快的言論；但也讓公共生活變得乎無法參與。
	# actual = 審查 處理 了 所有 令 人 不快 的 言論 ； 但 也 讓 公共 生活 變得 乎 無法 參與 。
	# predicted = 審查 處理 了 所有 令 人 不 快 的 言論 ； 但 也 讓 公共 生活 變得 乎 無法 參與 。
	# match = no
	# percent correct = 98.99%

All of these predicted tokenisations differ from the actual tokensations by only one decision. So, while the model is very poor at producing
matches, it largly tokenises correctly.  

-----------------------------------------------------------------------------------------------------------------------------
