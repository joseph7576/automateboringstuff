#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


'''more ideas :D

- Open all links on a page in separate browser tabs.
- Open the browser to the URL for your local weather.
- Open several social network sites that you regularly check.
'''


''' on Respone Object
The iter_content() method returns “chunks” of the content on each iteration through the loop. 
Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain.
'''

