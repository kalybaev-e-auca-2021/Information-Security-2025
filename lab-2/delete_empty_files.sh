#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory=$1

if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' does not exist."
    exit 2
fi

empty_files=$(find "$directory" -type f -empty)

if [ -z "$empty_files" ]; then
    echo "No empty files found in '$directory'."
    exit 0
fi

echo "Deleting the following empty files:"
echo "$empty_files"

find "$directory" -type f -empty -print -delete
