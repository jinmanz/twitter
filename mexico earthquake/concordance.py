 # -*- coding: utf-8 -*-     
import csv

from nltk.book import *



#define a list to score the tweets posted per day
tweetsPD=[]
with open('tweets-19.csv','rb') as f:
    reader = csv.reader(f)
    for row in reader:
        tweetsPD.append(row[3])
           
         
#convert a list of words to text           
tweetsPD = ' '.join(tweetsPD)
tweetsPD = tweetsPD.lower()
fo = open("text.txt", "wb")
fo.write(tweetsPD);


# concordance analysis
tweetsPD.concordance('@jorge_guajardo')



