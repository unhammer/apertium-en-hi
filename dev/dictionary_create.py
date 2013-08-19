import urllib2

r = open("hindi_word_list")
f = open("html_response3","w")
count = 1
for line in r:
	hindi_word = line[:-1]

	url = "http://dict.hinkhoj.com/hindi-dictionary.php?scode=dict_home&word="+hindi_word

	# This packages the request (it doesn't make it) 
	
	request = urllib2.Request(url)
	
	# Sends the request and catches the response

	response = urllib2.urlopen(request)

	# Extracts the response

	html = response.read()
	word = hindi_word
	start = 0
	print count
	while html.find('<span  onMouseOver=setYellowBG(this) onMouseOut=setWhiteBG(this) >',start) != -1 and html.find('डाटाबेस') == -1 :

		start = html.find('<span  onMouseOver=setYellowBG(this) onMouseOut=setWhiteBG(this) >',start) + 66
	
		word = html[start : html.find('</span>', start)]

		start = html.find('<span  onMouseOver=setYellowBG(this) onMouseOut=setWhiteBG(this) >',start) + 66
		english_word = html[start : html.find('</span>', start)].lower()
	
		start = html.find("<span class='gram_dict_span'>",start) + 29
		part_of_speech = html[start : html.find('</span>', start)][1:-1].lower()
		if word != hindi_word: 
			break;
		f.write(hindi_word+"," + english_word+ ","+part_of_speech+"\n")
			
	count = count + 1	
	