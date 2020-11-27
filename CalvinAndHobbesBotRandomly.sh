#!/bin/sh

# call this from cron.hourly

RANDOM_NUMBER_FROM_0_TO_11=$(echo $((RANDOM % 12)))
[ "$RANDOM_NUMBER_FROM_0_TO_11" -eq 0 ] && python3 CalvinAndHobbesBot.py --random
