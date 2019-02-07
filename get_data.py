'''
    I will be using beautifulsoup4 and requests to get data from online forums
'''

# requests module will be used to download online files if any, but to also give raw HTML text to beautifulsoup4
import requests

# beautifulsoup4 will be used to collect data in this module
import bs4

class Data:
    
    def __init__(self):
        # TODO : Initiate variables
        self.media = ''
        self.connector_to_website = {"twitter" : get_twitter,
                                    'instagram' : get_instagram,
                                    "github" : get_github,
                                    "kaggle" : get_kaggle,
                                    "mail" : get_mail,
                                    "xkcd" : get_xkcd,
                                    "school" : get_school
                                   }
        
    def get_from(self, media): # receive a link to sign in into
        # TODO : a social media name is given in string, then is signed into, and collected data from
        return self.connector_to_website[media]()

def get_school():
    # TODO : get latest home page pics and articles from Bronx Science's website and the Science Survey website
    pass
    
def get_twitter():
    # TODO : get data such as number of followers and following, a few of their names, also some of the tweets from my favorite twitter accounts
    pass
    
def get_instagram():
    # TODO : get my followers list of names, following list of names, and pics from some accounts
    pass
    
def get_github():
    # TODO : get list of followers and following names, plus some news from github home page
    pass
    
def get_kaggle():
    # TODO : get some interesting articles from kaggle homepage (first five)
    pass
    
def get_mail():
    # TODO : the email themselves will be signed into in another module, here I just want to see if I have any new unread emails, if so, what are their subjects
    pass
    
def get_xkcd():
    # TODO : get me the last 10 articles from the xkcd blog, AND 10 random pics from the xkcd comic. Well, the first pic from the comic has to be after random is pressed, I already say the Carbonated Beverage one
    pass

if __name__ == '__main__':
    data = Data()
    data.get_from(input())