#!/bin/bash
# create an header and a post message wiit json typw of file```r
curl -s -H "Content-Type: application/json" --data-binary @"$2" "$1"
