#! python3
# searchpypi.py  - Opens several search results.

import requests, sys, webbrowser, bs4

print('Searching...') # display text while downloading the search result page

res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status() # make sure no error has happened


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.package-snippet') #TODO: need to update this.

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href') # type: ignore
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
    
    
'''More Ideas

- Open all the product pages after searching a shopping site such as Amazon.
- Open all the links to reviews for a single product.
- Open the result links to photos after performing a search on a photo site such as Flickr or Imgur.
'''