#!/bin/bash


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
fn=$(gshuf -n 1 "$DIR/names")
ln=$(gshuf -n 1 "$DIR/last_names")
pyth="print raw_input().lower().capitalize()"
echo "$(echo "$fn" | python -c "$pyth") $(echo "$ln" | python -c "$pyth")"

