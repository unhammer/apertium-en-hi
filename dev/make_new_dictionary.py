f = open('handle_response.txt')
map = {'n': 'noun' ,'adj':'adjective','adv':'adverb','post':'preposition','cnjcoo':'conjunction','v':'verb','tv':'transitiveverb','iv':'intransitiveverb'}

new_dict = open('new_dict1',"w")

dictionary = {}
l = open("hindi_words")
f = open("handle_response.txt")
pos_dict = {}

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
				

for line in l:
	hindi_word = line[:-1]
	for pos in map.keys():
		key = hindi_word +","+map[pos]
		
		if ( key in dictionary):
			english_word = dictionary[key].split(",")[0]
			if english_word.isalpha():
				entry = "<e><p><l>"+english_word+'<s n="'+pos+'"/></l><r>'+hindi_word+'<s n="'+pos+'"/></r></p></e>'+"\n"
		
				if pos not in pos_dict:
					pos_dict[pos]= entry
				else:
					pos_dict[pos] = pos_dict[pos]  +  entry
						
				
for pos in pos_dict.keys():
	new_dict.write(pos_dict[pos] + "\n\n\n")			
			
		
	
	
					
f.close()				
