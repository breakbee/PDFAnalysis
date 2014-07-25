### コーパスの作成
### 長さ2以上の名詞と未知語を特徴とする
### ストップワードは取り除く

import os
import re

### ストップワードのリスト
stopword = set()

### 日本語ストップワード
with open('../stopword/Japanese.txt', 'r', encoding='utf-8') as f:
	for line in f:
		word = line.rstrip('\n')
		stopword.add(word)


### 英語ストップワード
with open('../stopword/English.txt', 'r', encoding='utf-8') as f:
	for line in f:
		word = line.rstrip('\n')
		stopword.add(word)

### 正規表現
pattern = re.compile(r'[ぁ-んァ-ンー\u4e00-\u9FFF]+')

input_folder = "../tmp/process3/"
corpus_path = "../corpus/corpus.data"

### コーパスの作成
f_w = open(corpus_path, 'w', encoding='utf-8')
documents = os.listdir(input_folder)
for doc in documents:

	if doc.startswith("."):
		continue

	input_path = input_folder + doc

	f_r = open(input_path, 'r', encoding='utf-8')

	reception_part = ["名詞", "未知語"]

	for line in f_r:

		line = line.rstrip('\n')
		token = line.split('_')
		if len(token) != 2:
			continue

		word = token[0]
		part = token[1]

		if part not in reception_part:
			continue
		if len(word) == 1:
			continue
		if word in stopword:
			continue

		for w in pattern.findall(word):
			f_w.write(w + " ") 

	f_r.close()
	
	f_w.write("\n")

f_w.close()