### pdf から抽出した文章に対して、日本語と区切り文字のみを抜き出す
### それをスペース/改行なしで結合する

import os
import re

input_folder = "../tmp/process1/"
output_folder = "../tmp/process2/"

# 正規表現
pattern = re.compile(r'[ぁ-んァ-ンー\u4e00-\u9FFF]+|[.,]+')

documents = os.listdir(input_folder)
for doc in documents:

	if doc.startswith("."):
		continue

	input_path = input_folder + doc
	output_path = output_folder + doc

	f_r = open(input_path, 'r', encoding='utf-8')
	f_w = open(output_path, 'w', encoding='utf-8')

	for line in f_r:
		line = line.rstrip('\n')
		tokens = line.split(' ')

		for word in tokens:
			for w in pattern.findall(word):
				f_w.write(w)
			
f_r.close()
f_w.close()
