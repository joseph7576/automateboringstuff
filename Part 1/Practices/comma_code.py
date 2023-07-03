spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(some_list):
    return_string = ''
    for item in some_list:
        if not item == some_list[-1]:
            return_string += item + ', '
        else:
            return_string += 'and ' + item 
    print(return_string)

comma_code(spam) # test with given list
comma_code([]) # test with empty list