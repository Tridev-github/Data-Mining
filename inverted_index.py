from nltk.corpus import stopwords
stp = stopwords.words("english")
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

doc1 = open("doc1",'r')
doc2 = open("doc2",'r')
doc3 = open("doc3",'r')


d1 = doc1.readline()
d2 = doc2.readline()
d3 = doc3.readline()
docs = [d1,d2,d3]
bagOfWords = set()

doc1.close()
doc2.close()
doc3.close()

dictionary = dict({d1:"id1",d2:"id2",d3:"id3"})

for i in docs:
    for j in i.split(" "):
        for char in j:
            if char in punc:
                j = j.replace(char,"")
        if j.lower() not in stp:
            bagOfWords.add(j.capitalize())


for word in bagOfWords:
    print(word, ":",end="")
    for doc in docs:
        for wordInDoc in doc.split(" "):
            for char in wordInDoc:
                if char in punc:
                    wordInDoc = wordInDoc.replace(char, "")
            if wordInDoc.lower() == word.lower():
                print(dictionary[doc],end=",")
                break
    print()
