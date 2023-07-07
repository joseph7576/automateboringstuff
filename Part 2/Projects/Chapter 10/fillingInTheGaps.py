'''
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, 
in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.
'''

from os import listdir
from os.path import isfile, join
import pyinputplus as pyip
from pathlib import Path

givenRegex = pyip.inputRegexStr("Please enter your desired regex to find gap in prefix?!: ")
searchDir = Path.cwd() / 'Data' / 'Chapter 11'

onlyfiles = [f for f in listdir(searchDir) if isfile(join(searchDir, f))] # get only files
onlyfiles.sort() # sort 

foundedFiles = [s for s in onlyfiles if givenRegex.match(s)] # filter list with given regex

for file in foundedFiles:
    pass

# TODO: First Think, The Apply