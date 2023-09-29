#!/bin/bash
# Sends a GET request to the URL with the X-School-User-Id header set to 98.
curl -sL -X GET "$1" -H "X-School-User-Id: 98"
