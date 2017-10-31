 # -*- coding: utf-8 -*-     
import csv
import re
import collections
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer




#define a list to score the tweets posted per day
tweetsPD=[]
with open('tweets-25.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:
        tweetsPD.append(row[3])
           
         
#convert a list of words to text           
tweetsPD = ' '.join(tweetsPD)
tweetsPD = tweetsPD.lower()

#clean text then split it into a list of words
tweetwords = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweetsPD).split()

#stemming words
tweetwords_stemmed = []
ps = PorterStemmer()
for word in tweetwords:
    tweetwords_stemmed.append(ps.stem(word))
#remove stop words
stop_words = set(stopwords.words('english'))
filtered_tweets=[]
for word in tweetwords_stemmed:
    if word not in stop_words and word != 'rt':
        filtered_tweets.append(word)
        
#count term frequency
tf = collections.Counter(filtered_tweets)

#record the term frequency in tf.csv
csvFile = open('tf-25.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
for word, freq in tf.most_common():
    csvWriter.writerow([word, freq])