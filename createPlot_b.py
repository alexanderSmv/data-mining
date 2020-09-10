from nltk import word_tokenize
import  matplotlib.pyplot as plt
import processingFile
#only sentence
arr_s = processingFile.spamList
arr_h = processingFile.hamList

#{'some text':count}
arrSentence_Spam={}
arrSentence_Ham={}

group_spam = {}
group_ham = {}

# print(arr_s)
# print(arr_h)

def countMax(arr):
    max = 0
    for item in arr:
        if len(item) > max:
            max = len(item)
    return  max

def add_and_count(someList,outputArr):
    for item in someList:
        # print(item)
        if not  item in outputArr :
            outputArr[item] = 1
        else:
            outputArr[item] += 1
    return someList

#key-number of symbol / value - number of times
def prepareData(arr_in,arr_out,max):
    for item in range(0, max):
        arr_out[item] = 0
    for key, value in arr_in.items():
        for i in range(0, max):
            if (len(key) == i):
                arr_out[i] += value
    # print(arr_out)

def createPlot(arr1, arr2):
    fig, ax = plt.subplots()
    plt.title('Диаграмма прспределения к-вa символов в предложениях')
    ax.plot(arr1.keys(), arr1.values(), 'y')
    ax.plot(arr2.keys(), arr2.values(), 'b')
    ax.set_xlabel('Symbols', fontsize=15, color='green')
    ax.set_ylabel('Amount', fontsize=15,  color='green')

    plt.show()

max = max(countMax(arr_h),countMax(arr_s))
print(max)

add_and_count(arr_s, arrSentence_Spam)
add_and_count(arr_h, arrSentence_Ham)
print(arr_s)
print(arrSentence_Spam)

prepareData(arrSentence_Spam,group_spam,countMax(arr_s)+1)
prepareData(arrSentence_Ham,group_ham,countMax(arr_h)+1)
print(group_spam)
print(group_ham)

createPlot(group_spam,group_ham)





