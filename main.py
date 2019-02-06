''' 
    My thought process here. I need to do several tasks, I will work through them one by one.
    I will also need to find some external web scrapping libraries to do some of them.
    Web scraping : beautifulsoup4 (import bs4)
    Interacting with website : selenim
    
'''

import time # for sleeping
from authenticate import Websites
from get_data import Data
from links import CONST_EMAILS, SOCIAL_MEDIA, CODING_MEDIA, BLOGS, SCHOOL
from helpers import convert_to_command as cts

class Jarvis:
    '''
        Jarvis is the class for the bot. It will handle all the other classes and call upon their functions.
    '''
    def __init__(self):
        self.Website = Websites()
        self.Data = Data()
        
    def 


