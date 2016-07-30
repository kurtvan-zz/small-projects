# Challenge #270 generating text with markov chains
# Started on 	24 - July - 2016
# Finished on 	25 - July - 2016 
# -------------------------------------------------

import random

PREFIX_SIZE = 2
LIMIT = 200

paragraph_size = 100

class Ngram():
	# holds a series of prefix words and a list of their suffixes

	def __init__(self, n):
		self.n = n
		self.prefixes = []
		self.suffixes = []

	def prefix_exists(self, check_prefix):
		"""
		Return True if check_prefix is in the list of
		prefixes.  return False otherwise
		"""
		for prefix in self.prefixes:
			
			i = 0
			found = True

			for word in prefix:
				if word != check_prefix[i]:
					found = False
				i += 1
			
			if found == True:
				return True

		return False

	def prefix_index(self, check_prefix):
		"""
		return the index of the check_prefix.  return
		-1 if it does not exist
		"""

		i = 0
		for prefix in self.prefixes:
			j = 0
			found = True

			for word in prefix:
				if word != check_prefix[j]:
					found = False
				j += 1
			
			if found == True:
				return i
			i += 1

		return -1

	def add_pair(self, add_prefix, add_suffix):

		if self.prefix_exists(add_prefix):
			self.suffixes[self.prefix_index(add_prefix)].append(add_suffix)
		else:
			self.prefixes.append(add_prefix)
			self.suffixes.append([add_suffix])

	def get_random_prefix(self):

		index = random.randint(0, len(self.prefixes) - 1)
		return self.prefixes[index]


	def get_suffix(self, cur_prefix):

		possible = self.suffixes[self.prefix_index(cur_prefix)]
		index = random.randint(0, len(possible) - 1)
		return possible[index]


##
## MAIN SCRIPT
##
if __name__ == "__main__":
	#first, we generate a list of words from the given text file
	file = open("trainer.txt", 'r')

	words = []
	linecount = 0

	# iterate through lines in training file
	for line in file:

		linecount += 1
		clean = line.lower()

		for word in clean.split():
			words.append(word.strip('.<>/,\"\''))

		if linecount == LIMIT:
			break

	file.close()

	#now, generate Ngrams from the word list
	prefix_to_suffix = Ngram(PREFIX_SIZE)

	i = 0

	while i < (len(words) - (PREFIX_SIZE)):

		prefix = []

		for j in range(0, PREFIX_SIZE):
			prefix.append(words[i+j])

		suffix = words[i + PREFIX_SIZE]
		prefix_to_suffix.add_pair(prefix, suffix)

		i += 1


	# generate the random paragraph from the generated Ngram set
	paragraph = ""

	prefix = prefix_to_suffix.get_random_prefix() # get random prefix to start

	# start with these 2 words first
	for word in prefix:
		paragraph = paragraph + word + " "


	for i in range(paragraph_size):
		new_word = prefix_to_suffix.get_suffix(prefix)
		paragraph = paragraph + new_word + " "

		prefix = [prefix[1], new_word]

		if i == paragraph_size - 1:
			if paragraph[-1] != '.':
				paragraph = paragraph[:-1] + "."


	paragraph = paragraph[0].upper() + paragraph[1:]

	print paragraph