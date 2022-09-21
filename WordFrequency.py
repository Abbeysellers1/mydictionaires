
import csv

text= open('sometext.txt', 'r')

count={}


for line in text:
    line=line.strip()
    words=line.split(' ')
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
for key in list(count.keys()):
    print(key, ':', count[key])

text.close()





