# -*- coding: utf-8 -*-
import futures
import urllib2

bidix = open("new_dict1")
f = open("html_response9","a")

urls = []


def load_url(url, timeout):
	html = urllib2.urlopen(url, timeout=timeout).read()
	hindi_word = url[url.find("=")+1:url.find("&")]

	if html.find("EXPRESSIONS") == -1:
		gender_index = html.find("noun") 
		if gender_index != -1:
			gender = html[gender_index + 5] 
			if gender == "m" or gender =="f":
				print gender
				f.write(hindi_word + "   " + gender+"\n")
			
	return html	
	
count = 0	
for line in bidix:	
	if line.find('<l>') != -1 and line.find('<s') != -1:
		word = line[(line.index('<l>') + 3) : line.index('<s')].replace('<b/>',' ')
		english_word = word.lower()
		part_of_speech = line.split('"')[1]
		line_split = line.split('</l>')
		
		if line_split[1].find('<s') != -1:		
			hindi_word   = line_split[1][(line_split[1].index('<r>') + 3) : line_split[1].index('<s')].replace('<b/>',' ')
		if part_of_speech == "n":
			if(line.find('"m"') == -1 and line.find ('"f"') == -1):	
				url = "http://hindi-english.org/index.php?input="+hindi_word+"&trans=Translate&direction=SE"
				count = count + 1
				urls.append(url)	
			
print count
with futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = dict((executor.submit(load_url, url, 60), url)
                        for url in urls)


