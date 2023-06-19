import tweepy
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

#initialize twitter bot
consumer_key = 'KEY'
consumer_secret = 'SECRET'
oauth_token = 'TOKEN'
oauth_secret = 'SECRET'

authenticator = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticator.set_access_token(oauth_token, oauth_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)
#function for tweeting
def tweet(text):
    api.update_status(text)


#main that post evry hour (xx:33)
while(True):
    Time = datetime.now()
    minutes = Time.minute

    if minutes==33:
        #scraping random stuff from wikipedia and post it
        while(True):
            #scrape the main content from wikipedia
            page = requests.get("https://it.wikipedia.org/wiki/Special:Random")
            soup = BeautifulSoup(page.content, 'html.parser')
            for div in soup.find_all("div", {'class': 'noprint torna-a'}):
                div.decompose()
            info=soup.findAll('p')
            fact = info[0].text
            #check if can be tweeted and procedes (tweets can't be longer than 280 character)
            if len(fact)<=280:
                break
        tweet(fact)
        time.sleep(60)

    time.sleep(15)



