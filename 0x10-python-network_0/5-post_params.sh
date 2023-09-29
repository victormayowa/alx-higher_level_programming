#!/bin/bash
# with comments sent using POST method
curl -sL -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
