"""Get the meaning of an entire bunch of words that are written into a file"""

import sys

from get import get

def get_from_file(fname):

	with open(fname, "r+") as f:
		words = f.readlines()
		words = list(map(
			lambda x: x.rstrip("\n"), words))
		
		for index, word in enumerate(words):
			print(str(index) + ") " + word)
			get(word)

if __name__ == "__main__":

	fname = sys.argv[1]
	get_from_file(fname)