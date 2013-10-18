from input import main
import unittest
import re

def splitline(docstring):
	# docstring = main.__doc__
	# Split lines in docstring
	lines = docstring.expandtabs().splitlines()
	# Make list of execute lines
	ex_lines = []
	for line in lines[1:]:
		stripped = line.strip()
		if stripped:
			ex_lines.append(stripped)
	return ex_lines

# Take list of numbers
# \s*: Skip space or not (\t\n\r\f\v), \d: Number [0-9]
# ?: Non-capturing version of regular parentheses
def get_first(line):
	first = re.compile("\s*(?:\[)(\d+)\s*(?:;)").findall(line)
	# Convert string to integer and return list
	return map(int, first)
def get_last(line):
	last = re.compile("\s*(?:;)(\d+)\s*(?:\])").findall(line)
	return map(int, last)
	
# Arrange classes
def arrange(first_int, last_int):
	i = 0
	while i < len(first_int)-1:
		if first_int[i] > first_int[i+1]:
			first_int[i], first_int[i+1] = first_int[i+1], first_int[i]
			last_int[i], last_int[i+1] = last_int[i+1], last_int[i]
		i += 1

# Check exception, return True if its wrong input, return False if its right input	
def check_exception(list):
	check = False
	for line in list:
		first_int = get_first(line)
		last_int = get_last(line)
		arrange(first_int, last_int)
	# Check exception
		j = 0
		while j < len(last_int)-1:
			if last_int[j] >= first_int[j+1]:
				check = True
				break
			else:
				j += 1
	return check

def testcase_generator(list):
	values = []
	for line in list:
		first_int = get_first(line)
		last_int = get_last(line)
		arrange(first_int, last_int)
		# Get the list of values for each variables
		values[len(values):] = [first_int]
	testcases = get_testcases(values)
	# Get list of code test
	l = []
	for testcase in testcases:
		l[len(l):] = [[len(l),testcase,"abc"]]
	return l

# Get list of testcases	
def get_testcases(values):
	testcases = []
	for value in values[0]:
		testcases.append([[value]])
	if len(values) >= 1:
		i = 1
		while i < len(values):
			testcases = [p+[q] for p in testcases for q in values[i]]
			i += 1
	return testcases
	
class TestSequense(unittest.TestCase):
    pass

def test_generator(a, b):
    def test(self):
        self.assertEqual(main(*a),b)
    return test

if __name__ == '__main__':
	x = splitline(main.__doc__)
	if check_exception(x):
		raise Exception("wrong input")
	else:
		l = testcase_generator(x)
		for t in l:
			test_name = 'test_%s' + str(t[0])
			test = test_generator(t[1], t[2])
			setattr(TestSequense, test_name, test)
		unittest.main()