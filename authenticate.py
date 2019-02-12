"""
    This module is for authenticating (signing in) into the various online places that I need to open and get data from.
    This will be done with the help of selenium library, as unlike the webbrowser library, it allows me to fill out username 
    and password columns instead of expecting my accounts to be already signed in.
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Websites:
    def __init__(self):
        self.url = 'https://twitter.com/'       # default link if none is passed in
        self.path_to_chromedriver = "/Users/ramanshsharma/Downloads/chromedriver"
        self.chrome_options = webdriver.ChromeOptions()     # to keep the opened browser open
        self.chrome_options.add_experimental_option("detach", True)     # this keeps the opened browser open
        self.file = pd.read_csv('secrets.csv')

    def sign_in(self, url=None):        # keeps the website open with chrome_options
        if url is not None:
            self.url = url
        driver = webdriver.Chrome(self.path_to_chromedriver, chrome_options=self.chrome_options)        # chrome_options added
        driver.get(self.url)
        sign_in_button = driver.find_element_by_link_text('Log in')
        sign_in_button.click()
        # search_box.send_keys('ramanshsharma2806')       # typing in the search bar
        # time.sleep(2)
        # search_box.send_keys(Keys.ENTER)        # submitting the search box


if __name__ == '__main__':
    website = Websites()
    website.sign_in()
