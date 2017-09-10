'''
Created on 8 Sep. 2017

@author: yuyao
'''

class Users(object):
    '''
    classdocs
    '''
    users = list()
    def __init__(self, users):
        '''
        Constructor
        '''
        self.users = users
        
    def addUser(self,user):
        self.users.append(user)
        
