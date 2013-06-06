#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys;

def mangle_flexion_tags(a): #{
	a = a.replace('actv', 'v0');
	a = a.replace('midv', 'v1');

	a = a.replace('inf', 'e0');
	a = a.replace('supn', 'e1');
	a = a.replace('pri', 'e2');
	a = a.replace('prs', 'e3');
	a = a.replace('psi', 'e4');
	a = a.replace('pss', 'e5');
	a = a.replace('imp', 'e6');
	a = a.replace('ppres', 'e7');
	a = a.replace('pp', 'e8');

	a = a.replace('pst', 'g1');
	a = a.replace('comp', 'g2');
	a = a.replace('sup', 'g3');

	a = a.replace('nom', 'c0');
	a = a.replace('acc', 'c3');
	a = a.replace('gen', 'c4');
	a = a.replace('dat', 'c5');
	a = a.replace('loc', 'c6');
	a = a.replace('ins', 'c7');
	a = a.replace('voc', 'c8');

	a = a.replace('ind', '0a');
	a = a.replace('def', 'x9');

	a = a.replace('sg', 'n1');
	a = a.replace('du', 'n2');
	a = a.replace('pl', 'n3');
	a = a.replace('ct', 'n4');

	a = a.replace('mf', 'a4');
	a = a.replace('m', 'a1');
	a = a.replace('f', 'a2');
	a = a.replace('nt', 'a3');

	return a;
#}

def demangle_flexion_tags(a): #{
	a = a.replace('v0', 'actv');
	a = a.replace('v1', 'midv');

	a = a.replace('e0', 'inf');
	a = a.replace('e1', 'supn');
	a = a.replace('e2', 'pri');
	a = a.replace('e3', 'prs');
	a = a.replace('e4', 'psi');
	a = a.replace('e5', 'pss');
	a = a.replace('e6', 'imp');
	a = a.replace('e7', 'ppres');
	a = a.replace('e8', 'pp');

	a = a.replace('g1', 'pst');
	a = a.replace('g2', 'comp');
	a = a.replace('g3', 'sup');

	a = a.replace('0a', 'ind');
	a = a.replace('x9', 'def');

	a = a.replace('a4', 'mf');
	a = a.replace('a1', 'm');
	a = a.replace('a2', 'f');
	a = a.replace('a3', 'nt');

	a = a.replace('n1', 'sg');
	a = a.replace('n2', 'du');
	a = a.replace('n3', 'pl');
	a = a.replace('n4', 'ct');

	a = a.replace('c0', 'nom');
	a = a.replace('c3', 'acc');
	a = a.replace('c4', 'gen');
	a = a.replace('c5', 'dat');
	a = a.replace('c6', 'loc');
	a = a.replace('c7', 'ins');
	a = a.replace('c8', 'voc');
	
	return a;
#}

def sort_flexions_by_key(a): #{
	if len(a) > 1:
		return mangle_flexion_tags(a[1])
	else:
		return ''
#}


# lemma    ;  surface form       ;  symbols                  ;  part-of-speech
# uttanbíggjamaður;  uttanbíggjamenninir;  definite, plural, nominative;  noun, masculine

def find_longest_common_substring(lemma, flexion): #{
	candidate = '';
	length = len(lemma);
	for char in lemma: #{
		candidate = candidate + char;
		#print >> sys.stderr , 'cand: ' , candidate , '; flexion:', flexion;
		if candidate not in flexion: #{
			return candidate[:-1];
		#}
	#}
	#print >> sys.stderr , 'cand: ' , candidate
	return candidate;
#}

# returns the shortest string from a given list
def return_shortest(ilist): #{

	#if ilist is empty
	if not ilist: #{
		return -1;
	#}

	return sorted(ilist, key=len)[0]
#}

def return_symlist(symlist): #{
	symlist = symlist.replace(':', '.');
	output = '';

	for symbol in symlist.split('.'): #{
		output = output + '<s n="' + symbol + '"/>';
	#}

	return output;
#}


#
#       MAIN
#


if len(sys.argv) < 2: #{
	print('python speling-paradigms.py <filename>');
	sys.exit(-1)

flist = open(sys.argv[1], 'r');
llist = flist.readlines();

current_lemma = '';

lemmata = {};
category = {};
flexions = {};

for line in llist: #{

	if len(line) < 2: #{
		continue;
	#}
	row = line.split(';');
	lemma = row[0].strip();

	current_lemma = lemma;
	if current_lemma not in lemmata: #{
		lemmata[current_lemma] = {};
	#}
	if current_lemma not in flexions: #{
		flexions[current_lemma] = {};
	#}
	if current_lemma not in category: #{
		category[current_lemma] = {};
	#}

	inflection = row[1].strip();
	if lemma.islower(): #{
		inflection = inflection.lower();	
	#}
	#print lemma , ' / ' , inflection;
	full = inflection;
	stem = find_longest_common_substring(lemma, inflection);
	pos = row[3].strip();
	syms = row[2].strip();
	symlist = pos + ':' + syms;

	#print lemma , '; ' , stem , '; -' + inflection , '; ' , full , '; ' + pos + '; ' + syms;

	form = (inflection, symlist);

	if pos not in lemmata[current_lemma]: #{
		lemmata[current_lemma][pos] = [];
	#}
	if pos not in flexions[current_lemma]: #{
		flexions[current_lemma][pos] = [];
	#}
	if pos not in category[current_lemma]: #{
		category[current_lemma][pos] = '';
	#}

	if form not in flexions[current_lemma][pos]: #{
		lemmata[current_lemma][pos].append(stem);
		flexions[current_lemma][pos].append(form);
		#category[current_lemma][pos] = pos.split('.')[0];
		category[current_lemma][pos] = pos.replace('.', '_');
	#}

#}

print('<dictionary>');
print('  <pardefs>');

for lemma in lemmata: #{
	for pos in lemmata[lemma]: #{
		stem = return_shortest(lemmata[lemma][pos]);
		print(stem, file=sys.stderr)
		print('  <!-- ' + lemma + '; ' +
		      stem + '; ' + str(len(flexions[lemma][pos])) + ' -->');
		end = lemma.replace(stem, '', 1);
		slash = '/';

		if end == '': #{
			slash = '';
		#}

		print('    <pardef n="' + stem + slash + end +
		      '__' + category[lemma][pos] + '">');
		
		flexions[lemma][pos].sort(key=sort_flexions_by_key);

		for pair in flexions[lemma][pos]: #{
			out = '';
			if len(pair[0]) > 1: #{
				out += ('      <e>       <p><l>' +
				pair[0].replace(stem, '',
				1).replace(' ', '<b/>') + '</l>');
			#}
			if len(pair[0]) == 1: #{
				out += ('      <e>       <p><l>' +
				pair[0].replace(' ', '<b/>') + '</l>');
			#}
			if len(pair[0]) < 1: #{
				out += '      <e>       <p><l/>';
			#}
			out += ('<r>' + end +
			return_symlist(pair[1]) + '</r></p></e>');
			print(out);
		#}
		
		#}
		print('    </pardef>');
		print('');
	#}
#}
print('  </pardefs>');
print('  <section id="main" type="standard">');

for lemma in lemmata: #{
	for pos in lemmata[lemma]: #{
		stem = return_shortest(lemmata[lemma][pos]);
		end = lemma.replace(stem, '',1);
		slash = '/';

		if end == '': #{
			slash = '';
		#}


		print('    <e lm="' + lemma + '"><i>' + stem +
		      '</i><par n="' +  stem + slash + end + '__' +
		      category[lemma][pos] + '"/></e>');
	#}
#}

print('  </section>');
print('</dictionary>');
