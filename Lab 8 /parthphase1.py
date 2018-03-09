import os
import nltk
import shutil
import numpy as np
import pprint
import re
import string
import matplotlib.pyplot as plt



def word_tokenize(line):
    words = re.split(r'\s',line)
    while '' in words:
        words.remove('')
    return words


def filterDict (data):
    badwords = []
    
    for key in data:
        if key.isnumeric():
            badwords.append(key)
        else:
            if key in list(string.punctuation):
                badwords.append(key)
    
    for word in badwords:
        del data[word]
        
    return data

def extract_n_words (dict_, n):
    sorted_dict = sorted(dict_, key=dict_.__getitem__)
    sorted_dict.reverse()
    return sorted_dict[:n]


# I am assuming files unziped before
# gunzip *.gz

english_docNameList = []
french_docNameList = []

# extract file paths to be processed
for root, dirs, files in os.walk('.'):
	for file in files:
		if file.endswith('.e'):
			english_docNameList.append( root + '/' + file )
		elif file.endswith('.f'):
			french_docNameList.append( root + '/' + file )


# frequency dictionary
english_dict = {}
french_dict = {}

# process each english file and update english_dict
for fileName in english_docNameList:
	file = open( fileName , encoding = "ISO-8859-1")

	for line in file:
		words = nltk.word_tokenize(line)
		
		for word in words:
			word = word.lower()
			
			if word not in english_dict:
				english_dict[word] = 1
			else:
				english_dict[word] += 1

	file.close()


# process each french file and update french_dict
for fileName in french_docNameList:
	file = open( fileName , encoding = "ISO-8859-1")

	for line in file:
		words = nltk.word_tokenize(line)
		
		for word in words:
			word = word.lower()
			
			if word not in french_dict:
				french_dict[word] = 1
			else:
				french_dict[word] += 1

	file.close()



english_dict = filterDict (english_dict)
french_dict = filterDict (french_dict)

e_freq = english_dict.values()
f_freq = french_dict.values()


# plotting English Frequency
plt.plot(e_freq)
plt.ylabel('English Freq')
plt.show()

# plotting French Frequency
plt.plot(f_freq)
plt.ylabel('French Freq')
plt.show()