import time

import tweepy

import Chained_Translation
import Image

# Enter api keys
# consumer_key = 
# consumer_secret = 

# access_token = 
# access_token_secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def parse_tweet(text):
    if '\n' in text:
        return text.split('\n')[1]
    else:
        return ''.join(text.split(' ')[1:])


last_id = 1099665704842752100 + 200
while True:
    # last_id = int(api.search('@kagamitranslate')[0]._json['id']) + 100

    last_id += 100
    print(last_id)

    mentions = api.search('@kagamitranslate', since_id=last_id, rpp=1)
    print(mentions)

    for index, tweet in enumerate(mentions):
        user_id = tweet._json['user']['screen_name']
        print(user_id)
        print(tweet._json['text'])

        api.update_with_media(Image.TextImage(
            Chained_Translation.Translate(parse_tweet(tweet._json['text'])).word_list).file_location,
                              status="@" + user_id)
        if index == 0:
            last_id = tweet._json['id']

    time.sleep(20)
