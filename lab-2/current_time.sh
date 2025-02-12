#!/usr/bin/env bash

WORK_START="09:00"
WORK_END="18:00"

current_time=$(date +%s)
work_start_time=$(date -d "$WORK_START" +%s)
work_end_time=$(date -d "$WORK_END" +%s)

echo -n "Current time: $(date +%H:%M)."

if (( current_time < work_start_time )); then
    echo " Work day has not started yet."
elif (( current_time >= work_end_time )); then
    echo " Work day is over."
else
    remaining_seconds=$((work_end_time - current_time))
    echo " Work day ends in $(date -u -d @$remaining_seconds +'%-H hours and %-M minutes')."
fi

