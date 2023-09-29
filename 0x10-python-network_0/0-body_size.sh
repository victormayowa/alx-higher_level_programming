#!/bin/bash
# This script takes a URL as an argument, sends a request, and displays the size of the response body in bytes

# Use curl to send a request and measure the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
