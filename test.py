
str = ''
spam = ['word1','word1','word2','word4','word4']
ham =  ['word1','word3','word3','word4','word4','word4','word4']

s_count ={'word1':2,'word2':1,'word4':2}
h_count = {'word1':1,'word3':2,'word4':4}

totalWords = 12
total_spam = 5
total_ham = 7

P_spam = total_spam / totalWords
print('P(spam) = ',P_spam)
P_ham = total_ham / totalWords
print('P(ham)  = ',P_ham)

#P(word|spam)
def P_word_spam(word):
    return s_count[word]/total_spam
print(P_word_spam("word4"))
print(P_word_spam("word2"))

def P_word(word):
    if word in h_count:
        return (s_count[word]+h_count[word])/totalWords
    else:
        return (s_count[word]) / totalWords
print(P_word("word4"))
print(P_word("word2"))
def P_spam_bodyText():
    return (P_word_spam('word4')*P_word_spam('word2')*P_spam)/(P_word('word4')*P_word('word2'))

print((P_word_spam('word4')*P_word_spam('word2')*P_spam )/ (P_word('word4')*P_word('word2')))
