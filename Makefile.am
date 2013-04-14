VERSION=0.1.0
LANG1=en
LANG2=hi
PREFIX1=$(LANG1)-$(LANG2)
PREFIX2=$(LANG2)-$(LANG1)

BASENAME=apertium-$(PREFIX1)

##
##	BUILD TARGETS
##

TARGETS_COMMON =  \
     $(PREFIX1).automorf.bin $(PREFIX1).autobil.bin $(PREFIX1).autogen.bin \
     $(PREFIX2).automorf.bin $(PREFIX2).autobil.bin $(PREFIX2).autogen.bin \
     $(PREFIX1).t1x.bin  $(PREFIX1).t2x.bin $(PREFIX1).t3x.bin $(PREFIX1).mode \
     $(PREFIX2).t1x.bin  $(PREFIX2).t2x.bin $(PREFIX2).t3x.bin $(PREFIX2).mode

##
## 	DICTIONARIES (ANALYSER / BILINGUAL / GENERATOR / POSTGEN)
##


$(PREFIX1).automorf.bin: $(BASENAME).$(LANG1).metadix $(BASENAME).$(LANG1).acx
	@xsltproc buscaPar.xsl apertium-en-hi.en.metadix | uniq > tmp1gen.xsl          
	@xsltproc tmp1gen.xsl apertium-en-hi.en.metadix >$(BASENAME).$(LANG1).dixtmp1
	@rm tmp1gen.xsl
	apertium-validate-acx $(BASENAME).$(LANG1).acx
	apertium-validate-dictionary $(BASENAME).$(LANG1).dixtmp1
	lt-comp lr $(BASENAME).$(LANG1).dixtmp1 $@ $(BASENAME).$(LANG1).acx
	@rm $(BASENAME).$(LANG1).dixtmp1

	
$(PREFIX1).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
	lt-comp lr $(BASENAME).$(PREFIX1).dix $@

$(PREFIX1).autogen.bin: $(BASENAME).$(LANG2).dix
	apertium-validate-dictionary $(BASENAME).$(LANG2).dix
	lt-comp rl $(BASENAME).$(LANG2).dix $@

$(PREFIX2).automorf.bin: $(BASENAME).$(LANG2).dix
	apertium-validate-dictionary $(BASENAME).$(LANG2).dix
	lt-comp lr $(BASENAME).$(LANG2).dix $@

$(PREFIX2).autobil.bin: $(BASENAME).$(PREFIX1).dix
	apertium-validate-dictionary $(BASENAME).$(PREFIX1).dix
	lt-comp rl $(BASENAME).$(PREFIX1).dix $@

$(PREFIX2).autogen.bin: $(BASENAME).$(LANG1).metadix $(BASENAME).$(LANG1).acx
	@xsltproc buscaPar.xsl apertium-en-hi.en.metadix | uniq > tmp1gen.xsl          
	@xsltproc tmp1gen.xsl apertium-en-hi.en.metadix >$(BASENAME).$(LANG1).dixtmp1
	@rm tmp1gen.xsl
	apertium-validate-acx $(BASENAME).$(LANG1).acx
	apertium-validate-dictionary $(BASENAME).$(LANG1).dixtmp1
	lt-comp rl $(BASENAME).$(LANG1).dixtmp1 $@ $(BASENAME).$(LANG1).acx
	@rm $(BASENAME).$(LANG1).dixtmp1


##
##	TRANSFER RULES
##

$(PREFIX1).t1x.bin: $(BASENAME).$(PREFIX1).t1x
	apertium-validate-transfer $(BASENAME).$(PREFIX1).t1x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).t1x $@

$(PREFIX1).t2x.bin: $(BASENAME).$(PREFIX1).t2x
	apertium-validate-interchunk $(BASENAME).$(PREFIX1).t2x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).t2x $@

$(PREFIX1).t3x.bin: $(BASENAME).$(PREFIX1).t3x
	apertium-validate-postchunk $(BASENAME).$(PREFIX1).t3x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX1).t3x $@

$(PREFIX2).t1x.bin: $(BASENAME).$(PREFIX2).t1x
	apertium-validate-transfer $(BASENAME).$(PREFIX2).t1x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX2).t1x $@

$(PREFIX2).t2x.bin: $(BASENAME).$(PREFIX2).t2x
	apertium-validate-interchunk $(BASENAME).$(PREFIX2).t2x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX2).t2x $@

$(PREFIX2).t3x.bin: $(BASENAME).$(PREFIX2).t3x
	apertium-validate-postchunk $(BASENAME).$(PREFIX2).t3x
	apertium-preprocess-transfer $(BASENAME).$(PREFIX2).t3x $@


#
##	MODE FILE(S)
#
#
$(PREFIX1).mode: modes.xml 
	apertium-gen-modes modes.xml
	cp *.mode modes/

$(PREFIX2).mode: modes.xml 
	apertium-gen-modes modes.xml
	cp *.mode modes/

## 
##	FILES WHICH AREN'T BUILD BUT ARE DISTRIBUTED
## 

EXTRA_DIST=$(BASENAME).$(LANG1).metadix $(BASENAME).$(PREFIX1).dix \
	   $(BASENAME).$(LANG2).dix \
           $(PREFIX1).prob  \
	   $(BASENAME).$(PREFIX1).t1x $(BASENAME).$(PREFIX1).t2x \
	   $(BASENAME).$(PREFIX1).t3x\
	   $(BASENAME).$(LANG1).tsx \
	   modes.xml


#           $(LANG1)-tagger-data/README $(LANG2)-tagger-data/README 

apertium_en_hidir=$(prefix)/share/apertium/apertium-$(PREFIX1)/
apertium_en_modesdir=$(prefix)/share/apertium/modes/

apertium_en_hi_DATA=$(PREFIX1).automorf.bin \
                    $(PREFIX1).autobil.bin  \
                    $(PREFIX1).autogen.bin \
		    $(PREFIX1).t1x.bin \
		    $(PREFIX1).t2x.bin \
		    $(PREFIX1).t3x.bin \
                    $(PREFIX2).automorf.bin  \
                    $(PREFIX2).autobil.bin  \
                    $(PREFIX2).autogen.bin \
		    $(PREFIX2).t1x.bin \
		    $(PREFIX2).t2x.bin \
		    $(PREFIX2).t3x.bin \
                    $(PREFIX1).prob \
	            $(PREFIX1).mode modes.xml
		  
install-data-local:
	cp *.mode modes/
	apertium-gen-modes modes.xml apertium-$(PREFIX1)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX1).t1x $(apertium_en_hidir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX1).t2x $(apertium_en_hidir)
	$(INSTALL_DATA) $(BASENAME).$(PREFIX1).t3x $(apertium_en_hidir)

CLEANFILES = -rf $(TARGETS_COMMON) modes

