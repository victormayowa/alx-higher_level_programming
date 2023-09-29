#!/bin/bash
# Use curl to send a request and measure the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
