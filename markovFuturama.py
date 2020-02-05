import os, tweepy, markovify, sys
    
# Keys and Tokens to access @DJTwitterbot
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Determine which character file to open
args  = len(sys.argv)

if args == 1:
    character = 'bender'

elif args == 2:
    character = sys.argv[1]
    character = character.lower()

f = open('characterTotals\\' + character + '.txt', 'r')
character = character.capitalize()
text = markovify.Text(f)

# Generate and print sentences
sentence = '"' + text.make_sentence() + '" \n    ~' + character
print(sentence)
while len(sentence) > 280 or len(sentence) < 45:
    sentence = '"' + text.make_sentence() + '" \n    ~' + character
    print(sentence)

api.update_status(sentence)
