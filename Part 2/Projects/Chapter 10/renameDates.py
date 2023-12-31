#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.

# To keep the group numbers straight, try reading the regex from the beginning, and count up each time you encounter an opening parenthesis.

# NEW PATTERN
datePattern = re.compile(r"""^(.*?)         # all text before the date
                        ((0|1)?\d)-         # one or two digits for the month
                        ((0|1|2|3)?\d)-     # one or two digits for the day
                        ((19|20)\d\d)       # four digits for the year
                        (.*?)$              # all text after the date
                        """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    
    # Skip files without a date.
    if mo == None:
        continue
    
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)
    
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    #shutil.move(amerFilename, euroFilename)   # uncomment after testing
    
    
'''Other Ideas
- To add a prefix to the start of the filename, such as adding spam_ to rename eggs.txt to spam_eggs.txt
- To change filenames with European-style dates to American-style dates
- To remove the zeros from files such as spam0042.txt
'''