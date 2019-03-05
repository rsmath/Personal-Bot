"""
    I will be using beautifulsoup4 and requests to get data from online forums
"""
from helpers import commands  # used to obtain the links of the forums

# requests module will be used to download online files if any, but to also give raw HTML text to beautifulsoup4
import requests

# beautifulsoup4 will be used to collect data in this module
import bs4 as bs


class Data:

    def __init__(self):
        # TODO : Initiate variables
        self.media = ''
        self.connector_to_website = {
            "twitter": self.get_twitter,
            "instagram": self.get_instagram,
            "github": self.get_github,
            "linkedin": self.get_linkedin,
            "kaggle": self.get_kaggle,
            "mail": self.get_mail,
            "mail0": self.get_mail,
            "mail1": self.get_mail,
            "mail2": self.get_mail,
            "xkcd": self.get_xkcd,
            "blog": self.get_xkcd,
            "school": self.get_school,  # different param from below one
            "sciencesurvey": self.get_school  # different param from above one
        }
        self.bsoup = None

    def get_from(self, media):  # receive a link to sign in into
        # TODO : a social media name is given in string, then is signed into, and collected data from
        return self.connector_to_website[media](param=media)

    def get_school(self, param=None):
        # TODO : get latest home page pics and articles from Bronx Science's website and the Science Survey website
        pass

    def get_twitter(self, param=None):
        # TODO : get data such as number of followers and following, a few of their names, also some of the tweets from my
        #  favorite twitter accounts
        pass

    def get_linkedin(self, param=None):
        # TODO : sign in and get data from the linkedin page; connections and possibly some top stories in the feed
        pass

    def get_instagram(self, param=None):
        # TODO : get my followers list of names, following list of names, and pics from some accounts
        pass

    def get_github(self, param=None):
        # TODO : get list of followers and following names, plus some news from github home page
        pass

    def get_kaggle(self, param=None):
        # TODO : get some interesting articles from kaggle homepage (first five)
        pass

    def get_mail(self, param=None):
        # TODO : the email themselves will be signed into in another module, here I just want to see if I have any new
        #  unread emails, if so, what are their subjects
        pass

    def get_xkcd(self, param=None):
        # TODO : get me the last 10 articles from the xkcd blog, AND 10 random pics from the xkcd comic. Well, the first
        #  pic from the comic has to be after random is pressed, I already saw the Carbonated Beverage one
        # For default right now, I will only access the main article page of xkcd. Learning requests here
        response = requests.get(commands[param])
        if check_res(response) is not None:
            print(check_res(response))
            return

        file = open('file.txt', 'wb')
        self.bsoup = bs.BeautifulSoup(response.text, features="html.parser")
        article = self.bsoup.select('article.entry')
        print(type(article[0].getText()))
        article_url = 'https:' + article[0].get('src')
        res = requests.get(article_url)
        if check_res(response) is not None:
            print(check_res(response))
            return

        for chunk in res.iter_content(100000):
            file.write(chunk)

        file.close()


def check_res(res):
    try:
        res.raise_for_status()

    except Exception as exc:
        return '\nThere was a problem: %s\nPlease try giving the command again\n' % exc


if __name__ == '__main__':
    data = Data()
    data.get_from(input())
