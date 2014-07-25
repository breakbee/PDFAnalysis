PDFAnalysis
===========

Japanese PDF Analysis by LDA  

PDFファイルから日本語コーパスを作成し、LDAを用いて分析します。  

**require**:  
Python(>3)  
Java(>1.6)  
sh  
mecab  

**library & require files**  
[Apache PDFBox (pdfbox-app-x.x.x.jar)](https://pdfbox.apache.org/)  
[日本語ストップワード (Japanese.txt)](http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt)  
[英語ストップワード (English.txt)](http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/English.txt)  
[LDA4J (lda4j.jar)](https://github.com/breakbee/LDA4J)

次のようにディレクトリを構成してください。  

PDFAnalysis  
├── README.md  
├── corpus  
├── jar  
│   ├── lda4j.jar  
│   └── pdfbox-app-x.x.x.jar  
├── pdf  
├── results  
├── scripts  
│   ├── analysis.sh  
│   ├── extract_text.py  
│   ├── extract_text.sh  
│   ├── filter_ja.py  
│   ├── make_corpus.py  
│   ├── make_tmpdir.py  
│   ├── mecab_text.py  
│   ├── mecab_text.sh  
│   └── remove_tmpdir.py  
└── stopword  
    ├── English.txt  
    └── Japanese.txt  

分析したい日本語PDFファイルを pdf ディレクトリに、  
lda4j.jar と pdfbox-app-x.x.x.jar を jar ディレクトリに、  
日本語と英語のストップワードを stopword ディレクトリに配置してください。  

PDFBoxのバージョンに応じて extract_text.sh の pdfbox-app-x.x.x.jar を書き換えてください。(標準では1.8.6)  

corpus ディレクトリに日本語PDFファイルから作成したコーパスが、  
results ディレクトリにLDAの結果が作成されます。  

summary.txt に LDAの概要が、  
param_theta.csv にトピック分布のパラメータが、  
param_phi.csv に単語分布のパラメータが保存されています。  