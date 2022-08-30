import sys
from os import strerror
from string import ascii_lowercase
from collections import defaultdict, Counter

dictLetter = defaultdict(int) 
try:
	fo = open('D:\\Cursos Python\\__Zen ofpython.txt', 'rt') 
	x =0
	
	sLine= fo.readline().lower()
	while len(sLine) > 0:
		x+=1
		#sys.stdout.write("\n" + str(x) + " - line :" + sLine + "\n")

		CollCounter = Counter(sLine)
		for ch, v in CollCounter.items():
			if ch.isalpha():
				dictLetter[ch] += v
		sLine= fo.readline().lower()
	fo.close()

	#print ("\n", dictLetter)
	for k, v in sorted(dictLetter.items(), key=lambda item:item[1], reverse=True):
			print (k + " -> " + str(v))

except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))



