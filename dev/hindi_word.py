f = open('freq-analysis')
r = open('hindi_words',"w")


for line in f:

	words = line.split()
	if len(words) > 1:
		hindi_word = words[1][:words[1].find("<")]
	
		if len(hindi_word) != 0:	
			r.write(hindi_word+"\n")	
		