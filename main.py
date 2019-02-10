"""
    My thought process here. I need to do several tasks, I will work through them one by one.
    I will also need to find some external web scrapping libraries to do some of them.
    Web scraping : beautifulsoup4 (import bs4)
    Interacting with website : selenium
"""

import time     # for sleeping
from authenticate import Websites
from get_data import Data
from links import CONST_EMAILS, SOCIAL_MEDIA, CODING_MEDIA, BLOGS, SCHOOL
from helpers import convert_to_command as cts


class Jarvis:
    
    def __init__(self):
        self.website = Websites()
        self.data = Data()
        self.cmd = ''

    def begin(self, cmd):
        # TODO : for any media command passed, sign in, then wait for other commands which refer to other functions



if __name__ == '__main__':
    Bot = Jarvis()
    flag = True
    cmd = input()
    while flag or cmd.lower() != 'end':
        flag = False
        Bot.begin(cmd)
        cmd = input()
