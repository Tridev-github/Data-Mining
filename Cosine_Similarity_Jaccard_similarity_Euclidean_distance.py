from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import TfidfVectorizer

d1 = "money money money "
d2 = "free money for free gambling fun "
d3 = "gambling for fun "
d4 = "machine learning for fun fun fun "
d5 = "free machine learning "
q = "machine learning for free"
txt = d1 + d2 + d3 + d4 + d5
text = [word for word in txt.split()]
vocab = set(word for word in text)
docs = [d1, d2, d3, d4, d5]
setOfDoc = []
queryList = [word for word in q.split(" ")]

for sen in docs:
    tempSet=set()
    for word in sen.split():
        tempSet.add(word)
        con = list(tempSet)
    setOfDoc.append(con)
jaccard = []
for doc in setOfDoc:
    jInter = 0
    jUnion = 0
    for word in doc:
        for wor in queryList:
            if wor == word:
                jInter+=1;
    tempList = set(doc+queryList)
    for ele in tempList:
        jUnion+=1;
    jaccard.append([jInter/ jUnion])

fl = []
que = []
for sen in docs:
    l = []
    for word in vocab:
        count = 0
        for com in sen.split(" "):
            if word == com:
                count += 1
        l.append(count)
    fl.append(l)
for word in vocab:
    count = 0
    for com in q.split(" "):
        if word == com:
            count += 1
    que.append(count)
print("EUCLIDEAN DISTANCE:")
print(euclidean_distances(fl,[que]))

print("JACCARD SIMILARITY:")
print(jaccard)

tfidf = TfidfVectorizer().fit_transform(docs+[q])
print("COSINE SIMILARITY:")
print(cosine_similarity(tfidf,tfidf))
