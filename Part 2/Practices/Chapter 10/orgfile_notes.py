'''
The shutil Module
The shutil (or shell utilities) module has functions to let you copy, 
move, rename, and delete files in your Python programs. To use the shutil functions,
you will first need to use import shutil.

>>> p = Path.home()
>>> shutil.copy(p / 'spam.txt', p / 'some_folder') -> copy file

>>> shutil.copytree(p / 'spam', p / 'spam_backup') -> copy folder

>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt') -> move file, folders and can rename 

'''

'''
OS Module

- Calling os.unlink(path) will delete the file at path.
- Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
- Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

It's good to first print the programs to see which files are going to delete.

'''


''' -> send2trash module :DDDD
>>> import send2trash
>>> baconFile = open('bacon.txt', 'a')   # creates the file
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')
'''

''' OS.WALK()
import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
    

folderName - A string of the current folder’s name - 0
subfolders - A list of strings of the folders in the current folder - 1
filenames - A list of strings of the files in the current folder - 2

'''

''' ZIP FILES

>>> import zipfile, os

>>> from pathlib import Path
>>> p = Path.home()
>>> exampleZip = zipfile.ZipFile(p / 'example.zip') -> ZipFile Objects represents an entire archive
>>> exampleZip.namelist()
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
>>> spamInfo = exampleZip.getinfo('spam.txt') -> ZipInfo objects holds useful info about a SINGLE FILE in the archive
>>> spamInfo.file_size
13908
>>> spamInfo.compress_size
3828
>>> f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
'Compressed file is 3.63x smaller!'
>>> exampleZip.close()

>>> exampleZip.extractall() -> extract all files and folders -> it will also create directory if not exist
The extract() method for ZipFile objects will extract a single file from the ZIP file.
The string you pass to extract() must match one of the strings in the list returned by namelist(). 


>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) -> copmress file
>>> newZip.close()
This code will create a new ZIP file named new.zip that has the compressed contents of spam.txt.

Keep in mind that, just as with writing to files, write mode will erase all existing contents of a ZIP file.
If you want to simply add files to an existing ZIP file, pass 'a' as the second argument to zipfile.ZipFile() to open the ZIP file in append mode.

'''


