#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4
from pathlib import Path

cwd = Path.cwd()
xkcdDir = cwd / 'Data' / 'Chapter 12' / 'xkcd'

url = 'https://xkcd.com'           # starting url
os.makedirs(xkcdDir, exist_ok=True)     # store comics in ./xkcd

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src') # type: ignore
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()


    # Save the image to ./xkcd.
        imageFile = open(os.path.join(xkcdDir, os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href') # type: ignore


print('Done.')

''' more more more

- Back up an entire site by following all of its links.
- Copy all the messages off a web forum.
- Duplicate the catalog of items for sale on an online store.
'''