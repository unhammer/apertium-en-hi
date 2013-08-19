
f = open("/home/nikant/Repository/git/apertium-en-hi/apertium-en-hi.hi.dix")
lines = f.readlines()
r = open("monodix_analysed","w")



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

for line in lines:
	if line.find("<e lm=") != -1:
		line_split = line.split('"')
		if(len(line_split) == 5):			
			hindi_word = line_split[1]
			paradigm = line_split[3]
			r.write(str(getInflectedForms(hindi_word,paradigm))+"\n")


