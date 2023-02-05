# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:18:57 2022

@author: milo
"""

import requests
from bs4 import BeautifulSoup

try:
    url = "https://www.vocabulary.com/lists/154147"
    
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text, 'lxml')
    
    result = []
    [result.append(i["word"]) for i in soup.find_all("li", {"class" : "entry"})]
    
    with open('vocabulary1.txt', 'w', encoding="utf-8") as f:
        f.writelines('\n'.join(result))

except:
    print("============= An exception occurred ===============")

print("=================== finished ================")