#!/bin/bash
# print http methods supported by server
curl -si -X OPTIONS "$1" | grep 'Allow' | cut -d " " -f 2-
