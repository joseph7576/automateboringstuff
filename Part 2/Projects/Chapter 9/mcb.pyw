#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.

# pyw -> The .pyw extension means that Python won’t show a Terminal window when it runs this program.
# Multi-CilpBoard

# It’s common practice to put general usage information in comments at the top of the file
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    
    
mcbShelf.close()

#TODO: add delete <keyword> and delete argument. first one deleting only that keyword and the second one delete ALL keywords :D