import requests
from pathlib import Path
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

cwd = Path.cwd()
playFile = open(cwd / 'Data' / 'Chapter 12' / 'RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000): # in bytes -> it's generally a good size.
    playFile.write(chunk)

playFile.close()