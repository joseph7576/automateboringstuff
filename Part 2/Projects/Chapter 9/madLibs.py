import pyinputplus as pyip
import os
from pathlib import Path
import re

cwd = Path.cwd()
text_dir = cwd / 'Data' / 'Chapter 9'

input_file = open(text_dir / 'madLibs.txt', 'r')
input_file_content = input_file.read()


TEXT_LOC = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

current_string = input_file_content
for txt_loc in TEXT_LOC:
    working_regex = re.compile(txt_loc)
    a = 'an' if txt_loc == 'ADJECTIVE' else 'a'
    user_input = pyip.inputStr(f'Enter {a} {txt_loc.title()}:\n')
    current_string = working_regex.sub(user_input, current_string)
    
print(current_string)
output_file = open(text_dir / 'madLibsOut.txt', 'w')
output_file.write(current_string)

# DONE :D