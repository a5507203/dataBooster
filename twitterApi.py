import twitter
from config import*
import os
'''
Created on 10 Sep. 2017

@author: yuyao
'''
def getRecentTweetId(userId):
    timeLines = api.GetUserTimeline(user_id=userId, include_rts=False)
    if len(timeLines)==0:
        return -1
    return api.GetUserTimeline(user_id=userId, include_rts=False)[0].id


def getRecentRetweeters(tweetId):
    return api.GetRetweeters(status_id=tweetId)


def strToSet(str): 
    return set(str.split(","))

def setToStr(set):
    list1 = list(set)
    return ','.join(str(e) for e in list1)    
        
def getAllCelebrities():
    return os.listdir(CELEBRITY_PATH)

def getAllSaltFishs():
    return os.listdir(SALTFISH_PATH)

#need to check is exist
def storeToSaltFish(retweeter):
    os.makedirs(SALTFISH_PATH+retweeter)
    open(SALTFISH_PATH+retweeter+"/userDetail",'w')


#need to check is exist
def storeToCelebrity(retweeter):
    os.makedirs(CELEBRITY_PATH+retweeter)
    open(CELEBRITY_PATH+retweeter+"/userDetail",'w')
    os.makedirs(CELEBRITY_PATH+retweeter+"/"+"tweets")

def isCelebrity(retweeter): 
    return api.GetUser(user_id=retweeter).followers_count>10000


def isExist(path, id):
    return os.path.exists(path+id)


def createTweets(path, id):
    f = open(path+id,'w')
    f.write("favorite_count:\nretweet_count:\nstart")
    f.close()
        
def updateRetweeters(userId,tweetId,retweeterList):
    if(isExist(CELEBRITY_PATH+userId+"/tweets/", tweetId)==False):
        createTweets(CELEBRITY_PATH+userId+"/tweets/",tweetId)
    with open(CELEBRITY_PATH+userId+"/tweets/"+tweetId, "r+") as f:
        lines=f.readlines()
        oldIdsSet = strToSet(lines[2])
        newIdsSet = set(retweeterList)-oldIdsSet
        newIdStr = setToStr(newIdsSet)
        updateUsers(newIdsSet)
        if(newIdStr!=""):    
            print("celebrity retweet updating"+userId)
            f.write(","+newIdStr)
            
def updateUsers(retweeterList):
    for retweeter in retweeterList:
        retweeterId = str(retweeter)
        if(isExist(CELEBRITY_PATH,retweeterId)==False and isCelebrity(retweeterId)):
            tracks.append(retweeterId)
            storeToCelebrity(retweeterId)
            print('updating Celebrity'+retweeterId)
        elif(isExist(SALTFISH_PATH, retweeterId)==False):
            print('updating saltFish'+retweeterId)
            storeToSaltFish(retweeterId)
        


account = account2
api = twitter.Api(consumer_key=account[0],
                      consumer_secret= account[1],
                      access_token_key=account[2],
                      access_token_secret=account[3],application_only_auth=True)

 
tracks = getAllCelebrities()
i = 0
while True:
    for celebrity in tracks:
        print(celebrity)
        tweetId = getRecentTweetId(celebrity)
        if(tweetId == -1):
            continue
        retweeterList = getRecentRetweeters(tweetId)
        updateRetweeters(str(celebrity),str(tweetId),retweeterList)
        print(i)
        i+=1
    print("next round")
        
       
    
    





# for root, dirs, files in a:
#     print (root)
#     print(dirs)
#     print (files)




