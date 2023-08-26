import bs4 as bs
import urllib3
import regex
import nltk # npm install nltk
import requests # npm install requests
from bs4 import BeautifulSoup # npm install BeautifulSoup
from inscriptis import get_text # npm install inscriptis
from googletrans import Translator # npm install googletrans



#funcion para extraer texto de un archivo txt
def extraer_texto_txt(archivo):
    print("Extrayendo texto de archivo txt... " + archivo)
    with open(archivo, 'r', encoding="utf8") as f:
        texto = f.read()
    return texto
#C:\Users\Sena\Documents\GitHub\coursePythonIA\RESUMIR TEXTOS\text.txt
text = extraer_texto_txt("C:\\Users\\Sena\\Documents\\GitHub\\coursePythonIA\\RESUMIR TEXTOS\\text.txt")

print("#####################")

from nltk import word_tokenize, sent_tokenize

# removing Square Brackets and Extra Spaces
text = regex.sub(r'\[[0-9]*\]', ' ', text)
text = regex.sub(r'\s+', ' ', text)


formatted_text = regex.sub('[^a-zA-Z]', ' ', text)
formatted_text = regex.sub(r'\s+', ' ', formatted_text)


#nltk.download()
sentence_list = sent_tokenize(text)

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
            
            
maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    

sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]


import heapq

summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)