

clift = open("/home/nikant/Repository/git/apertium-en-hi/dev/UW_Hindi_Dict_20090403/UW-Hindi_Dict-20090403.txt")
missing_words = open("/home/nikant/Repository/git/apertium-en-hi/dev/freq-an")

dictionary1 = {}
dictionary2 = {}
present_words = {}
add_words={}
r = open("monodix_analysed")
corrected = open("new_corrected","w")

monolingual = []
bilingual = []
paradigm_map = {"f notch" : "ऊब__n_f" ,"m notch" : "ऐ__n_m","f NI" : "ध/ी__n_f","f NII" : "ध/ी__n_f","f Ni" : "नति__n_f" ,
"f Nu" : "हनु__n_f","f NA" : "ऊब__n_f","f NAA" : "ऊब__n_f","f Na" : "जड__n_f","f NU " : "खुशब/ू__n_f", "f NO" : "गौ__n_f","m NI" : "हठ/ी__n_m","m NII" : "हठ/ी__n_m","f NEE":"कला/ई__n_f","m NU" : "थ/ू__n_m","m Na" : "गम__n_m","m NA" : "ध/ा__n_m","m NAA" : "गम__n_m","m NAA" : "ध/ा__n_m","m NG" : "अडबंग__n_m","m NEE":"क/ई__n_m","m NAa":"पौ/आ__n_m"}

gender_map = {"male":"m","female":"f","m":"m","f":"f"}

f = open("/home/nikant/Repository/git/apertium-en-hi/apertium-en-hi.hi.dix")
lines = f.readlines()



def getPos(line):
	split = line.split('"')
	pos = []
	count = 1
	while count < len(split):
		pos.append(split[count])
		count = count + 2
	return pos
		
	
def getInflectedForms(hindi_word,paradigm):
	inflected_forms = []	
	for count in range(len(lines)):
		if lines[count].find(paradigm) != -1:

			count = count + 1
			while lines[count].find("</pardef>") == -1:

				pos = []
				if lines[count].find("<l>") != -1:
					pos = getPos(lines[count])
					inflected_word = hindi_word + lines[count][lines[count].find("<l>") +3 :lines[count].find("</l>")] 
					for item in pos:
						inflected_word = inflected_word + ","+item
					inflected_forms.append(inflected_word)
				count = count + 1
			break;
	return inflected_forms


previous_word = ""
i = 0
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
			dictionary1[hindi_word]  = english_word
			
			pos = words[3].replace("(","").replace(")","")
			pos_split = pos.split(",");
			ending = ""
			if pos_split[0].lower() == "n" and len(pos_split) > 2:	
				i = i+1
				ending = pos_split[-1]
			
				if pos_split[1] == "prop":
					dictionary2[hindi_word] = pos_split[0].lower() + "," + pos_split[2].lower() 
				else:
					dictionary2[hindi_word] = pos_split[0].lower() + "," + pos_split[1].lower() 
				if  len(hindi_word) > 1 and hindi_word[-1] == "ई":
					ending = "NEE"
				dictionary2[hindi_word] = dictionary2[hindi_word] + ","+ending
				if  len(pos_split) > 3 and "NOTCH" in pos_split:
					dictionary2[hindi_word] = dictionary2[hindi_word] + "," + pos_split[-2].lower()
								

			else:
				dictionary2[hindi_word] = pos_split[0].lower()	
							

			previous_word = english_word
			
			#corrections_words.write(english_word + "   " + hindi_word + "   "+dictionary2[english_word]+ "\n")
count = 0		


for line in missing_words:
	if len(line.split()) > 1 :	
		hindi_word = line.split()[1]
		if hindi_word in dictionary1:		
			add_words[hindi_word] = 1

	

for line in r:
	hindi_word = line[2:line.find("'",2)].split(",")[0]
	present_words[hindi_word] = 1

for word in dictionary1:
	if word not in present_words and word not in add_words:
		add_words[word] = 1

noun_count = 0
for hindi_word in add_words:
	pos = dictionary2[hindi_word] 
	pos_split = pos.split(",")
	if pos_split[0] == "n" and len(pos_split) > 2:

		key = ""
		if pos_split[1] in gender_map:
			gender = gender_map[pos_split[1]]		
			key = gender + " " + pos_split[-1]
			paradigm = ""
			if key in paradigm_map:
				
				paradigm = paradigm_map[key]									
				if paradigm.find("/") != -1:
					word = hindi_word[:-1]
				else:
					word = hindi_word
					
			else:
				if gender == "m":					
					paradigm =  "ऐ__n_m"
				else: 
					paradigm = "ऊब__n_f"
			monolingual_entry = '<e lm="'+hindi_word +'"><i>'+word+'</i><par n="'+paradigm+'"/></e>'
			bilingual_entry =   '<e><p><l>'+dictionary1[hindi_word]+'<s n="n"/></l><r>'+hindi_word+'<s n="n"/><s n="'+gender+'"/></r></p></e>'
			#if 	not dictionary1[hindi_word][0].isupper():		
			#	bilingual.append(bilingual_entry)
			#	monolingual.append(monolingual_entry)	
	
	elif pos_split[0] == "adj":				
		monolingual_entry = '<e lm="'+hindi_word +'"><i>'+hindi_word+'</i><par n="'+"जड__adj"+'"/></e>'
		bilingual_entry =   '<e><p><l>'+dictionary1[hindi_word]+'<s n="adj"/></l><r>'+hindi_word+'<s n="adj"/></r></p></e>'

		if 	not dictionary1[hindi_word][0].isupper():		
				bilingual.append(bilingual_entry)
				monolingual.append(monolingual_entry)	

for entry in monolingual:
	corrected.write(entry+"\n")
corrected.write("\n\n")	
for entry in bilingual:
	corrected.write(entry+"\n")

		
