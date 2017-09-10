'''
Created on 8 Sep. 2017

@author: yuyao
'''

class User(object):
    '''
    classdocs
    '''

    id = 0
    priority = 1
    follow = list()
    massages = list()
    def __init__(self, userId, follow, massages):
        '''
        Constructor
        '''
        self.id = userId
        self.follow = follow
        self.massages = massages
        
        
    def addMassage(self,massage):
        self.massages.append(massage)
        