#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

body_size=$(curl -s "$1" | wc -c)

echo "$body_size"
