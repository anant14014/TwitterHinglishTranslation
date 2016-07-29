import pickle

transliterate = {}
with open("Data/hindi_english_transliteration.txt") as f:
    for line in f:
       (key, val) = line.split()
       transliterate[key] = val

#print len(transliterate)

with open("Data/crowd-indic-transliteration-data-master/crowd_transliterations.hi-en.txt") as f:
    for line in f:
       (key, val) = line.split()
       transliterate[key] = val

#print len(transliterate)

for i in range(1, 19):
	filename = "Data/Hindi - Word transliteration pairs 2/Chat/" "user-" + str(i) + ".txt"
	file = open(filename, "r")
	english_sentence = file.readline()
	while (english_sentence != ''):
		english_sentence = file.readline()
		if (english_sentence=='\r\n'):
			english_sentence = file.readline()
		hindi_sentence = file.readline()
		english_words = english_sentence.split(';')
		hindi_words = hindi_sentence.split(';')
		for eword, hword in zip(english_words, hindi_words):
			transliterate[eword] = hword

#print len(transliterate)

for i in range(1, 19):
	filename = "Data/Hindi - Word transliteration pairs 2/Scenario/" "user-" + str(i) + ".txt"
	file = open(filename, "r")
	english_sentence = file.readline()
	while (english_sentence != ''):
		english_sentence = file.readline()
		if (english_sentence=='\r\n'):
			english_sentence = file.readline()
		hindi_sentence = file.readline()
		english_words = english_sentence.split(';')
		hindi_words = hindi_sentence.split(';')
		for eword, hword in zip(english_words, hindi_words):
			transliterate[eword] = hword

#print len(transliterate)

for i in range(1, 19):
	filename = "Data/Hindi - Word transliteration pairs 2/Dictation Experiment/" "user-" + str(i) + ".txt"
	file = open(filename, "r")
	english_sentence = file.readline()
	while (english_sentence != ''):
		english_sentence = file.readline()
		if (english_sentence=='\r\n'):
			english_sentence = file.readline()
		hindi_sentence = file.readline()
		english_words = english_sentence.split(';')
		hindi_words = hindi_sentence.split(';')
		for eword, hword in zip(english_words, hindi_words):
			transliterate[eword] = hword

#print len(transliterate)

hindi2eng = {}

with open("Data/UW_Hindi_Dict_20131003/UW-Hindi_Dict-20131003.txt") as f:
	for line in f:
		#print line.partition('[')[-1].rpartition(']')[0]
		#print line.partition('"')[-1].rpartition('"')[0]
		#print line.split()[0].split('[')[1].split(']')[0]
		hindi2eng[line.partition('[')[-1].rpartition(']')[0]] = line.partition('"')[-1].rpartition('"')[0]

with open("Data/UW_Hindi_Dict_20131003/hindi_function_word_dictionary.txt") as f:
	for line in f:
		#print line.partition('[')[-1].rpartition(']')[0]
		#print line.partition('"')[-1].rpartition('"')[0]
		#print line.split()[0].split('[')[1].split(']')[0]
		hindi2eng[line.partition('[')[-1].rpartition(']')[0]] = line.partition('"')[-1].rpartition('"')[0]

translate = {}

for element in transliterate:
	if (transliterate[element] in hindi2eng):
		translate[element] = hindi2eng[transliterate[element]]

# print len(translate)

translate_file = open("dictionary.pickle","wb")
pickle.dump(translate, translate_file)
translate_file.close()