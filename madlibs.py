#string concatenation (also known as how to put strings togehter)
#suppose we want to create a string that says "subscribe to _____"
youtuber = " "

#ways to do it
#print("subscribe to " + youtuber)
#print("subscribe to  {}".format.(youtuber))
#print(f'subscribe to {youtuber}')

adj = input("Adjective: ")
verb = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous person: ")
madlib = f"Computer programming is so {adj}! It makes me so excited all the time, \
I love to {verb}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)


