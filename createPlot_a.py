import  matplotlib.pyplot as plt
import  numpy as  np
import processingFile

arr_s = processingFile.arrWord_Spam
arr_h = processingFile.arrWord_Ham

#массив слов разбитый на диапазоны по к-ву
group_s = {}
group_h = {}
# print(arr_s)
# print(arr_h)

def countAvg(arr):
    t_len = 0
    t_val = 0
    for key, value in arr.items():
        t_len += len(key)*value
        t_val += value
    return t_len/t_val

def countMax(arr):
    max = 0
    for key, value in arr.items():
        if len(key) > max:
            max = len(key)
    return  max

def prepareData(arr_in,arr_out,max):
    for item in range(0, max):
        arr_out[item] = 0

    for key, value in arr_in.items():
        for i in range(0, max):
            if (len(key) == i):
                arr_out[i] += value
    # print(arr_out)

max_s = countMax(arr_s)
max_h = countMax(arr_h)
print('avg for spam: ',countAvg(arr_s))
print('avg for ham : ',countAvg(arr_h))

prepareData(arr_s,group_s,max_s)
prepareData(arr_h,group_h,max_h)

fig, ax = plt.subplots()
plt.title('Диаграмма распределения к-ва слов в spam/ham')

ax.plot(group_s.keys(),group_s.values(),'y')
ax.plot(group_h.keys(),group_h.values(),'b')

ax.set_xlabel('к-во слов', fontsize = 15, color = 'green')
ax.set_ylabel('Частота', fontsize = 15, color = 'green')

plt.show()














