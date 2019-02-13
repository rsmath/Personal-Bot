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
        self.url = 'https://github.com/ramanshsharma2806'       # default link if none is passed in
        self.path_to_chromedriver = "/Users/ramanshsharma/Downloads/chromedriver"
        self.chrome_options = webdriver.ChromeOptions()     # to keep the opened browser open
        self.chrome_options.add_experimental_option("detach", True)     # this keeps the opened browser open
        self.file = pd.read_csv('secrets.csv')

    def sign_in(self, url=None):        # keeps the website open with chrome_options
        if url is not None:
            self.url = url
        driver = webdriver.Chrome(self.path_to_chromedriver, chrome_options=self.chrome_options)        # chrome_options added
        driver.get(self.url)
        sign_in_button = driver.find_element_by_link_text('Sign in')
        sign_in_button.click()
        sign_in_button = driver.find_element_by_id('login_field')
        sign_in_button.send_keys(self.file.iloc[1, 1])
        time.sleep(1)
        sign_in_button = driver.find_element_by_id('password')
        time.sleep(1)
        sign_in_button.send_keys(self.file.iloc[1, 2])
        time.sleep(1)
        sign_in_button.send_keys(Keys.RETURN)

    def get_school(self, spec):
        # TODO : either open school website or the sciencesurvey based on param
        pass

    def get_linkedin(self):
        # TODO : sign intp linkedin
        pass

    def get_twitter(self):
        # TODO : sign into twitter
        pass

    def get_instagram(self):
        # TODO : sign into instagram
        pass

    def get_github(self):
        # TODO : sign into github
        pass

    def get_kaggle(self):
        # TODO : sign into kaggle
        pass

    def get_mail(self, num):
        # TODO : sign into the mail specified; 0 is bxsci, 1 is eps, 2 is personal gmail
        pass

    def get_xkcd(self, spec):
        # TODO : just open the xkcd desired
        pass


if __name__ == '__main__':
    website = Websites()
    website.sign_in()
