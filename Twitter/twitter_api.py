from time import sleep
import os
import tweepy
import configparser
import pandas as pd

#read all the credentials of the config file

class Setting(object):

    def __init__(self, cfg_path):
        self.cfg = configparser.ConfigParser()
        #Sections before the read print(self.cfg.sections())
        #print(cfg_path)
        self.cfg.read(cfg_path)
        #Sections after the read print(self.cfg.sections())
        # Escribe en el archivo config.ini donde se encuentre la raiz del instalador configparser:
        #with open(cfg_path, "w") as configfile:
        #    self.cfg(configfile)

    def get_setting(self, section, my_setting):
        try:        
            ret = self.cfg.get(section, my_setting)
        except configparser.NoOptionError:
            ret = None
        return ret


if __name__ == '__main__':

    
    conf=Setting("Twitter/config.ini")
    API_KEY = conf.get_setting('twitter', 'api_key')
    print ('api key is :', API_KEY)
    API_KEY_SECRET = conf.get_setting('twitter', 'api_key_secret')
    print ('the secret api key  is :', API_KEY_SECRET)
    BEARER_TOKEN = conf.get_setting('twitter', 'BEARER_TOKEN')
    print ('the secret api key  is :', BEARER_TOKEN)
    ACCESS_TOKEN = conf.get_setting("twitter","ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = conf.get_setting("twitter","ACCESS_TOKEN_SECRET")

#autentication at the app
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    #get access to my tweets:
    public_tweets = api.home_timeline()
    #print(public_tweets) Get all the information from the tweets
    #print(public_tweets[0].text) Get the text for the first tweet
    #for tweet in public_tweets:
    #    print(tweet.text)
    #print(public_tweets[0].created_at) date of the created tweet
    #print(public_tweets[0].text) text of the created tweet
    #print(public_tweets[0].user.screen_name) date of the created tweet

    columns = ["Time", "User", "Tweet"]
    data = []
    for tweet in public_tweets:
        data.append([tweet.created_at, tweet.user.screen_name, tweet.text])
        
    print (data)
    df = pd.DataFrame(data, columns=columns)
    print(df)
    df.to_csv("Twitter/tweets.csv")

    #tweet = pd.json_normalize(response["data"])
    #client = tweepy.Client(
    #    bearer_token=BEARER_TOKEN,
    #    return_type = requests.Response # Needed to use json methods, which makes life much easier
    #)
    
    







"""
API_KEY_SECRET = config["twitter"]["API_KEY_SECRET"]


print(API_KEY)
"""