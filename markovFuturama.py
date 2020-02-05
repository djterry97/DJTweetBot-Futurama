import os, tweepy, markovify, sys
    
# Keys and Tokens to access @DJTwitterbot
consumer_key = 's9TGxOnUOxDag7P0T93MSxKkv'
consumer_secret = 'U2PwUyOd7qYOnDSbD8evy8Ebff1dlpjK0onYzpxKpEob3BoOng'
access_token = '1059596360171876352-TUe8IJFXpGCTxVQczXZgg4LqroTDpn'
access_secret = 'hMti3N1ZlVxQAlqw6dFucipANxJcl0bfCZvdO0StxuET2'

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
