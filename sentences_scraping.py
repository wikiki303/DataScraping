# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 23:38:54 2022

@author: milo
"""
import numpy as np
import requests
from bs4 import BeautifulSoup

error_words = []
result = []
word = ""

try:
    def get_sentences(url):
        sentences = []
        
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        page = requests.get(url, headers=headers)
    
        soup = BeautifulSoup(page.text, 'lxml')
    
        for e in soup.select('tr[class*="exv2row"]'):
            sentences.append(word + " || " + e.get_text().strip())
       
        return sentences
        
        
    f = open("vocabulary_1.txt", "r")
    for idx, x in enumerate(f):
        word = x.strip()
        print(idx, word)
        url = f'https://www.wordhippo.com/what-is/sentences-with-the-word/{word}.html'
        tmp_sentences = get_sentences(url)
        if not tmp_sentences:
            error_words.append(word)
            print(f'Empty: idx= {idx}, val= {word}')
        result = np.concatenate((result, tmp_sentences))


    with open('sentences_1.txt', 'w', encoding="utf-8") as f:
        f.writelines('\n'.join(result))
        
    if len(error_words) > 0:
        with open('error_words.txt', 'w', encoding="utf-8") as f:
            f.writelines('\n'.join(error_words))
    
except:
    print("============= An exception occurred ===============")

print("=================== finished ================")
