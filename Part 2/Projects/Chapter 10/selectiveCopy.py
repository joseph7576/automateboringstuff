'''
Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). 
Copy these files from whatever location they are in to a new folder.
'''

import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
    
#TODO: Complete this