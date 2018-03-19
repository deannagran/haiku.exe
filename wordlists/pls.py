import random 


firstadjective = random.choice(open("AT-1.txt").readlines()).rstrip()

firstnoun = random.choice(open("NN-1.txt").readlines()).rstrip()

verb = random.choice(open("VBZ-1.txt").readlines()).rstrip()

secondadjective = random.choice(open("AT-1.txt").readlines()).rstrip()

secondnoun = random.choice(open("NN-1.txt").readlines()).rstrip()

if firstadjective == "a" and (firstnoun[0] == 'a' or firstnoun[0] == 'e' or firstnoun[0] == 'i' or firstnoun[0] == 'o' or firstnoun[0] == 'u'):
    firstadjective = "an"

print(firstadjective == "an" and not((firstnoun[0] == 'a') or (firstnoun[0] == 'e') or (firstnoun[0] == 'i') or (firstnoun[0] == 'o') or (firstnoun[0] == 'u')))

if firstadjective == "an" and not((firstnoun[0] == 'a') or (firstnoun[0] == 'e') or (firstnoun[0] == 'i') or (firstnoun[0] == 'o') or (firstnoun[0] == 'u')):
    firstadjective = "a"

if secondadjective == "a" and  (secondnoun[0] == 'a' or secondnoun[0] == 'e' or secondnoun[0] == 'i' or secondnoun[0] == 'o' or secondnoun[0] == 'u'):
    secondadjective = "an"

print (secondadjective == "an" and not(secondnoun[0] == 'a' or secondnoun[0] == 'e' or secondnoun[0] == 'i' or secondnoun[0] == 'o' or secondnoun[0] == 'u'))

if secondadjective == "an" and not(secondnoun[0] == 'a' or secondnoun[0] == 'e' or secondnoun[0] == 'i' or secondnoun[0] == 'o' or secondnoun[0] == 'u'):
    secondadjective = "a"

finalstring = firstadjective + " " + firstnoun + " " + verb + " " + secondadjective + " " + secondnoun


print(finalstring)