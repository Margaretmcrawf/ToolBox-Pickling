""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
import pickle

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
	if not reset:
		try:
			input_file = open(file_name, 'r')
			s = pickle.load(input_file) + 1
		except IOError:
			s = 1
	else:
		s = 1
	#make and pickle the file
	f = open(file_name, 'w')
	pickle.dump(s, f)
	f.close()
	return s

		

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		#doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
	print update_counter('nope2.txt')
