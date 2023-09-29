#!/bin/bash
# This script takes a URL as input, sends a GET request, and displays the body of the response
if ["$(curl -sL -o /dev/null -sw "%{http_code}" "$1")" -eq 200 ]; then curl -sL "$1"; fi
