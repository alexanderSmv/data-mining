import collections
import csv
import re
from gensim.parsing.preprocessing import remove_stopwords
import gensim
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from collections import  Counter
import  matplotlib.pyplot as plt
import  numpy as  np

gensim.parsing.preprocessing.STOPWORDS = {'a', 'the', 'to', 'in'}
all_stopwords = gensim.parsing.preprocessing.STOPWORDS

#['some sentence','else sentence']
spamList = []
hamList = []

#{'word':count}
arrWord_Spam = {}
arrWord_Ham = {}


porter = PorterStemmer()
lancaster = LancasterStemmer()
#привести слова к корню
def stemSentence(sentence):
    token_words = word_tokenize(sentence)
    token_words
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

#Посчитать к-во слов в массиве
def add_and_count(someList,outputArr):
    for item in someList:
        split_words = word_tokenize(item)
        for word in split_words:
            #print(word)
            if not  word in outputArr :
                outputArr[word] = 1
            else:
                outputArr[word] += 1
    return someList

def openFile_fillArrays():
    with open("sms-spam-corpus.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        i = 1
        for row in reader:
            i += 1


            if row['v1'] =='spam':
                spamList.append(stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower())))
            else:
                hamList.append(stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower())))
            # print(i, '|', row['v1'], '|', stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', row['v2'])).lower())))


    csvfile.close()

openFile_fillArrays()
add_and_count(spamList, arrWord_Spam)
add_and_count(hamList, arrWord_Ham)



# print(arrWord_Spam)
# print(arrWord_Ham)

# Сортировка слов по алфавиту
# tmp = collections.OrderedDict(sorted(arrWord_Spam.items()))
# print(tmp)

def fillSpamFile():#по алфавиту
    w = csv.writer(open("spam.csv", "w"))
    tmp = collections.OrderedDict(sorted(arrWord_Spam.items()))
    for key, val in tmp.items():
        w.writerow(['word: ', key, ' amount: ', val])

def fillHamFile():#дефолтный
    w = csv.writer(open("ham.csv", "w"))
    for key, val in arrWord_Ham.items():
        w.writerow(['word: ', key, ' amount: ', val])

fillHamFile()
fillSpamFile()
