# Web scraping is the term for using a program to download and process content from the web.

'''GOOD MODULES

- webbrowser Comes with Python and opens a browser to a specific page.
- requests Downloads files and web pages from the internet.
- bs4 Parses HTML, the format that web pages are written in.
- selenium Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser.
'''

import requests

# A simpler way to check for success is to call the raise_for_status() method on the Response object. 
# This will raise an exception if there was an error downloading the file and will do nothing if the download succeeded.
# The raise_for_status() method is a good way to ensure that a program halts if a bad download occurs.
# This is a good thing: You want your program to stop as soon as some unexpected error happens.
# Always call raise_for_status() after calling requests.get(). You want to be sure that the download has actually worked before your program continues.


# you need to write binary data instead of text data in order to maintain the Unicode encoding of the text. -> 'wb': write binary


'''
To review, here’s the complete process for downloading and saving a file:

- Call requests.get() to download the file.
- Call open() with 'wb' to create a new file in write binary mode.
- Loop over the Response object’s iter_content() method.
- Call write() on each iteration to write the content to the file.
- Call close() to close the file.
'''

# DON’T USE REGULAR EXPRESSIONS TO PARSE HTML

# Copy ▸ CSS Selector!!! cool thing to know.

# parse (that is, analyze and identify the parts of)

# Selectors are like regular expressions: they specify a pattern to look for

# body > section > div.container.mt-5.pb-5 > div.mt-5 > div > div:nth-child(1) > div -> this selector was what i wanted 1 month ago! DAMN

# The select() method will return a list of Tag objects, which is how Beautiful Soup represents an HTML element. 
# The list will contain one Tag object for every match in the BeautifulSoup object’s HTML. 


# A major “tell” to websites that you’re using a script is the user-agent string, which identifies the web browser and is included in all HTTP requests. 

# https://www.whatsmyua.info/ -> user agent

from selenium import webdriver
from selenium.webdriver.common.by import By # for find_elementsssss stuff - changed.
from selenium.webdriver.common.keys import Keys

# “Gecko” is the name of the browser engine used in Firefox.

# Calling the submit() method on any element will have the same result as clicking the Submit button for the form that element is in. 

''' e.g -> browser = webdriver.Firefox()

- browser.back() Clicks the Back button.
- browser.forward() Clicks the Forward button.
- browser.refresh() Clicks the Refresh/Reload button.
- browser.quit() Clicks the Close Window button.
'''