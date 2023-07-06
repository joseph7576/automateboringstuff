'''
Regex Search
Write a program that opens all .txt files in a folder 
and searches for any line that matches a user-supplied regular expression.
The results should be printed to the screen.
'''

import re # did not even used this :D
from pathlib import Path
import pyinputplus as pyip 

p = Path(Path.cwd() / 'Data' / 'Chapter 9')

user_regex = pyip.inputRegexStr('Enter your regex in python style: ') # regex python style :D

for file in list(p.glob('*.txt')):
    file_open = open(file)
    lines = file_open.readlines()
    for i in range(len(lines)):
        regex_results = user_regex.findall(lines[i])
        if regex_results:
            print(f'- Your pattern find {regex_results} in following lines in file {file.name}')
            print(f'line number {i+1}: {lines[i]}')
            print('-'*20)
    