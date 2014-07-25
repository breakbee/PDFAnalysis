#!/bin/sh
python make_tmpdir.py
python extract_text.py
python filter_ja.py
python mecab_text.py
python make_corpus.py
python remove_tmpdir.py

java -jar ../jar/lda4j.jar ../corpus/corpus.data 2 100 ../results/summary.txt ../results/param_theta.csv ../results/param_phi.csv