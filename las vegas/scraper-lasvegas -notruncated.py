 # -*- coding: utf-8 -*-     
import tweepy 
from tweepy import OAuthHandler
import csv
import time


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
query = 'Las Vegas shooting'
# 语言代码（遵循ISO 639-1标准）
language = 'en'
    
#把用户名和text存到一个csv  
rows = []
i = 0
fo = open('tweets-02.txt', 'a')
#取1000条
while i < 10:
    results = api.search(q=query, lang=language, since='2017-10-02', until='2017-10-03',include_rts='true',count = 100)
    for tweet in results:
        if hasattr(tweet, 'retweeted_status'):
            
            if len(rows)== 0 :
                rows.append([tweet.id,tweet.user.screen_name,tweet.created_at,('RT @'+ tweet.retweeted_status.user.screen_name + ' ' + tweet.retweeted_status.text).encode('utf-8')])
            if len(rows) > 0 and tweet.id != rows[-1][0] :
                rows.append([tweet.id,tweet.user.screen_name,tweet.created_at,('RT @'+ tweet.retweeted_status.user.screen_name + ' ' + tweet.retweeted_status.text).encode('utf-8')])      
        else:
            if len(rows)== 0 :
                rows.append([tweet.id,tweet.user.screen_name,tweet.created_at,tweet.text.encode('utf-8')])
            if len(rows) > 0 and tweet.id != rows[-1][0] :
                rows.append([tweet.id,tweet.user.screen_name,tweet.created_at,tweet.text.encode('utf-8')])      
        
        #把text存到一个文件txt
        fo.write(tweet.text.encode('utf-8'))
    i += 1
    #暂停2秒再执行下一次搜索
    time.sleep(2)

with open('tweets-02.csv','a') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(rows)
f.close()
