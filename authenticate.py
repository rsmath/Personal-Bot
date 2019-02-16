"""
    This module is for authenticating (signing in) into the various online places that I need to open and get data from.
    This will be done with the help of selenium library, as unlike the webbrowser library, it allows me to fill out username 
    and password columns instead of expecting my accounts to be already signed in.
"""

import pandas as pd
from selenium import webdriver
from helpers import commands        # to convert link to command
from selenium.webdriver.common.keys import Keys
import time


class Websites:
    def __init__(self):
        self.url = 'https://github.com/ramanshsharma2806'       # default link if none is passed in
        self.path_to_chromedriver = "/Users/ramanshsharma/Downloads/chromedriver"
        self.chrome_options = webdriver.ChromeOptions()     # to keep the opened browser open
        self.chrome_options.add_experimental_option("detach", True)     # this keeps the opened browser open
        self.file = pd.read_csv('secrets.csv')
        self.driver = None
        # if instantiated here, then it will launch a browser when the object is instantiated
        # which is highly undesired
        self.media_to_func = {
                            'twitter': self.get_twitter,
                            'instagram': self.get_instagram,
                            'github': self.get_github,
                            'kaggle': self.get_kaggle,
                            'mail': self.get_mail,
                            'mail0': self.get_mail,
                            'mail1': self.get_mail,
                            'mail2':self.get_mail,
                            'xkcd': self.get_xkcd,
                            'blog': self.get_xkcd,
                            'school': self.get_school,
                            'sciencesurvey': self.get_school
                            }

    def sign_in(self, url=None):        # keeps the website open with chrome_options
        if url is not None:
            self.url = url
        media = link_to_media(self.url)
        self.driver = webdriver.Chrome(self.path_to_chromedriver,
                                       chrome_options=self.chrome_options)  # chrome_options added
        self.get_github()

    def get_school(self, spec):
        # TODO : either open school website or the sciencesurvey based on param
        pass

    def get_linkedin(self):
        # TODO : sign into linkedin
        pass

    def get_twitter(self):
        # TODO : sign into twitter
        pass

    def get_instagram(self):
        # TODO : sign into instagram
        pass

    def get_github(self):
        # TODO : sign into github
        self.driver.get(self.url)
        time.sleep(2)
        sign_in_button = self.driver.find_element_by_link_text('Sign in')
        sign_in_button.click()
        sign_in_button = self.driver.find_element_by_id('login_field')
        time.sleep(2)
        sign_in_button.send_keys(self.file.iloc[1, 1])
        time.sleep(2)
        sign_in_button = self.driver.find_element_by_id('password')
        time.sleep(2)
        sign_in_button.send_keys(self.file.iloc[1, 2])
        time.sleep(2)
        sign_in_button.send_keys(Keys.RETURN)

    def get_kaggle(self):
        # TODO : sign into kaggle
        pass

    def get_mail(self, num):
        # TODO : sign into the mail specified; 0 is bxsci, 1 is eps, 2 is personal gmail
        pass

    def get_xkcd(self, spec):
        # TODO : just open the xkcd desired
        pass


def link_to_media(link):
    # TODO : obtain the media associated with a link
    return [item[0] for item in commands.items() if link == item[1]][0]


if __name__ == '__main__':
    website = Websites()
    website.sign_in()
