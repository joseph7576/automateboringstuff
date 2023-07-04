# .  ^  $  *  +  ?  {  }  [  ]  \  |  (  ) -> special meaning in regex
# escape with backslash -> \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)

import re # first thing to import

# You can think of the ? as saying, “Match zero or one of the group preceding this question mark.”
# The * (called the star or asterisk) means “match zero or more”—the group that precedes the star can occur any number of times in the text.
# While * means “match zero or more,” the + (or plus) means “match one or more.”

# Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible.
# The non-greedy (also called lazy) version of the braces, which matches the shortest string possible, has the closing brace followed by a question mark.

"""
Review of Regex Symbols
This chapter covered a lot of notation, so here’s a quick review of what you learned about basic regular expression syntax:

- The ? matches zero or one of the preceding group.
- The * matches zero or more of the preceding group.
- The + matches one or more of the preceding group.
- The {n} matches exactly n of the preceding group.
- The {n,} matches n or more of the preceding group.
- The {,m} matches 0 to m of the preceding group.
- The {n,m} matches at least n and at most m of the preceding group.
- {n,m}? or *? or +? performs a non-greedy match of the preceding group.
- ^spam means the string must begin with spam.
- spam$ means the string must end with spam.
- The . matches any character, except newline characters.
- \\d, \\w, and \\s match a digit, word, or space character, respectively.
- \\D, \\W, and \\S match anything except a digit, word, or space character, respectively.
- [abc] matches any character between the brackets (such as a, b, or c).
- [^abc] matches any character that isn’t between the brackets.
"""

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
# print(mo.group()) -> fully found text
areaCode, mainNumber = mo.groups() # type: ignore

# print(areaCode)
# print(mainNumber)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
sub_txt = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(sub_txt)

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) # Including all three options in the second argument will look like this





# numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')
numRegex = re.compile(r'\d+')
print(numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))