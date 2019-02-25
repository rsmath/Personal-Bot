"""
    This module is for authenticating (signing in) into the various online places that I need to open and get data from.
    This will be done with the help of selenium library, as unlike the webbrowser library, it allows me to fill out
    username and password columns instead of expecting my accounts to be already signed in.
"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helpers import commands  # to convert link to command
from links import SCHOOL, CONST_EMAILS, BLOGS


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
                            'linkedin' : self.get_linkedin,
                            'kaggle': self.get_kaggle,
                            'mail': self.get_mail,      # open all the emails
                            'mail0': self.get_mail,     # open bxsci email
                            'mail1': self.get_mail,     # open eps email
                            'mail2':self.get_mail,      # open personal gmail
                            'xkcd': self.get_xkcd,      # main article page
                            'blog': self.get_xkcd,      # blog (comic) page
                            'school': self.get_school,      # open the school website
                            'sciencesurvey': self.get_school        # open the sciencesurvey online newspaper
                            }

    def sign_in(self, url=None):        # keeps the website open with chrome_options
        if url is not None:
            self.url = url
        media = link_to_media(self.url)
        self.driver = webdriver.Chrome(self.path_to_chromedriver,
                                       chrome_options=self.chrome_options)  # chrome_options added

        # TODO : in order to pass in certain params to certain functions, I need explicit cases mentioned here
        if media == 'mail0' or media == 'mail1' or media == 'mail2':        # EMAILS
            self.media_to_func[media](num=int(media[-1]))

        elif media == 'school' or media == 'sciencesurvey':                 # SCHOOL WEBSITE AND SCIENCESURVEY
            self.media_to_func[media](spec=media)

        elif media == 'xkcd' or media == 'blog':
            self.media_to_func[media](spec=media)       # XKCD OR BLOG

        else:
            self.media_to_func[media]()

    def get_school(self, spec=None):
        # TODO : either open school website or the sciencesurvey based on param
        # if check_if_none(self.driver):
        # self.driver.execute_script(f'''window.open({str(self.url)}, "_blank");''')
        if spec == 'school' or spec is None:
            self.url = SCHOOL[0]

        elif spec == 'sciencesurvey':
            self.url = SCHOOL[1]

        self.driver.get(self.url)

    def get_linkedin(self):
        # TODO : sign into linkedin
        # if check_if_none(self.driver):
        #     body = self.driver.find_element_by_tag_name("body")
        #     body.send_keys(Keys.CONTROL + 't')
        self.driver.get(self.url)
        time.sleep(2)
        give_username = self.driver.find_element_by_id('login-email')
        give_username.send_keys(self.file.iloc[4, 1])
        time.sleep(2)
        give_password = self.driver.find_element_by_id('login-password')
        time.sleep(2)
        give_password.send_keys(self.file.iloc[4, 2])
        time.sleep(2)
        give_password.send_keys(Keys.RETURN)

    def get_twitter(self):
        # TODO : sign into twitter
        # if check_if_none(self.driver):
        #     body = self.driver.find_element_by_tag_name("body")
        #     body.send_keys(Keys.CONTROL + 't')
        self.driver.get(self.url)
        time.sleep(2)
        click_login = self.driver.find_element_by_link_text('Log in')
        click_login.click()
        give_username = self.driver.find_element_by_class_name('js-username-field')
        give_username.send_keys(self.file.iloc[0, 1])
        time.sleep(2)
        give_password = self.driver.find_element_by_class_name('js-password-field')
        give_password.send_keys(self.file.iloc[0, 2])
        time.sleep(2)
        give_password.send_keys(Keys.RETURN)

    def get_instagram(self):
        # TODO : sign into instagram
        # if check_if_none(self.driver):
        #     body = self.driver.find_element_by_tag_name("body")
        #     body.send_keys(Keys.CONTROL + 't')
        self.driver.get(self.url)
        time.sleep(2)
        log_in = self.driver.find_element_by_link_text('Log in')
        log_in.click()
        time.sleep(2)
        email_enter = self.driver.find_element_by_class_name('_2hvTZ')
        email_enter.send_keys(self.file.iloc[2, 1])
        time.sleep(2)
        email_enter = self.driver.find_element_by_class_name('pexuQ')
        email_enter.send_keys(self.file.iloc[2, 2])
        time.sleep(2)
        email_enter.send_keys(Keys.RETURN)

    def get_github(self):
        # TODO : sign into github
        # if check_if_none(self.driver):
        #     body = self.driver.find_element_by_tag_name("body")
        #     body.send_keys(Keys.CONTROL + 't')
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
        # if check_if_none(self.driver):
        #     body = self.driver.find_element_by_tag_name("body")
        #     body.send_keys(Keys.CONTROL + 't')
        self.driver.get(self.url)
        time.sleep(2)
        click_login = self.driver.find_element_by_class_name('button--small')
        click_login.click()
        give_username = self.driver.find_element_by_id('username-input-text')
        give_username.send_keys(self.file.iloc[4, 1])
        time.sleep(2)
        give_password = self.driver.find_element_by_id('password-input-text')
        give_password.send_keys(self.file.iloc[4, 2])
        time.sleep(2)
        click_sign_in = self.driver.find_element_by_link_text('Sign in')
        click_sign_in.click()

    def get_mail(self, num=None):
        # TODO : sign into the mail specified; 0 is bxsci, 1 is eps, 2 is personal gmail, if no num, then all
        # if check_if_none(self.driver):
        #     body = self.driver.find_element_by_tag_name("body")
        #     body.send_keys(Keys.CONTROL + 't')
        if num is None:
            self.url = CONST_EMAILS[0]
            email, password = self.file.iloc[5, 1], self.file.iloc[5, 2]
            mail_action(self.driver, self.url, email, password)
            email, password = self.file.iloc[6, 1], self.file.iloc[6, 2]        # update
            time.sleep(2)
            self.driver.execute_script(f'window.open({self.url}, "_blank");')
            mail_action(self.driver, self.url, email, password)     # second email
            email, password = self.file.iloc[7, 1], self.file.iloc[7, 2]        # update
            time.sleep(2)
            self.driver.execute_script(f'window.open({self.url}, "_blank");')
            mail_action(self.driver, self.url, email, password)     # third email

        else:
            self.url = CONST_EMAILS[num]
            email = self.file.iloc[num + 5, 1]
            password = self.file.iloc[num + 5, 2]

        mail_action(self.driver, self.url, email, password)

    def get_xkcd(self, spec):
        # TODO : just open the xkcd desired, either the blog or the comics
        # if check_if_none(self.driver):
        #     body = self.driver.find_element_by_tag_name("body")
        #     body.send_keys(Keys.CONTROL + 't')
        if spec == 'xkcd':
            self.url = BLOGS[0]

        elif spec == 'blog':
            self.url = BLOGS[1]

        self.driver.get(self.url)


def link_to_media(link):
    # TODO : obtain the media associated with a link
    return [item[0] for item in commands.items() if link == item[1]][0]


def mail_action(driver, url, email, password):
    driver.get(url)
    time.sleep(2)
    email_input = driver.find_element_by_id('identifierId')
    email_input.send_keys(email)
    email_input.send_keys(Keys.RETURN)
    time.sleep(2)
    password_input = driver.find_element_by_class_name('whsOnd')
    password_input.send_keys(password)
    time.sleep(2)
    password_input.send_keys(Keys.RETURN)


if __name__ == '__main__':
    website = Websites()
    website.sign_in()
