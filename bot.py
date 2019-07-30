# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:18:37 2019

@author: giuse
"""
import tweepy  
import telepot
from twitter_app_credentials import *

def OAuth():
    try:
        auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        return auth 
    except Exception as e:
        return None
    
oauth= OAuth()
api = tweepy.API(oauth)
bot = telepot.Bot(TOKEN_giuschilbot)

def send_tweet():
    public_tweets = tweepy.Cursor(api.search,q=("inter","calciomercato"),result_type="mixed",tweet_mode="extended").items(10)
    return public_tweets
    
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        bot.sendMessage(chat_id, 'Ciao sono un bot stupido questi sono gli utlimi tweet: ')
        for tweet in public_tweets:
            tweet_text = tweet.full_text
            bot.sendMessage(chat_id,tweet_text)
        

bot = telepot.Bot(TOKEN_giuschilbot)
bot.message_loop(on_chat_message)

print ('Listening ...')
import time
while 1:
    time.sleep(10) 

     

    