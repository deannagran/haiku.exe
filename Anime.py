import tweepy, time

CONSUMER_KEY = 'ZnFJoAvuD8e0hrBNk1BR2zNdZ'
CONSUMER_SECRET = 'iAqZBQhfxWhHyJiHzRrJKsv9zPu1qJZqlngDLZmBYEJKtRrHaA'
ACCESS_TOKEN = '974419809898323974-TXIF9nLDbWYWywW8Qf4R74BtGocjdns'
ACCESS_SECRET = '0nOZEM9JNeGffTQIfdIMG9jT5o0x4cZkXaAp5Ho4MVVue'


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

i = 0

while True:
    api.update_status("Anime was \n a mistake " + str(i))
    print("Tweeting!")
    i = i + 1
    time.sleep(90) #Tweet every 2 minutes
    print("All done tweeting!")