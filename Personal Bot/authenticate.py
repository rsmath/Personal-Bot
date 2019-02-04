'''
    This module is for authenticating (signing in) into the various online places that I need to open and get data from.
    This will be done with the help of selenium library, as unlike the webbrowser library, it allows me to fill out username 
    and password columns instead of expecting my accounts to be already signed in.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import [TheNameOfTheExceptionClass]
import websites as wb

class Websites:
    
    def __init__(self):
        self.url = ""
        self.checked_in = False
    
    def sign_in(url):
        self.url = url

        
    

if __name__ == '__main__':
    website = Websites()
    website.sign_in('')