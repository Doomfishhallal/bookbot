import sys
if len(sys.argv)==2:
	path = sys.argv[1]
else:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def count_words(path):
	with open(path) as f:
	        splits = f.read()
	banana = splits.split()
	for i in range(0, len(banana)):
	        i += 1
	print("----------- Word Count -----------")
	print("Found",i,"total words")
	print("--------- Character Count ---------")

def count_letters(path):
	with open(path) as f:
        	splits = f.read()
	splits = splits.lower()
	bananas = list(splits)
	for i in range(len(bananas)-1, -1, -1):	
		if not bananas[i].isalpha():
			del bananas[i]
	letters = {}
	for banana in bananas:
        	if banana in letters:
            		letters[banana] += 1
        	else:
            		letters[banana] = 1
	letters = [{"char": k, "num": v} for k, v in letters.items()]
	def sort_on(items):
		return items["num"]	
	letters.sort(reverse=True, key=sort_on)
	for letter in letters:
		print(f'{letter["char"]}: {letter["num"]}')
	print("============= END =============")

count_words(path)
count_letters(path)

