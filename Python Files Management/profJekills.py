import sys
import pathlib
from os import strerror, stat
from string import ascii_lowercase
from collections import defaultdict

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
	def __init__(self, sPath, message):
		Exception.__init__(self, message)
		self.sPath= sPath
		self.message = message

class FileEmpty(StudentsDataException):
	def __init__(self, sPath, message):
		Exception.__init__(self, message)
		self.sPath= sPath
		self.message = message

try:
	dictLetter = defaultdict(int) 
	sPath = str(pathlib.Path(__file__).parent.resolve())
	sPath += '\\prof Jekylls.txt'

	if stat(sPath).st_size == 0:
		raise FileEmpty(sPath, 'File is empty.!')
	
	#open source file
	fo = open(sPath, 'rt') 

	#read lines until empty	
	sLine= fo.readline()
	while len(sLine) > 0:
		sList = sLine.split()
		#Format Name as requested
		sName = sList[0] + " " + sList[1]
		#Student Points
		sPoint = sList[2]

		#print(sName +  " " + sPoint)
		dictLetter[sName ] += float(sPoint)
		#print(dictLetter)
		sLine= fo.readline()
	fo.close()

	for k, v in sorted(dictLetter.items(), key=lambda item:item[0], reverse=False):
			print (k + "\t" + str(v))

except BadLine as e:
	print(e.sPath, ':', e.message)
except FileEmpty as e:
	print(e.sPath, ':', e.message)
except IOError as e:
    print("File: " + sPath + " does not exists", strerror(e.errno))



