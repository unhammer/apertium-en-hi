
# -*- coding: utf-8 -*-

import futures
import urllib2


r = open("hindi_word_list")

f = open("html_response4","w")


urls = []

count = 0




def load_url(url, timeout):

	html = urllib2.urlopen(url, timeout=timeout).read()

	start = 0

	print count
	while html.find('<span  onMouseOver=setYellowBG(this) onMouseOut=setWhiteBG(this) >',start) != -1 and html.find('डाटाबेस') == -1 :

		start = html.find('<span  onMouseOver=setYellowBG(this) onMouseOut=setWhiteBG(this) >',start) + 66
	
		word = html[start : html.find('</span>', start)]

		start = html.find('<span  onMouseOver=setYellowBG(this) onMouseOut=setWhiteBG(this) >',start) + 66
		english_word = html[start : html.find('</span>', start)].lower()
	
		start = html.find("<span class='gram_dict_span'>",start) + 29
		part_of_speech = html[start : html.find('</span>', start)][1:-1].lower()
		f.write(word+"," + english_word+ ","+part_of_speech+"\n")
	return html	

	
	
  for line in r:
	
	hindi_word = line[:-1]
	url = "http://dict.hinkhoj.com/hindi-dictionary.php?scode=dict_home&word="+hindi_word	
	urls.append(url)	

	
  with futures.ThreadPoolExecutor(max_workers=5) as executor:
    
	future_to_url = dict((executor.submit(load_url, url, 60), url)
                         for url in urls)

			

