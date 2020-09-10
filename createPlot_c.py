import processingFile
from collections import  Counter
import  matplotlib.pyplot as plt


spam20 = dict(Counter(processingFile.arrWord_Spam).most_common(15))
ham20 = dict(Counter(processingFile.arrWord_Ham).most_common(15))

def createPlot(arr,info):
    fig, ax = plt.subplots()
    plt.title('top10 '+info +' words')
    ax.plot(arr.keys(), arr.values(), 'y')
    ax.set_xlabel('Words', fontsize=15, color='green')
    ax.set_ylabel('Amount', fontsize=15, color='green')

    plt.show()

createPlot(ham20,'ham')
createPlot(spam20,"spam")

