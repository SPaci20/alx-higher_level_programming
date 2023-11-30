#!/bin/bash
# Send a JSON POST request to the URL with the contents of a file and display the body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
