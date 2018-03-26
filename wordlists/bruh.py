import tweepy, time, random
    
def make5line():
    random = randint(1, 100)
    if (random < 33):
            haikuline = a1s4p()
    elif (random < 66):
        haikuline = a2s3p()
    else:
        haikuline = a3s2p()
    return haikuline
    
def a1s4p():
    noun = a1n()
    random = randint(1, 4)
    if (random == 1):
        predicate = a3v() + ' ' + a1n()
    elif (random == 2):
        predicate = a2v() + ' ' + a2n()
    elif (random == 3):
        predicate = a1v() + ' ' + a3n()
    line = noun + ' ' + predicate
    return line
        
    
def a2s3p():
    noun = a2n()
    random = randint(1, 3)
    if (random == 1):
        predicate = a2v() + ' ' + a1n()
    elif (random == 2):
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
def a2n():
    random = randint(1, 3)
    if (random == 1):
      	string = a1a() + ' ' + a1n()
    else:
      	string = random.choice(open("NN-2.txt").readlines()).rstrip()
    return string
          
def a3n():
    random = randint(1, 4)
    if (random == 1):
      	string = a1a() + ' ' + a2n()
    elif (random == 2)
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
    random = randint(1, 3)
    if (random == 1):
      string = a2av() + ' ' + a1v()
    else:
      string = random.choice(open("VBZ-3.txt").readlines()).rstrip()
  	return string
        
def a1a():
    random = randint(1, 3)
    if (random == 1):
    	adj = random.choice(open("JJ-1.txt").readlines()).rstrip()
    else:
      adj = random.choice(open("AT-1.txt").readlines()).rstrip()
    return adj
        
def a2a():
    random = randint(1, 3)
    if (random == 1):
    	adj = random.choice(open("JJ-2.txt").readlines()).rstrip()
    else:
      adj = random.choice(open("AT-1.txt").readlines()).rstrip() + " " + random.choice(open("JJ-1.txt").readlines()).rstrip()
    return adj
        
def a2av():
    adv = random.choice(open("RB-2.txt").readlines()).rstrip()
    return adv
      
firstLine = make5line() 
print(firstline)
#middleLine = make7line() worry about this shit later
lastLine = make5line()
print(lastline)
    
#api.update_status(firstLine +"\n" + "\n" + lastLine)
print("Tweeting!")
i = i + 1
time.sleep(90) #Tweet every 2 minutes
print("All done tweeting!")

#python haiku_exe.py
#cd C:\Users\ddgra\Desktop\haiku.exe\wordlists