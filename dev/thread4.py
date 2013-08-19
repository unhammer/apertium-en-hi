# -*- coding: utf-8 -*-
import futures
import urllib2

bidix = open("new_dict1")
f = open("html_response9","a")

urls = []


def load_url(url, timeout):
	html = urllib2.urlopen(url, timeout=timeout).read()
	print html
	if html.find("Sorry") == -1:

		gender_index = html.find("Gender") 
		if gender_index != -1:
			gender = html[gender_index + 8] 
			print gender
	return html	
	
count = 0	
for line in bidix:	
	if line.find('<l>') != -1 and line.find('<s') != -1:
		word = line[(line.index('<l>') + 3) : line.index('<s')].replace('<b/>',' ')
		english_word = word.lower()
		part_of_speech = line.split('"')[1]
		if part_of_speech == "n":
			if(line.find('"m"') == -1 and line.find ('"f"') == -1):	
				url = "http://www.shabdkosh.com/hi/translate?e="+word+"&l=hi"
				count = count + 1
				urls.append(url)	
			
print count
with futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url = dict((executor.submit(load_url, url, 60), url)
                        for url in urls)


