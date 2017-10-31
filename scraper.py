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
'''
# 遍历所拉取的全部微博
for tweet in public_tweets:  
   # 打印存在微博对象中的text字段
   print tweet.user.screen_name
   print "lo:" + tweet.user.location
'''


'''
# 传入认证信息，并创建API对象
api = tweepy.API(auth)

# 待拉取微博的用户
name = "nytimes"  
# 待拉取的微博数量
tweetCount = 20

# 使用上面的参数，调用user_timeline函数
results = api.user_timeline(id=name, count=tweetCount)

# 遍历所拉取的全部微博
for tweet in results:  
   # 打印存在微博对象中的text字段
   print tweet.text
 '''


# 传入认证信息，并创建API对象
api = tweepy.API(auth)

# 你想查找的关键字
query = "Trump"  
# 语言代码（遵循ISO 639-1标准）
language = "en"

# 使用上面的参数，调用user_timeline函数
results = api.search(q=query, lang=language)
'''
fo = open("tweets.csv","wb")
writer = csv.writer(fo)
writer.writerow(['username','text'])
'''
rows = []
for tweet in results:
    rows.append([tweet.user.screen_name,tweet.text])


with open('tweets.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(rows)
f.close()
'''
# 遍历所拉取的全部微博
for tweet in results:
    data.append([tweet.user.screen_name,tweet.text])
    for line in data:
        fo.writerows(line + "\n")
fo.close()
    #line = tweet.user.screen_name + ' tweeted ' + tweet.text + '\n'

    #fo.write(line.encode('utf-8'))


   # 打印存在微博对象中的text字段
   #print tweet.user.screen_name,"Tweeted:",tweet.text 
   #file.write(tweet.text.encode('utf-8'))

'''