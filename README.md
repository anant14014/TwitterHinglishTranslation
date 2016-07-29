#Introduction
This is the second programming assignment submitted as part of the Precog Research Group Recruitment Process.

The program uses the Twitter Search API to filter out Hindi-English code-mixed ('Hinglish') tweets. The tweets are then parsed, preprocessed and translated into pure English

#Requirements
	1. Python 2.7
	2. TwitterSearch
	3. Pickle
	4. JSON
	5. NLTK
	6. Codecs (Python Library)

Most of the dependencies can be installed using a python package manager like pip.

#Usage
	1. python getTweets.py >> tweets.txt
	2. python createDictionary.py
	3. python analyzeTweets.py

#Approach
A simple approach with minimal use of any APIs is implemented

## Filtering (getTweets.py)
	1. Used several datasets to create a list of the most commonly used Hindi words (in Roman/Latin script) on the web and their frequencies.
	2. Used the twitter REST API to search for tweets containing specific keywords (passed as pairs - single keywords like 'mujhe' were not effective. So instead, pairs of keywords were used like 'mujhe' AND 'tujhe'. This gave less false positives. Moreover, for words like 'me' 'tu' 'hi' etc. the other word must be a reasonably unqiue Hindi word.
	3. The retrieved tweets were then filtered for English words - a tweet passed the filter only if it contained at least 3 words for the NLTK English stopwords list
	4. Duplicates were deleted
	5. 921 (out of 25,800 tweets) passed the filters

## Dictionary Creation (createDictionary.py)
	1. First a dictionary that mapped from Hindi words in Roman script to Hindi words in Devanagari script was created using datasets containing pairs of such words
	2. Then, I used several datasets to create a dictionary that mapped from Hindi words (in Devanagari) to English words
	3. Finally, I created a dictionary that mapped from Hindi words in Roman Script to English words

## Translation
Given these dictionaries, translation was trivial: if a word in a tweet is not present in the list of English stopwords, it is translated.

#Output
The output is written to a file called "output.txt" in the working directory. The format is: Tweet\n Translated Tweet\n \n
		
#Challenges
	1. Nature of tweets - acronyms, spelling errors, lots of noisy data
	2. Lack of easy availability of high quality transliterated Hindi-English data

#Possible Optimizations
Given a larger timeframe, the following optimizations can be explored:
	1. Better datasets would significantly improve results - can be purchased, created etc
	2. A machine learning approach could be used for transliteration and detecting when a word is Hindi
	3. An RNN could be used to cross-reference dictionary resuts with context in the task of translation

#References and Datasets
	+https://www.atala.org/IMG/pdf/2.Das-TAL54-3.pdf
	+http://blog.alejandronolla.com/2013/05/15/detecting-text-language-with-python-and-nltk/
	+https://github.com/ckoepp/TwitterSearch
	+https://github.com/anoopkunchukuttan/crowd-indic-transliteration-data
	+http://www.cfilt.iitb.ac.in/~hdict/webinterface_user/
	+http://cse.iitkgp.ac.in/resgrp/cnerg/qa/fire13translit/
