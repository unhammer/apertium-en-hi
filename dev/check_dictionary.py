bidix = open("/home/nikant/Repository/git/apertium-en-hi/apertium-en-hi.en-hi.dix")


dictionary = {}




english_words = open("english_words_anlysed")



i = 0

for line in english_words:
	words = line.split("/")
		
	if len(words) > 1:
		word = words[1]
		if word.find("*") == -1:		
			pos = word[word.find("<") + 1: word.find(">")]
			i = i + 1		
			dictionary3[word[:word.find("<")]] = pos

for line in shabdanjali:
	words = line.split(",")
	dictionary[words[0][1:-1]] = words[1][1:-1] + "," +words[2][3:-2]

i = 0


previous_word = ""
for line in clift:
	words = line.split()
	hindi_word = words[0][1:-1]
	#print (words)
	if len(words) > 3:

		if words[2].find("(") == -1 and (len(words[2]) >2) and words[2][1].isalpha():
			english_word = words[2][1:-1]
		else:
			english_word = words[2][1:words[2].find("(")]
		
		if len(english_word) > 1 and english_word.isalpha() and previous_word != english_word :		
			dictionary1[english_word]  = hindi_word
			dictionary2[english_word] = words[3].split(",")[0].replace("(","").replace(")","").lower()		
			i = i+1
			previous_word = english_word
			#corrections_words.write(english_word + "   " + hindi_word + "   "+dictionary2[english_word]+ "\n")
		
		if i == 30000:
			break	


count = 0

adj = []
noun = []
adv = []




for line in bidix:
	flag = 0
	
	if line.find('<l>') != -1 and line.find('<s') != -1:
		english_word = line[(line.index('<l>') + 3) : line.index('<s')]
		part_of_speech = line.split('"')[1]

		line_split = line.split('</l>')
		
		if line_split[1].find('<s') != -1:		
			hindi_word   = line_split[1][(line_split[1].index('<r>') + 3) : line_split[1].index('<s')]
		english_word_list.write(english_word+"\n")
		hindi_word_list.write(hindi_word+"\n")
		if english_word in dictionary3  and (part_of_speech == "n" or part_of_speech == "adj" or part_of_speech == "adv") :
			if(dictionary3[english_word]!= part_of_speech and (dictionary3[english_word] == "n" or dictionary3[english_word] == "adj" or dictionary3[english_word] == "adv" )	):			
					line = line.replace('"'+part_of_speech+'"','"'+dictionary3[english_word]+'"')		
		#			count = count + 1
					#corrections_words.write(line[:-1] + "   " + dictionary3[english_word] + "\n")
					if dictionary3[english_word] == "adj":
						adj.append(line[:-1])
					if dictionary3[english_word] == "n":
						noun.append(line[:-1])
					if dictionary3[english_word] == "adv":
						adv.append(line[:-1])	
					flag = 1					
		#			english_words.write(english_word + "\n")
	if flag == 0:	
		new_words.write(line)


for item in adj:
	corrections_words.write(item  + "\n")

for item in noun:
	corrections_words.write(item + "\n")

for item in adv:
	corrections_words.write(item  + "\n")

#print ( dictionary2	)	

