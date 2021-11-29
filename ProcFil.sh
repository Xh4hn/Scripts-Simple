#!/bin/bash

# Simple "ps -eo command" Process Filter for possible escalation

process=$(ps -eo command)

while true; do
    new_process=$(ps -eo command)
    diff <(echo "$process") <(echo "$new_process") | grep "[\>\<]" | grep -v -E "procmon|command|kworker"
    process=$new_process
done
