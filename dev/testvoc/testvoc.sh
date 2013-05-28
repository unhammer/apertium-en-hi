if [[ $1 = "hin-eng" ]]; then
echo "==Hindi->English===========================";
bash inconsistency.sh hin-eng > /tmp/hin-eng.testvoc; bash inconsistency-summary.sh /tmp/hin-eng.testvoc hin-eng
echo ""

elif [[ $1 = "eng-hin" ]]; then
echo "==English->Hindi===========================";
bash inconsistency.sh eng-hin > /tmp/eng-hin.testvoc; bash inconsistency-summary.sh /tmp/eng-hin.testvoc eng-hin

fi
