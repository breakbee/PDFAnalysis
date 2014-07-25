### pdfからテキストの抽出

import os
import subprocess

# フォルダは予め作っておくこと
input_folder = "../pdf/"
output_folder = "../tmp/process1/"

documents = os.listdir(input_folder)
for i, doc in enumerate(documents):

	if doc.startswith("."):
		continue

	input_path = input_folder + doc
	output_path = output_folder + str(i) + ".txt"

	commands = ["sh", "extract_text.sh", input_path, output_path]
	subprocess.call(commands)
