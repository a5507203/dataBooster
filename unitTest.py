'''
Created on 10 Sep. 2017

@author: yuyao
'''
import unittest
from twitterApi import*
from config import*


class Test(unittest.TestCase):


    def testUpdateRetweeters(self):
        retweeterList = ["hello","world","adsfaewf2"]
        tweetId="906712991940399104"
        userId = "25073877"
        updateRetweeters(userId,tweetId,retweeterList)

    def testIsExist(self):
        print(isExist("","aaaa"))
        
    def testStoreToCelebrity(self):
        storeToCelebrity("12313123")
        
    def testCreateTweets(self):
        path = CELEBRITY_PATH+"12313123"+"/tweets/"
        id = "12312313141513"
        createTweets(path, id)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    test =Test()
    #test.testUpdateRetweeters()
    #test.testIsExist()
    #test.testStoreToCelebrity()
   # print(api.GetUserTimeline(user_id="403992815",include_rts=False))
    #test.testCreateTweets()
    
    