import sys, os
import re

if __name__ == '__main__':
	
	with open('test.txt', 'r') as novel:
		novelText = novel.read()
	
	#for things like G. K. Chesterton
	convertedText = re.sub(r'([A-Z])\.', r'\1$$$', novelText)
	#for Mr.
	convertedText = re.sub("Mr.", "Mr$$$", convertedText)

	#for full stops not followed by single quote
	convertedText = re.sub(r'\.(\s+)', r'.</s>\1<s>', convertedText)
	#for full stops followed by single quote
	convertedText = re.sub(r'\.\'(\s+)', r".</s>'\1<s>", convertedText)

	convertedText = re.sub(r"\? '", r'@@@', convertedText)
	#for question mark followed by space
	convertedText = re.sub(r'\?(\s+)', r'?</s>\1<s>', convertedText)
	#for question mark followed by single quote ending a sentence for example, 
	'''Then after a pause he added--
	'What do you call this tremendous President of yours?' '''
	convertedText = re.sub(r'\?\'(\s{2,})', r"?</s>'\1<s>", convertedText)
	#other case is in a sentence like 'Are you for real?' asked he. In this case <s></s> not required
	convertedText = re.sub(r'@@@(\s+)', r"?</s> '\1<s>", convertedText)

	#for exclamation mark not followed by single quote ending sentence
	convertedText = re.sub(r'\!\s([A-Z])', r'!</s> <s>\1', convertedText)
	#for exclamation mark followed by single quote ending sentence
	convertedText = re.sub(r'\!\'(\s+)([A-Z])', r"!</s>'\1<s>\2", convertedText)
	convertedText = re.sub(r'\!\'(\s+)(\'[A-Z])', r"!</s>'\1<s>\2", convertedText)

	convertedText = re.sub(r'<s>$', '', convertedText)

	convertedText = re.sub(r'\n<s>([A-Z ]+)\n', r'\n\1\n', convertedText)
	convertedText = re.sub(r'\n<s>([A-Z$ ]+)\n', r'\n\1\n', convertedText)

	convertedText = re.sub(r'\n\n([A-Z][A-Za-z, ]*\n[A-Za-z, ]*\.</s>)', r'\n\n<s>\1', convertedText)

	#replace our introduced $$$ back with stops
	convertedText = re.sub(r'\$\$\$', ".", convertedText)

	with open('terminatorTaggedText.txt', 'w') as result:
		result.write(convertedText)
