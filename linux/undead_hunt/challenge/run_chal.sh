#!/bin/bash


ulimit -c unlimited
sysctl -w kernel.core_pattern=/tmp/cores/core.%p > /dev/null
./out
/bin/bash