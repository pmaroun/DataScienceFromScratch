import random

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for __ in range (10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print ("older:", older_girl)
print ("either:", either_girl)
print ("both:", both_girls)
print("P(both | older):", both_girls / older_girl) #0.514 ~1/2
print("P(both | either):", both_girls / either_girl) #0.342 ~1/3

print ("bayes's theorem")
