import tweepy, time, random

CONSUMER_KEY = 'YEdJ0gW2MVJ0G2oiAiA5MEnmb'
CONSUMER_SECRET = 'i7wujPA3984OVCwZKgxSkxne8qs5ZhXGgWbvZdYfPfVtmc5dy3'
ACCESS_TOKEN = '974501511349915648-3NFWLIY8md0lwVCuS9BulCONSE5l0dM'
ACCESS_SECRET = 'ca7YpxwhOPFIFcxuAAudsiknock5GApfKXAWyKuKAh3Oz'


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

i = 0

firstadjective = random.choice(open("AT-1.txt").readlines()).rstrip()
firstnoun = random.choice(open("NN-1.txt").readlines()).rstrip()
verb = random.choice(open("VBZ-1.txt").readlines()).rstrip()
secondadjective = random.choice(open("AT-1.txt").readlines()).rstrip()
secondnoun = random.choice(open("NN-1.txt").readlines()).rstrip()

if firstadjective == "a" and (firstnoun[0] == 'a' or firstnoun[0] == 'e' or firstnoun[0] == 'i' or firstnoun[0] == 'o' or firstnoun[0] == 'u'):
    firstadjective = "an"

if firstadjective == "an" and not((firstnoun[0] == 'a') or (firstnoun[0] == 'e') or (firstnoun[0] == 'i') or (firstnoun[0] == 'o') or (firstnoun[0] == 'u')):
    firstadjective = "a"

if secondadjective == "a" and  (secondnoun[0] == 'a' or secondnoun[0] == 'e' or secondnoun[0] == 'i' or secondnoun[0] == 'o' or secondnoun[0] == 'u'):
    secondadjective = "an"

if secondadjective == "an" and not(secondnoun[0] == 'a' or secondnoun[0] == 'e' or secondnoun[0] == 'i' or secondnoun[0] == 'o' or secondnoun[0] == 'u'):
    secondadjective = "a"

finalstring = firstadjective + " " + firstnoun + " " + verb + " " + secondadjective + " " + secondnoun

while True:
    api.update_status(finalstring)
    print("Tweeting!")
    i = i + 1
    time.sleep(90) #Tweet every 2 minutes
    print("All done tweeting!")