'''
Hola, Worldo
@author Sean Lander

Counts and sorts letters from a list of words from a
line-break delimited text document (one word per line)
'''

import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('words',type=argparse.FileType('r'))

	args = parser.parse_args()

	words_f = args.words

	letters = {}

	for line in words_f:
		line = line.strip()
		for letter in line:
			if letter not in letters:
				letters[letter] = 1
			else:
				letters[letter] += 1

	letters_sorted = sorted(letters.items(), key=lambda x: x[1])
	letters_sorted.reverse()

	count = 0

	for key,value in letters_sorted:
		if count > 10:
			break
		print(key, value)
		count += 1


if __name__ == "__main__":
	main()