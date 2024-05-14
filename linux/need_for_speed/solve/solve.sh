#!/bin/bash
attack() { for ((i=0;i<200;i++)); do echo hacker > password.txt ;done }

run() { for ((i=0;i<20;i++)); do ./out ;done }

attack & run

# for ((i=0;i<40;i++)); do eval $CMD;done
# CMD="echo hacker > password.txt & ./out /"