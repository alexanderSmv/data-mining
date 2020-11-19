import math
import re
import networkx as nx
import matplotlib.pyplot as plt
import operator
from bs4 import BeautifulSoup
import requests


d = 0.5
E = 0.01
allKink = []
graph = nx.DiGraph()  # узлы и ребра
dictLinks_Key = dict()
dictNumToCountOfLink = dict()
chekedLink = []
numOfLink = 0

# url = "https://sites.google.com/site/alexdatapages/"
# url = "https://sites.google.com/site/gorbanpages/"
url = input("Url: ")
invalid_href = ['.jpeg', '.jpg', '.png', '.gif', '.ppt', '.pdf', '.doc', '.txt', '.xml', '.zip', '.rar']

def recursion(mHref):
    global numOfLink
    global dictLinks_Key
    chekedLink.append(mHref)
    inerLink = []

    # текст html приводит к дереву синтаксического разбора
    pageTree = BeautifulSoup(requests.get(mHref).text, "html.parser")
    for link in pageTree.find_all('a', href=re.compile('^(/)')):  # this for /j/j/j/j
        href = link.get('href')
        href = url + href[1:]  # воссоздаем полную ссылку
        if (validation(href)):
            if href not in dictLinks_Key.keys():
                # unique {link : key}
                dictLinks_Key[href] = numOfLink
                numOfLink = numOfLink + 1
            inerLink.append(href)

            graph.add_edge(dictLinks_Key[mHref], dictLinks_Key[href])
            if href in chekedLink:
                continue
            print("href = " + href)
            recursion(href)
    dictNumToCountOfLink[dictLinks_Key[mHref]] = len(inerLink)
    graph.add_node(dictLinks_Key[mHref])
    # print(graph.edges)
    return
def validation(href):
    for i in invalid_href:
        if i in href:
            return False
    return True

def clean_url(url):
    if (url[4] == 's'):
        return url[5:]
    else:
        return url[4:]

def slau_yakobi(B):
    global dictLinks_Key
    vector_result = []
    vector_new = []
    for i in range(0, len(B)):
        vector_result.append(B[i][len(B)])
    eps = 1
    while eps > E:
        for i in range(0, len(B)):
            sum = 0
            for j in range(0, len(vector_result)):
                sum = sum + vector_result[j] * B[i][j]
            sum = sum + B[i][len(B)]
            vector_new.append(sum)
        eps = 0
        for j in range(0, len(vector_result)):
            eps = eps + math.fabs(vector_new[j] - vector_result[j])

        vector_result = vector_new.copy()
        vector_new.clear()
    pRangeDict = dict()
    for j in range(0, len(vector_result)):
        pRangeDict[j] = vector_result[j]
    pRangeDict = sorted(pRangeDict.items(), key=operator.itemgetter(1), reverse=True)
    print(pRangeDict)
    print("Top 10:")
    for j in range(0, 10):
        print(j + 1, " - ", "pageRank:", pRangeDict[j][1],"-",list(dictLinks_Key.keys())[list(dictLinks_Key.values()).index(pRangeDict[j][0])])
    print("\n")


trimUrl = clean_url(url)
dictLinks_Key[url] = numOfLink

numOfLink = numOfLink + 1
recursion(url)

nx.draw(graph, with_labels=True)
plt.show()

print("amount of links: ", len(graph.nodes))
for link, key in dictLinks_Key.items():
    print(key, " - ", link)

B = [[0 for x in range(len(graph.nodes) + 1)] for y in range(len(graph.nodes))]
for n in graph.edges:
    B[n[1]][n[0]] = d / dictNumToCountOfLink[n[0]]

for i in range(0, len(graph.nodes)):
    B[i][len(graph.nodes)] = 1 - d

slau_yakobi(B)
