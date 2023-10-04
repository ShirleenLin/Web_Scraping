import os
import tweepy
import pandas as pd
from tqdm import tqdm, notebook

auth = tweepy.OAuthHandler(os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_SECRET")) #export TWITTER_API_KEY=...   - set up the environment variable in the terminal
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = list(tqdm(tweepy.Cursor(api.search_tweets, q="#interestrate -filter:retweets", lang="en", since="2023-01-01").items(500)))

def extract_tweet(tweet):
    try:
        hashtags = [i["text"] for i in tweet.entities["hashtags"]]
        text = api.get_status(id=tweet.id, tweet_mode='extended').full_text  #tweet.text if within the 280-character limit
    except Exception as e: print(e)
    tweet_data = {'user_name': tweet.user.name, 'user_location': tweet.user.location, 'user_description': tweet.user.description, 'user_created': tweet.user.created_at, 'user_followers': tweet.user.followers_count, 'user_friends': tweet.user.friends_count, 'user_favourites': tweet.user.favourites_count, 'user_verified': tweet.user.verified, 'date': tweet.created_at, 'text': text, 'hashtags': hashtags if hashtags else None, 'source': tweet.source, 'is_retweet': tweet.retweeted}
    return tweet_data

tweets = list(map(extract_tweet, tqdm(tweets)))
tweets_df = pd.DataFrame(tweets)

print(tweets_df.head())
