TMPDIR=/tmp

xsltproc ../buscaPar.xsl ../apertium-en-hi.en.metadix | uniq > ../tmp1gen.xsl          
xsltproc ../tmp1gen.xsl ../apertium-en-hi.en.metadix > ../apertium-en-hi.en.dixtmp1
rm ../tmp1gen.xsl

lt-expand ../apertium-en-hi.en.dixtmp1 | grep -v '<prn><enc>' | grep -e ':<:' -e '\w:\w' | sed 's/:<:/%/g' | sed 's/:/%/g' | cut -f2 -d'%' |  sed 's/^/^/g' | sed 's/$/$ ^.<sent>$/g' | tee $TMPDIR/tmp_testvoc1.txt |
        apertium-pretransfer|
        apertium-transfer ../apertium-en-hi.en-hi.t1x  ../en-hi.t1x.bin  ../en-hi.autobil.bin |
         apertium-interchunk ../apertium-en-hi.en-hi.t2x  ../en-hi.t2x.bin |
        apertium-postchunk ../apertium-en-hi.en-hi.t3x  ../en-hi.t3x.bin  |tee $TMPDIR/tmp_testvoc2.txt |
        lt-proc -d ../en-hi.autogen.bin > $TMPDIR/tmp_testvoc3.txt
paste -d _ $TMPDIR/tmp_testvoc1.txt $TMPDIR/tmp_testvoc2.txt $TMPDIR/tmp_testvoc3.txt | sed 's/\^.<sent>\$//g' | sed 's/_/   --------->  /g'

rm ../apertium-en-hi.en.dixtmp1
