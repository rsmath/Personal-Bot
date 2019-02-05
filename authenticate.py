'''
    This module is for authenticating (signing in) into the various online places that I need to open and get data from.
    This will be done with the help of selenium library, as unlike the webbrowser library, it allows me to fill out username 
    and password columns instead of expecting my accounts to be already signed in.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import links
import schedule
import time

class Websites:
    
    def __init__(self):
        self.url = 'https://github.com/ramanshsharma2806/'
        self.checked_in = False
         
    def sign_in(self, url = None):
        if url != None:
            self.url = url            
        path_to_chromedriver = "/Users/ramanshsharma/Downloads/chromedriver"
        driver = webdriver.Chrome(path_to_chromedriver)
        driver.get(self.url);
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('Ramansh Sharma') # typing in the search bar
        search_box.submit()
        time.sleep(5)
        driver.close() # closing the test browser

if __name__ == '__main__':
    website = Websites()
    website.sign_in()