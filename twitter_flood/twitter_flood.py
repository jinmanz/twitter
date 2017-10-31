 # -*- coding: utf-8 -*-     
import tweepy 
from tweepy import OAuthHandler
import csv


consumer_key = "WRzrHerkO3PQFE9PsbOSVJxUO"  
consumer_secret = "l2F8owgWRm33SeK7ts5Vs6yBU3Qd2FbXzVoM2x9k0BFsXbqLfr"  
access_token = "527454179-JZ7zT9M4jgffQYqn3SG7W1z3UdphCT5irgXI96Qa"  
access_token_secret = "Ljtj25dztSwJ4OGs2IfB2vkGhdghmvZl4cLMSkCssKxnJ" 

# 使用API对象获取你的时间轴上的微博，并把结果存在一个叫做public_tweets的变量中
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()  

# 传入认证信息，并创建API对象
api = tweepy.API(auth)

# 你想查找的关键字
query = "#harveyflood"  
# 语言代码（遵循ISO 639-1标准）
language = "en"
results = api.search(q=query, lang=language,since='2017-09-17',until='2017-09-18', count='20000')

#把text存到一个文件txt
fo = open("tweets17-18.txt", "wb")
for tweet in results:
    fo.write(tweet.text.encode('utf-8'))
    
#把用户名和text存到一个csv  
rows = []
for tweet in results:
    rows.append([tweet.user.screen_name,tweet.text.encode('utf-8')])


with open('tweets17-18.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(rows)
f.close()
