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

tweet_text_string = ' '.join(map(str,tweet_text))
#统计所有转发账号
rts = re.findall(r'@[\w]+',tweet_text_string) #a list of all the matches
rts_set = set(rts)
count_list = []
for item in rts_set:
    count_list.append((item,rts.count(item)))
    
count_list_sorted = sorted(count_list,cmp=lambda x,y:cmp(x[1],y[1]),reverse=True)

# record the list sorted in a csv file
headers = ['Account','Frequency']
with open('count_RT.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(count_list_sorted)

    

   
    
#创建空dictionary
#遍历文件夹下csv文件
    #对每个文件读取csv中text一列
        #判断是否是‘RT 。。。’
            #判断是否在list里，
                #不在的话，加入dictionary，value为1
                #在的话，该key的value+1
            