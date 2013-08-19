f = open('html_response')
dictionary = {}
d = open('dictionary',"w")
bidix = open("new_dict")
map = {'n': 'noun' ,'adj':'adjective','adv':'adverb','prep':'preposition','cnjcoo':'conjunction'}
analysed = {}
new_dict = open('new_dict1',"w")
k = open("word_list.txt")
useless = open("useless","w")

english_dictionary = {}
l = open("word_list2.txt")
for line in k:
	english_dictionary[line[:-1]] = 1
for line in l:
	word = line.split()[0].lower()
	if word not in dictionary:
		english_dictionary[word] = 1
for line in f:
	
	words = line[:-1].split(",")
	if len(words) == 3:
		hindi_word = words[0]
		english_word = words[1]
		part_of_speech = words[2]
		
		key = hindi_word+","+part_of_speech
		
		if  key not in dictionary:
			dictionary[key] = english_word			
		else:
			if english_word not in dictionary[key].split(","):
				dictionary[key] = dictionary[key] + "," + english_word
				
for line in bidix:
	flag = 0
	
	if line.find('<l>') != -1 and line.find('<s') != -1:
		word = line[(line.index('<l>') + 3) : line.index('<s')].replace('<b/>',' ')
		english_word = word.lower()
		part_of_speech = line.split('"')[1]
		
		line_split = line.split('</l>')
		
		if line_split[1].find('<s') != -1:		
			hindi_word   = line_split[1][(line_split[1].index('<r>') + 3) : line_split[1].index('<s')].replace('<b/>',' ')
		
		key = english_word + " " + part_of_speech +" "+hindi_word
		if  key not in analysed and (english_word in english_dictionary  or english_word == "prpers" or english_word.find(" ") != -1 or len(english_word) == 1 or word[0].isupper() ):
			analysed[key] = 1
			#d.write(english_word +"   "+ line)
		
		else:
			useless.write(line)
			flag = 1
		
	if flag == 0:
		new_dict.write(line)

					
f.close()				
