'''
Created on 8 may 2019

@author: orishiku
'''
import os
from django.conf import settings

class ConfigFile(object):
    '''
    classdocs
    '''


    def __init__(self, filepath):
        '''
        Constructor
        '''
        self.file = filepath
        self.loadConfigs();
    
    def getKey(self, keyname):
        for k in self.settings:
            if k[0] == keyname:
                return k[1].strip()
        return None
    
    def loadConfigs(self):
        with open(self.file) as f:
            FILE_DATA = f.read()
            FILE_DATA = FILE_DATA.split(';')
            self.data = FILE_DATA
            self.settings = []
            for data in self.data:
                data = data.strip()
                self.settings.append(data.split(':'))
            
        