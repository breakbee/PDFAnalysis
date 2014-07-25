#!/bin/sh
mecab -F"%m_%f[0]\n" -U"%m_未知語\n" -E"\n" $1 > $2
nkf -w --overwrite $2