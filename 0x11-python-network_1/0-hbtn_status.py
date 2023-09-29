#!/usr/bin/python3
import urllib.request


def status_code():
    ''' Define the URL'''
    url = "https://alx-intranet.hbtn.io/status"
    # Open the URL using urllib.request.urlopen() in a with statement
    with urllib.request.urlopen(url) as response:
        '''Read the content of the response'''
        content = response.read()
        # Print information about the response
        print("Body response:")
        print("    - type: {}".format(type(content)))  # Print type of content
        print("    - content: {}".format(content))  # Print the raw content
        print("    - utf8 content: {}".format(content.decode('utf-8')))


if __name__ == "__main__":
    status_code()
