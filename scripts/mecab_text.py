### 形態素解析

import os
import subprocess

input_folder = "../tmp/process2/"
output_folder = "../tmp/process3/"

documents = os.listdir(input_folder)
for doc in documents:

	if doc.startswith("."):
		continue

	input_path = input_folder + doc
	output_path = output_folder + doc

	commands = ['sh', 'mecab_text.sh', input_path, output_path]
	subprocess.call(commands)
