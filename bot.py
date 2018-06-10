from bs4 import BeautifulSoup
import urllib.request
import re
import tweepy
from secrets import *

def getTwitter():
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

    return tweepy.API(auth)

def getRandomWikiTitle():
    with urllib.request.urlopen("https://en.wikipedia.org/wiki/Special:Random") as page:
        heading = None
        while not heading:
            parsed = BeautifulSoup(page.read(), "html.parser")
            heading = parsed.find(id="firstHeading") #Parse page and get heading

        return re.sub(r"\(.*\)", "", heading.get_text()).strip() #Eliminate parenthesis and additional spaces

getTwitter().update_status(getRandomWikiTitle() + " Battle Royale confirmed")