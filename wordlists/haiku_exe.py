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


'''
firstadjective = random.choice(open("AT-1.txt").readlines()).rstrip()
firstnoun = random.choice(open("NN-1.txt").readlines()).rstrip()
verb = random.choice(open("VBZ-1.txt").readlines()).rstrip()
secondadjective = random.choice(open("AT-1.txt").readlines()).rstrip()
secondnoun = random.choice(open("NN-1.txt").readlines()).rstrip()

firstVerb = random.choice(open("VB-3.txt").readlines()).rstrip()
secondVerb = random.choice(open("VB-3.txt").readlines()).rstrip()
    thirdVerb = random.choice(open("VB-1.txt").readlines()).rstrip()

    lastLineAdj = random.choice(open("JJ-2.txt").readlines()).rstrip()

    if firstadjective == "a" and (firstnoun[0] == 'a' or firstnoun[0] == 'e' or firstnoun[0] == 'i' or firstnoun[0] == 'o' or firstnoun[0] == 'u'):
        firstadjective = "an"

    if firstadjective == "an" and not((firstnoun[0] == 'a') or (firstnoun[0] == 'e') or (firstnoun[0] == 'i') or (firstnoun[0] == 'o') or (firstnoun[0] == 'u')):
        firstadjective = "a"

    if secondadjective == "a" and  (secondnoun[0] == 'a' or secondnoun[0] == 'e' or secondnoun[0] == 'i' or secondnoun[0] == 'o' or secondnoun[0] == 'u'):
        secondadjective = "an"

    if secondadjective == "an" and not(secondnoun[0] == 'a' or secondnoun[0] == 'e' or secondnoun[0] == 'i' or secondnoun[0] == 'o' or secondnoun[0] == 'u'):
        secondadjective = "a"

    firstLine = firstadjective + " " + firstnoun + " " + verb + " " + secondadjective + " " + secondnoun
    middleLine = firstVerb + ", " + secondVerb + ", " + thirdVerb
    lastLine = firstadjective + " " + firstnoun + " is " + lastLineAdj + "."
    '''


# start here

def make5line():
    rand = random.randint(1, 100)
    if (rand < 33):
        haikuline = a1s4p()
    elif (rand < 66):
        haikuline = a2s3p()
    else:
        haikuline = a3s2p()
    return haikuline


def a1s4p():
    noun = a1n()
    rand = random.randint(1, 3)
    if (rand == 1):
        predicate = a3v() + ' ' + a1n()
    elif (rand == 2):
        predicate = a2v() + ' ' + a2n()
    elif (rand == 3):
        predicate = a1v() + ' ' + a3n()
    line = noun + ' ' + predicate
    return line


def a2s3p():
    noun = a2n()
    rand = random.randint(1, 2)
    if (rand == 1):
        predicate = a2v() + ' ' + a1n()
    elif (rand == 2):
        predicate = a1v() + ' ' + a2n()
        line = noun + ' ' + predicate
    return line


def a3s2p():
    noun = a3n()
    predicate = a1v() + a1n()
    line = noun + ' ' + predicate
    return line


def a1n():
    noun = random.choice(open("NN-1.txt").readlines()).rstrip()
    return noun

def a2n():
    rand = random.randint(1, 2)
    if (rand == 1):
        string = a1a() + ' ' + a1n()
    else:
        string = random.choice(open("NN-2.txt").readlines()).rstrip()
    return string


def a3n():
    rand = random.randint(1, 3)
    if (rand == 1):
        string = a1a() + ' ' + a2n()
    elif (rand == 2):
        string = a2a() + ' ' + a1n()
    else:
        string = random.choice(open("NN-3.txt").readlines()).rstrip()
    return string


def a1v():
    verb = random.choice(open("VBZ-1.txt").readlines()).rstrip()
    return verb


def a2v():
    verb = random.choice(open("VBZ-2.txt").readlines()).rstrip()
    return verb


def a3v():
    rand = random.randint(1, 2)
    if (rand == 1):
        string = a2av() + ' ' + a1v()
    else:
        string = random.choice(open("VBZ-3.txt").readlines()).rstrip()
        return string


def a1a():
    rand = random.randint(1, 2)
    if (rand == 1):
        adj = random.choice(open("JJ-1.txt").readlines()).rstrip()
    else:
        adj = random.choice(open("AT-1.txt").readlines()).rstrip()
    return adj


def a2a():
    rand = random.randint(1, 2)
    if (rand == 1):
        adj = random.choice(open("JJ-2.txt").readlines()).rstrip()
    else:
        adj = random.choice(open("AT-1.txt").readlines()).rstrip() + " " + random.choice(
            open("JJ-1.txt").readlines()).rstrip()
    return adj


def a2av():
    adv = random.choice(open("RB-2.txt").readlines()).rstrip()
    return adv

while True:
    firstLine = make5line()
    print(firstLine)
    # middleLine = make7line() worry about this shit later
    lastLine = make5line()
    print(lastLine)

    # api.update_status(firstLine +"\n" + "\n" + lastLine)
    print("Tweeting!")
    i = i + 1
    time.sleep(90)  # Tweet every 2 minutes
    print("All done tweeting!")

    # python haiku_exe.py
    # cd C:\Users\ddgra\Desktop\haiku.exe\wordlists