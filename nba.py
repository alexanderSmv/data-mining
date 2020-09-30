from nltk import word_tokenize
import re
import processingFile
from gensim.parsing.preprocessing import remove_stopwords

inputStr = input("Input sentence: ")
test_Str = processingFile.stemSentence(remove_stopwords((re.sub(r'[^a-zA-Z ]', r'', inputStr)).lower()))

# ['word1','word1'...] без повторов
ham_words = []
spam_words = []

# {'word':count}
ham_words_count = processingFile.arrWord_Ham
spam_words_count = processingFile.arrWord_Spam

# ['some text 1','some text 2'...]
ham_sentence = processingFile.hamList
spam_sentence = processingFile.spamList
print(spam_sentence)
print(ham_sentence)


amountOfHamSentence = len(ham_sentence)
amountOfSpamSentence = len(spam_sentence)
all_sentence = amountOfHamSentence + amountOfSpamSentence

for item in processingFile.arrWord_Ham:
    ham_words.append(item)
for item in processingFile.arrWord_Spam:
    spam_words.append(item)


P_Ham =  amountOfHamSentence / all_sentence
P_Spam =  amountOfSpamSentence / all_sentence
print("P(ham) =  ",P_Ham,"\nP(spam) = ",P_Spam)



bodyText = word_tokenize(test_Str)
# print(bodyText)


#из массива предложений
def getAllWords(arr):
    output = []
    for item in arr:
        tmp = word_tokenize(item)
        for item1 in tmp:
            output.append(item1)
    return output

print("amount of spam words: ",len(getAllWords(spam_sentence)))
print("amount of ham words: ",len(getAllWords(ham_sentence)))


# всего word1 в спам/хам делим на общее к-во слов


P_bodytext_ham = 1
P_bodytext_spam = 1

# для P(bodyText | spam)
for i in range(0,len(bodyText)):
    if(bodyText[i] in spam_words_count):
        P_word_i_spam = spam_words_count[bodyText[i]]/len(getAllWords(spam_sentence))#P(word1 | spam)
    else:
        if(bodyText[i] in ham_words_count):
            P_word_i_spam = (ham_words_count[bodyText[i]]+1)/(len(ham_sentence)+1)
        else:
            P_word_i_spam = 1/(len(ham_sentence)+1)

    P_bodytext_spam = P_bodytext_spam * P_word_i_spam


# для P(bodyText | ham)
for i in range(0,len(bodyText)):
    if(bodyText[i] in ham_words_count):
        P_word_i_ham = ham_words_count[bodyText[i]]/len(getAllWords(ham_sentence))#P(word1 | ham)
    else:
        if(bodyText[i] in spam_words_count):
            P_word_i_ham = (spam_words_count[bodyText[i]]+1)/(len(spam_sentence)+1)
        else:
            P_word_i_ham = 1/(len(spam_sentence)+1)

    P_bodytext_ham = P_bodytext_ham * P_word_i_ham

# print("P(bodyText | spam) = ",P_bodytext_spam)
# print("(P(spam) * P(bodyText | spam)) = ",P_Spam*P_bodytext_spam)
# print("-----")
# print("P(bodyText | ham) = ",P_bodytext_ham)
# print("(P(ham) * P(bodyText | ham)) = ",P_Ham*P_bodytext_ham)


if((P_Ham*P_bodytext_ham)<(P_Spam*P_bodytext_spam)):
    print("input sentence  is ham")
else:
    print("input sentence  is spam")

#tests round
# def toFixed(numObj, digits=0):
#     return f"{numObj:.{digits}f}"
#
# def getAmountOf00(number):
#     tmp = str(number)
#     return int(tmp[len(tmp)-2]+tmp[len(tmp)-1])
#
#
# print("ham  = ",toFixed(P_Ham*P_bodytext_ham,getAmountOf00(P_Ham*P_bodytext_ham)+5))
# print("spam = ",toFixed(P_Spam*P_bodytext_spam,getAmountOf00(P_Spam*P_bodytext_spam)+5))
