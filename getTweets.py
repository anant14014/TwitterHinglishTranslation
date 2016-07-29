from collections import Counter
import operator

try:
    import json
except ImportError:
    import simplejson as json

from TwitterSearch import *

words = []

for i in range(1, 19):
	filename = "Data/Hindi - Word transliteration pairs 2/Chat/" "user-" + str(i) + ".txt"
	file = open(filename, "r")
	c = 2
	for line in file:
		if (c%2==0):
			words.extend(line.split(';'))
		if line != '\r\n':
			c = c + 1

for i in range(1, 19):
	filename = "Data/Hindi - Word transliteration pairs 2/Dictation Experiment/" "user-" + str(i) + ".txt"
	file = open(filename, "r")
	c = 2
	for line in file:
		if (c%2==0):
			words.extend(line.split(';'))
		if line != '\r\n':
			c = c + 1

for i in range(1, 19):
	filename = "Data/Hindi - Word transliteration pairs 2/Scenario/" "user-" + str(i) + ".txt"
	file = open(filename, "r")
	c = 2
	for line in file:
		if (c%2==0):
			words.extend(line.split(';'))
		if line != '\r\n':
			c = c + 1

word_counts = Counter(words)
#print(word_counts)
sorted_word_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_word_counts[:20])

# Variables that contain the user credentials to access Twitter API 
ACCESS_TOKEN = '3300772537-UwfYYD7VWnW4O1KxKRgfjjhd6bTBSECgN8N95KP'
ACCESS_SECRET = 'D62GjVqvpsHPrFvL1qztCRYnrnqJsj9JRDJgdSmz4SKUi'
CONSUMER_KEY = 'iusl4lLcAfnidQ1RmYO3dD5NP'
CONSUMER_SECRET = 'HNQ3uTsUO1bv27CXzK4tuvIr9LLhPh2W9ovBFrWHYsPhYgEHFr'

tweets = []

try:
	# it's about time to create a TwitterSearch object with our secret tokens
	ts = TwitterSearch(
	    consumer_key = CONSUMER_KEY,
	    consumer_secret = CONSUMER_SECRET,
	    access_token = ACCESS_TOKEN,
	    access_token_secret = ACCESS_SECRET
	)
	tso = TwitterSearchOrder() # create a TwitterSearchOrder object
	for i in range(1, 20):
		for j in range(1, 20):
			if (i!=j) and (sorted_word_counts[i][0] != 'me') and (sorted_word_counts[i][0] != 'hi') and (sorted_word_counts[i][0] != 'is'):
				tso.set_keywords([sorted_word_counts[i][0], sorted_word_counts[j][0]]) # let's define all words we would like to have a look for
				#tso.set_language('hi') # we want to see German tweets only
				tso.set_include_entities(False) # and don't give us all those entity information
				for tweet in ts.search_tweets_iterable(tso):
					# print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
					print json.dumps(tweet)


except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

#stream.filter(track=['main', 'woh', 'tu', 'aisa', 'waisa', 'kaun', 'hoon', 'ayega', 'jayega', 'gaya', 'aaya', 'kab', 'jab', 'mujhe', 'tujhe', 'kaise', 'kyun', 'bol', 'kabhi', 'tabhi'])