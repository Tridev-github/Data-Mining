import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
stp = stopwords.words("english")
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

doc1 = requests.get("https://adgvit.com/")
doc2 = requests.get("https://dscvit.com/")
doc3 = requests.get("https://www.codechefvit.com/")

soup1 = BeautifulSoup(doc1.content,"html.parser")
soup2 = BeautifulSoup(doc2.content,"html.parser")
soup3 = BeautifulSoup(doc3.content,"html.parser")

for word in soup1(["style","script"]):
    word.decompose()
d1 = " ".join(soup1.stripped_strings)
for word in soup2(["style","script"]):
    word.decompose()
d2 = " ".join(soup2.stripped_strings)
for word in soup3(["style","script"]):
    word.decompose()
d3 = " ".join(soup3.stripped_strings)

docs = [d1,d2,d3]
bagOfWords = set()

dictionary = dict({d1:"id1",d2:"id2",d3:"id3"})

for i in docs:
    for j in i.split(" "):
        for char in j:
            if char in punc:
                j = j.replace(char,"")
        if j.lower() not in stp:
            bagOfWords.add(j.capitalize())

count = 0
index = 0
lis = []


for word in bagOfWords:
    print(word, ":",end="")
    for doc in docs:
        lis.clear()
        index = 0
        count = 0
        check=0
        for wordInDoc in doc.split(" "):
            for char in wordInDoc:
                if char in punc:
                    wordInDoc = wordInDoc.replace(char, "")
            if wordInDoc.lower() == word.lower():
                check=5
                lis.append(index)
                count+=1
                if count==1:
                    print("<",end="")
                    print(dictionary[doc],end=",")
            index+=1
        if check==5:
            print(count,end=",")
            print("[",end="")
            for i in lis:
                print(i+1,end=",")
            print("]>",end=",")
    print()
