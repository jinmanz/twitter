 # -*- coding: utf-8 -*-     
import csv
from os import listdir
import re


def read_file(filename):
    "Read the contents of FILENAME and return as a string."
    infile = open(filename) # windows users should use codecs.open after importing codecs
    contents = infile.read()
    infile.close()
    return contents

def list_textfiles(directory):
    "Return a list of filenames ending in '.txt' in DIRECTORY."
    textfiles = []
    for filename in listdir(directory):
        if filename.endswith(".csv"):
            textfiles.append(directory + "/" + filename)
    return textfiles


filenames = list_textfiles("csv")
# 遍历csv文件，读取每个csv文件中的text列，并把所得的list 变成 string
tweet_text=[]
for filename in filenames:
    with open(filename,'rb') as csvfile:
        reader = csv.reader(csvfile)
        #tweet_text.append( [row[3] for row in reader])
        tweet_text.append(' '.join(map(str,[row[3] for row in reader])))
#str用来当文件名变量，再循环中保存每天的转发量
str = '1'
#对每天的text分析，统计转发量
for text_per_day in tweet_text:
    rts = re.findall(r'@[\w]+',text_per_day) #a list of all the matches
    rts_set = set(rts)
    count_list = []
    for item in rts_set:
        count_list.append((item,rts.count(item)))  
    count_list_sorted = sorted(count_list,cmp=lambda x,y:cmp(x[1],y[1]),reverse=True)
    headers = ['Account','Frequency']
    with open(str+'.csv','wb') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(count_list_sorted)
    str += '1'


