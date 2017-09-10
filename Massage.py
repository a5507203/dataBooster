'''
Created on 8 Sep. 2017

@author: yuyao
'''

class Massage(object):
    '''
    classdocs
    '''
    reSends = {}
    reactions = {}
    comments = {}
    time = 0
    popularity = 0
    def __init__(self, reSends, reactions, comments,time, popularity):
        '''
        Constructor
        '''
        self.reSends = reSends
        self.reactions = reactions
        self.comments = comments
        self.popularity = popularity
        self.time = time
        
        
    def addreSend(self,reSend):
        self.users.append(reSend)
    
    
    def addReaction(self,reaction):
        self.reactions.append(reaction)      


    def addComment(self,comment):
        self.comments.append(comment)   
    
    
    def setTime(self,time):
        self.time =time
 
 
    def setPopuarity(self,popularity):
        self.popularity=popularity    
             
        
    def setreSend(self,reSends):
        self.users=reSends
    
    
    def setReaction(self,reactions):
        self.reactions=reactions    


    def setComment(self,comments):
        self.comments=comments     