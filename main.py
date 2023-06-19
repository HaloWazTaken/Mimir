import tweepy
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

#initialize twitter bot
consumer_key = 'nf4doCJIBCPhV2omwi9okGnTz'
consumer_secret = 'oR1OklVoWNAgiog492JeNoxhdGAvpREQZ5SLoU1gEfuE8hWqs4'
oauth_token = '1594028438662397954-3e8zPNY6uuJTCvd68wwCyRyxFhxQDw'
oauth_secret = 'bSU3oiJ0kmn4ygz9MONAalkbJuf0l9yXywFzyqCw6dFMT'

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



