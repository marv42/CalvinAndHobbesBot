#!/bin/bash

# call this from cron.hourly

RANDOM_NUMBER_FROM_0_TO_23=$(echo $((RANDOM % 24)))
[[ "$RANDOM_NUMBER_FROM_0_TO_23" -eq 0 ]] && python3.8 CalvinAndHobbesBot.py --random
