TMPDIR=/tmp

DIR=$1

if [[ $DIR = "hin-eng" ]]; then

lt-expand ../../apertium-en-hi.hi.dix | grep -v '<prn><enc>' | grep -v 'REGEX' | grep -v ':<:' | sed 's/:>:/%/g' | sed 's/:/%/g' | cut -f2 -d'%' |  sed 's/^/^/g' | sed 's/$/$ ^.<sent>$/g' | tee $TMPDIR/$DIR.tmp_testvoc1.txt |
        apertium-pretransfer|
	lt-proc -b ../../hi-en.autobil.bin |  tee $TMPDIR/$DIR.tmp_testvoc2.txt |
        apertium-transfer -b ../../apertium-en-hi.hi-en.t1x  ../../hi-en.t1x.bin |
        apertium-interchunk ../../apertium-en-hi.hi-en.t2x  ../../hi-en.t2x.bin |
        apertium-postchunk ../../apertium-en-hi.hi-en.t3x  ../../hi-en.t3x.bin  | tee $TMPDIR/$DIR.tmp_testvoc3.txt |
        lt-proc -d ../../hi-en.autogen.bin > $TMPDIR/$DIR.tmp_testvoc4.txt
paste -d _ $TMPDIR/$DIR.tmp_testvoc1.txt $TMPDIR/$DIR.tmp_testvoc2.txt $TMPDIR/$DIR.tmp_testvoc3.txt $TMPDIR/$DIR.tmp_testvoc4.txt | sed 's/\^.<sent>\$//g' | sed 's/_/   --------->  /g'

elif [[ $DIR = "eng-hin" ]]; then

lt-expand ../../apertium-en-hi.en.dix | grep -v '<prn><enc>' | grep -v 'REGEX' | grep -v ':<:' | sed 's/:>:/%/g' | sed 's/:/%/g' | cut -f2 -d'%' |  sed 's/^/^/g' | sed 's/$/$ ^.<sent>$/g' | tee $TMPDIR/$DIR.tmp_testvoc1.txt |
        apertium-pretransfer|
	lt-proc -b ../../en-hi.autobil.bin | tee $TMPDIR/$DIR.tmp_testvoc2.txt |
        apertium-transfer -b ../../apertium-en-hi.en-hi.t1x  ../../en-hi.t1x.bin |
        apertium-interchunk ../../apertium-en-hi.en-hi.t2x  ../../en-hi.t2x.bin |
        apertium-postchunk ../../apertium-en-hi.en-hi.t3x  ../../en-hi.t3x.bin  | tee $TMPDIR/$DIR.tmp_testvoc3.txt |
        lt-proc -d ../../en-hi.autogen.bin > $TMPDIR/$DIR.tmp_testvoc4.txt
paste -d _ $TMPDIR/$DIR.tmp_testvoc1.txt $TMPDIR/$DIR.tmp_testvoc2.txt $TMPDIR/$DIR.tmp_testvoc3.txt $TMPDIR/$DIR.tmp_testvoc4.txt| sed 's/\^.<sent>\$//g' | sed 's/_/   --------->  /g'


else
	echo "bash inconsistency.sh <direction>";
fi
