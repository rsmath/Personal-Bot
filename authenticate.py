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
        self.url = ""
        self.checked_in = False
        path_to_chromedriver = "/Users/ramanshsharma/Downloads/chromedriver"
        driver = webdriver.Chrome(path_to_chromedriver)  # Optional argument, if not specified will search path.
        driver.get('http://www.google.com/xhtml');
        time.sleep(1) # Let the user actually see something!
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        time.sleep(1) # Let the user actually see something!
        driver.quit()
    
    def sign_in(self, url):
        self.url = url

def a():
    path_to_chromedriver = "/Users/ramanshsharma/Downloads/chromedriver"
    driver = webdriver.Chrome(path_to_chromedriver)  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/xhtml');
    time.sleep(1) # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(1) # Let the user actually see something!
    driver.quit()
        
schedule.every().minute.at(":5").do(a)
    

if __name__ == '__main__':
    website = Websites()
    website.sign_in('')