import json
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
import pickle
import codecs

def parseTweetSet(tweets_data_path):
	tweets_text = []
	tweets_file = open(tweets_data_path, "r")
	english_stopwords_set = set(stopwords.words('english'))
	for line in tweets_file:
		tweet = json.loads(line)
		text = tweet['text']
		tokens = wordpunct_tokenize(text)
		words = [word.lower() for word in tokens]
		words_set = set(words)
		common_elements = words_set.intersection(english_stopwords_set)
		if (len(common_elements)>2):
			tweets_text.append(tweet['text'])

	tweets_text_set = set(tweets_text)
	#print len(tweets_text)
	#print len(tweets_text_set)
	#print tweets_text_set
	return list(tweets_text_set)

def translateHinglishTweets(tweets_text):
	counter = 0
	tweets_text_translated = []
	n = len(tweets_text)

	open_file = open("dictionary.pickle", "rb")
	dictionary = pickle.load(open_file)
	open_file.close()

	english_stopwords_set = set(stopwords.words('english'))

	for i in range(n):
		text = tweets_text[i]
		translated_text = ""
		tokens = wordpunct_tokenize(text)
		words = [word.lower() for word in tokens]
		for word in words:
			if word in english_stopwords_set:
				translated_text = translated_text + " " + word
			elif (word in dictionary):
				#print word + "-" + dictionary[word]
				translated_text = translated_text + " " + dictionary[word]
				counter = counter + 1
			else:
				translated_text = translated_text + " " + word
		tweets_text_translated.append(translated_text)

	#print counter
	return tweets_text_translated

def writeToFile(tweets_text, tweets_text_translated, filename):
	f = codecs.open(filename, 'w', encoding='utf8', errors='ignore')
	n = len(tweets_text)
	for i in range(n):
		f.write(tweets_text[i] + '\n')
		f.write(tweets_text_translated[i] + '\n')
		f.write('\n')
	f.close()

if __name__ == '__main__':
	tweets_data_path = 'tweets.txt'
	tweets_text = parseTweetSet(tweets_data_path)
	tweets_text_translated = translateHinglishTweets(tweets_text)
	#print len(tweets_text)
	#print len(tweets_text_translated)
	writeToFile(tweets_text, tweets_text_translated, 'output.txt')
	#tweets_data = processTweets(tweets_data_path)
	# tweets = pandizeTweets(tweets_data)
	# writeTweetsToExcel(tweets)