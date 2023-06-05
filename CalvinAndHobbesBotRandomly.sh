#!/bin/bash

# call this from cron.hourly

# TODO https://stackoverflow.com/a/246128
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR
source $DIR/venv/bin/activate

RANDOM_NUMBER_FROM_0_TO_35=$(echo $((RANDOM % 36)))
[ "$RANDOM_NUMBER_FROM_0_TO_35" -eq 0 ] && $DIR/venv/bin/python3 $DIR/CalvinAndHobbesBot.py --random
