#!/usr/bin/env bash

# Requires curl, bsondump to be installed

function div {
    printf '=%.0s' {1..80}; echo
    printf "$1\n"
    printf '=%.0s' {1..80}; echo
}

python app.py &
appid=$!

sleep 2

val=$(cat "test.bson" | curl -sv -H 'Content-Type:application/bson' -X POST --data-binary @- http://localhost:5000/ | bsondump)

div "$val"
echo "$val" > "test.json"

val=$(cat "not real bson, will fail" | curl -sv -H 'Content-Type:application/bson' -X POST --data-binary @- http://localhost:5000/)

div "$val"

fz1=`wc -c test.bson | awk '{print $1}'`
fz2=`wc -c test.json | awk '{print $1}'`
pct=`echo "scale=5;$fz1/$fz2*100.0" | bc -l`

div "The BSON output is $pct%% of the size of JSON output"

ps -ef | grep app.py | grep -v grep | grep -v Vim | awk '{print $2}' | xargs kill
