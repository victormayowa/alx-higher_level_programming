#!/usr/bin/python3
import urllib.request
''' Define the URL'''

url = "https://alx-intranet.hbtn.io/status"
# Open the URL using urllib.request.urlopen() in a with statement
with urllib.request.urlopen(url) as response:
    # Read the content of the response
    content = response.read()

    # Print information about the response
    print("Body response:")
    print(f"    - type: {type(content)}")  # Print the type of the content
    print(f"    - content: {content}")  # Print the raw content
    print(f"    - utf8 content: {content.decode('utf-8')}")
