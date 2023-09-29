#!/bin/bash
# print http methods supported by server
curl -sL -X OPTIONS "$1" | grep -Po 'Allow: \K.*'
