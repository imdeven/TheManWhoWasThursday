import sys, os
import re

if __name__ == '__main__':
	
	with open('test.txt', 'r') as novel:
		novelText = novel.read()
	
	convertedText = re.sub(r'([A-Za-z]+)\'([A-Za-z]+)', r'\1$$$\2', novelText)
	convertedText = re.sub(r'\'([^\']*[,\.\?\-\!]+[^\']*)\'', r'"\1"', convertedText)
	convertedText = re.sub(r'\$\$\$', "'", convertedText)

	with open('conversionIdentified.txt', 'w') as result:
		result.write(convertedText)
