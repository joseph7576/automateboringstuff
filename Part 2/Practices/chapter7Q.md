# Practice Questions

1. What is the function that creates Regex objects?
    - re.compile()


2. Why are raw strings often used when creating Regex objects?
    - because we need to specify regex patterns that has special characters which should not be interpreter as normal python string

3. What does the search() method return?
    - it will return match object if found and None if there is no matching pattern in given text

4. How do you get the actual strings that match the pattern from a Match object?
    - you would call group(0)

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
    - group 0 cover the whole string, while group 1 will cover the first parentheses and group 2 the second parentheses

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?
    - with escape characters -> \( \.

7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
    - if the regex contains of groups, it will return a list of tuples of strings, if there is no group ( parantheses ) used in regex, it will return a list of strings

8. What does the | character signify in regular expressions?
    - this is an OR operator, it use to match with the left side or the right side of pipe

9. What two things does the ? character signify in regular expressions?
    - the first thing is match character that has zero or one occurrence
    - the second thing is to use un-greedy (lazy) matching -> {}?

10. What is the difference between the + and * characters in regular expressions?
    - plus means 1 or more
    - star means zero or more

11. What is the difference between {3} and {3,5} in regular expressions?
    - {3} means exactly 3 times (repeat/occurrence)
    - {3,5} means min repeat is 3 and max repeat is 5, happend 3 or 4 or 5 times

12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?
    - digits, words, whitespaces

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
    - not digits, not words, not whitespaces

14. What is the difference between .* and .*??
    - .* means any character repeated any times, anything
    - .*? match anything in non-greedy mode. (lazy mode)

15. What is the character class syntax to match all numbers and lowercase letters?
    - [0-9a-z]

16. How do you make a regular expression case-insensitive?
    - pass re.I or re.IGNORECASE to the second argument of compile method

17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
    - . means any character except newlines, however, re.DOTALL will include newlines.

18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?
    - guess -> 'XX drummers, XX pipers, five rings, X hens'
    - tested -> 'X drummers, X pipers, five rings, X hens' -> note that + sign -> it will match digit with any length and match it as ONE result.

19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
    - it will allow us to use comments in our regex

20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

'42'
'1,234'
'6,368,745'
but not the following:

'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)

    - ^\d{1,3}(,\d{3})*$

21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'

but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)

    - [A-Z]\w*\sWatanabe

22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'

but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'

    - (Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\., re.IGNORECASE -> second argument of compile.