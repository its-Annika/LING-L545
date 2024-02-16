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



Step 4: run the model and store the tokenized sentences in output.test.txt 

	cat original.test.txt | python maxmatch.py dictionary.txt > output.test.txt  



Step 5: evaluate the model with evaluate.Tyers.py and save the results in model.results.txt
	
	python3 evaluate.py tokenised.test.txt output.test.txt > model.results.txt
	
--------------------------------------------------------------------------------------------
# of Sentences = 200, WER = 50.84%
------------------------------------------------------------------------------------------

Overall, the model performed decently; not extremely well but also not extremely poor.  


The model did achieve a WER of 0% for 8/200 sentences, a few of which can be seen below.

	WER: 0.00%
	REF: 如果 他 的 民主黨 對手 競選 成功 了 ， 他 保證 她 會 “ 被 調查 很多 年 ” 。 
	HYP: 如果 他 的 民主黨 對手 競選 成功 了 ， 他 保證 她 會 “ 被 調查 很多 年 ” 。 
	EVA:


	WER: 0.00%
	REF: 從 20 世紀 60 年代 初 就 定居 下來 的 伊斯蘭 市民 主要 來 自 土耳其 。 	
	HYP: 從 20 世紀 60 年代 初 就 定居 下來 的 伊斯蘭 市民 主要 來 自 土耳其 。 
	EVA:   


	WER: 0.00%
	REF: 就 像 大 多數 南 歐 的 地點 一樣 ， 該 研究 可 追溯 到 早 至 公元 前 5 世紀 。 
	HYP: 就 像 大 多數 南 歐 的 地點 一樣 ， 該 研究 可 追溯 到 早 至 公元 前 5 世紀 。 
	EVA:  

	
	WER: 0.00%
	REF: 這 需要 評估 。 
	HYP: 這 需要 評估 。 
	EVA:

The sentences which were correctly predicted are on the shorter side, and likely don't contain any OOV items

 


The major issue for this model is OOV items.

A) Number/English-Word OOV Items 
	
	WER: 109.52%
	REF: 德國 Obermarsberg                       具有 歷史性   的 市政廳     建 於 13   世紀 ， 並 在 三十   年 戰爭 後 進行 了 修補   。 
	HYP: 德國 O            b e r m a r s b e r g 具有 歷史  性 的 市   政 廳 建 於 1  3 世紀 ， 並 在 三  十 年 戰爭 後 進行 了 修  補 。 
	EVA:    S            I I I I I I I I I I I    S   I   S   I I     S  I          S  I             S  I   


	WER: 54.76%
	REF: 蒂娜   · 安塞密爾       於 1927     年 3 月 25 日 出生   於 威尼托 自由堡        ； 她 在 一 個 反 法西斯     的 天主教 家庭 中 長大 ， 她 的 家庭 受 社會 主義 軍人   父親 被 迫害 的 經歷 的 影響 。 
	HYP: 蒂  娜 · 安    塞 密 爾 於 19   2 7 年 3 月 2  5 日出 生 於 威   尼   托 自由 堡 ； 她 在 一 個 反 法   西 斯 的 天主教 家庭 中 長大 ， 她 的 家庭 受 社會 主義 軍  人 父親 被 迫害 的 經歷 的 影響 。 
	EVA: S  I   S    I I I   S    I I       S  S S  I   S   S   I I  I             S   I I                                S  I                     


	WER: 105.00%
	REF: 和 許多 社會 主義 者   一樣 ， Pedro Sánchez                     在 Évole         項目 中 表示 西班牙 是 萬民   之 邦 。 
	HYP: 和 許多 社會    主義者 一樣 ， P     e       d r o S á n c h e z 在 É     v o l e 項目 中 表示 西班牙 是 萬  民 之 邦 。 
	EVA:         D  S        S     S       I I I I I I I I I I   S     I I I I               S  I 


maxMatch doesn't acount for OOV items (especially if they aren't Chinese characters), instead they are outputed as a series of one character words (Obermarsberg -> O b e r m a r s b e r g, 13 -> 1 3, 1927 -> 19 27, 25 -> 2 5).


B) Chinese OOV Items

	WER: 61.54%
	REF: 根據 流程   ， 她 將 會 在 23   點 45   分 講話   。 
	HYP: 根據 流  程 ， 她 將 會 在 2  3 點 4  5 分 講  話 。 
	EVA:    S  I

	
	WER: 66.67%
	REF: 後者 在 監督   共和黨 的 黨內 初選     ， 在 那 次 初選   中 瑞啟達     · 達利   對 尼古拉斯 · 薩科齊     表示 了 支持 。 
	HYP: 後者 在 監  督 共和黨 的 黨  內  初 選 ， 在 那 次 初  選 中 瑞   啟 達 · 達  利 對 尼古拉斯 · 薩   科 齊 表示 了 支持 。 
	EVA:      S  I       S  S  I I         S  I   S   I I   S  I          S   I I           

	
	WER: 62.50%
	REF: 在 這 條 信息 裡 ， 前司法部       部長 譴責 布里斯       · 奧爾特弗       是 一 個 “ 法西斯     分子 ” 、 “ 愚蠢 內政   部長 ” 和 一 個 ” 暴徒   “ 。 
	HYP: 在 這 條 信息 裡 ， 前    司 法 部 部長 譴  責   布 里 斯 · 奧    爾 特 弗 是 一 個 “ 法   西 斯 分子 ” 、 “ 愚蠢 內  政 部長 ” 和 一 個 ” 暴  徒 “ 。 
	EVA:              S    I I I    S  S   I I I   S    I I I         S   I I             S  I              S  I     

If a comination of characters doesn't appear in the dictionary, maxmatch outputs said characters individualy (流程 -> 流 程, 講話 -> 講 話, 監督-> 監 督, ...). If more than a few OOV items occur in the same sentence, the resulting WER is very high:

	WER: 111.11%
	REF: 費德里克      · 費里尼     曾經 說 過 ： “ 小丑 之於 人性       就 如同 影子 之於 常人         。 ” 
	HYP: 費    德里 克 · 費   里 尼 曾經 說 過 ： “ 小  丑  之  於 人 性 就 如  同  影  子  之 於 常 人 。 ” 
	EVA: S    I  I   S   I I            S  S  S  I I I   S  S  S  S  I I I I     

	費德里克 -> 費 德里 克
	費里尼 -> 費 里 尼
	小丑 -> 小 丑
	之於 -> 之 於
	人性 -> 人 性
	如同 -> 如 同
	影子 -> 影 子
	之於 -> 之 於
	常人 -> 常 人
 







