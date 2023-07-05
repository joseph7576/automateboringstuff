# take care that you should write script that works on all operating systems
from pathlib import Path
import sys

print(sys.platform) # -> says the platform this script is running rn

print(type(Path('saawfe', 'awfe'))) # -> PosixPath, if u were on windows it would be WindowsPath _> uses `\\` # replace os.path :D


# The / operator replaces the older os.path.join() function
''' joining path strings with forward slash is EZZZ
>>> from pathlib import Path
>>> Path('spam') / 'bacon' / 'eggs'
WindowsPath('spam/bacon/eggs')
>>> Path('spam') / Path('bacon/eggs')
WindowsPath('spam/bacon/eggs')
>>> Path('spam') / Path('bacon', 'eggs')
WindowsPath('spam/bacon/eggs')
'''

'''
Every program that runs on your computer has a current working directory, or cwd. 
Any filenames or paths that do not begin with the root folder are assumed to be under the current working directory.
'''

# working directory is the standard term

# print Current Working Directory -> Path.cwd()
print(Path.cwd())
# change working directory -> os.chdir()

print(Path.home()) # -> user home directory 
# Your scripts will almost certainly have permissions to read and write the files under your home directory

#  os.makedirs() -> creates directory

# To make a directory from a Path object, call the mkdir() method
# Note that mkdir() can only make one directory at a time; it won’t make several subdirectories at once like os.makedirs().

# To get an absolute path from a relative path, you can put Path.cwd() / in front of the relative Path object.

# os.path.abspath(path) will return a string of the absolute path of the argument. 

# os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.

# Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. 
# If start is not provided, the current working directory is used as the start path.

'''
The parts of a file path include the following:

- The anchor, which is the root folder of the filesystem
- On Windows, the drive, which is the single letter that often denotes a physical hard drive or other storage device
- The parent, which is the folder that contains the file
- The name of the file, made up of the stem (or base name) and the suffix (or extension)

Note that Windows Path objects have a drive attribute, but macOS and Linux Path objects don’t. The drive attribute doesn’t include the first backslash.
'''


'''
Calling os.path.getsize(path) will return the size in bytes of the file in the path argument.
Calling os.listdir(path) will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)

'''


# p.glob() -> Glob patterns are like a simplified form of regular expressions often used in command line commands
''' 
>>> p = Path('C:/Users/Al/Desktop')
>>> p.glob('*')
<generator object Path.glob at 0x000002A6E389DED0>
>>> list(p.glob('*')) # Make a list from the generator.
[WindowsPath('C:/Users/Al/Desktop/1.png'), WindowsPath('C:/Users/Al/
Desktop/22-ap.pdf'), WindowsPath('C:/Users/Al/Desktop/cat.jpg'),
  --snip--
WindowsPath('C:/Users/Al/Desktop/zzz.txt')]


- If you want to perform some operation on every file in a directory, you can use either os.listdir(p) or p.glob('*').
'''

'''
- Calling p.exists() returns True if the path exists or returns False if it doesn’t exist.
- Calling p.is_file() returns True if the path exists and is a file, or returns False otherwise.
- Calling p.is_dir() returns True if the path exists and is a directory, or returns False otherwise.
'''


# Plaintext files contain only basic text characters and do not include font, size, or color information.
# Text files with the .txt extension or Python script files with the .py extension are examples of plaintext files.


'''
The pathlib module’s read_text() method returns a string of the full contents of a text file.
Its write_text() method creates a new text file (or overwrites an existing one) with the string passed to it.
'''

# r -> read mode, w -> write (overwrite) mode, a -> append mode 


# You can save variables in your Python programs to binary shelf files using the shelve module. 

# The shelve module will let you add Save and Open features to your program.

''' #!
the pprint.pprint() function will “pretty print” the contents of a list or dictionary to the screen, 
while the pprint.pformat() function will return this same text as a string instead of printing it.
'''

