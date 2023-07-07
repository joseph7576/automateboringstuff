'''
>>> raise Exception('This is the error message.')
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.

this is how u raise exception
'''

# Often it’s the code that calls the function, rather than the function itself, that knows how to handle an exception. 
# That means you will commonly see a raise statement inside a function and the try and except statements in the code calling the function.


# Traceback - Call stack -> most recent call last
# Python displays the traceback whenever a raised exception goes unhandled. But you can also obtain it as a string by calling traceback.format_exc().


'''Write traceback to another file in try/except example

>>> import traceback
>>> try:
...          raise Exception('This is the error message.')
except:
...          errorFile = open('errorInfo.txt', 'w')
...          errorFile.write(traceback.format_exc())
...          errorFile.close()
...          print('The traceback info was written to errorInfo.txt.')

'''


# assertions -> sanity check :D
'''How to make an assertion?:
- The assert keyword
- A condition (that is, an expression that evaluates to True or False)
- A comma
- A string to display when the condition is False
'''

# In plain English, an assert statement says, “I assert that the condition holds true, and if not, there is a bug somewhere, so immediately stop the program.”


'''
Unlike exceptions, your code should not handle assert statements with try and except; 
if an assert fails, your program should crash. By “failing fast” like this,
you shorten the time between the original cause of the bug and when you first notice the bug. 
This will reduce the amount of code you will have to check before finding the bug’s cause.

Assertions are for programmer errors, not user errors. Assertions should only fail while the program is under development;
a user should never see an assertion error in a finished program.

You shouldn’t use assert statements in place of raising exceptions, because users can choose to turn off assertions. 
If you run a Python script with python -O myscript.py instead of python myscript.py, Python will skip assert statements. 

By failing fast early in the program’s execution, you can save yourself a lot of future debugging effort.
'''

#! python3 
# enable logging 
import logging
# logging.disable(logging.CRITICAL) #? Disables logging :D
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') #? logging to a file 

#  when Python logs an event, it creates a LogRecord object that holds information about that event.

'''
The nice thing about log messages is that you’re free to fill your program with as many as you like, 
and you can always disable them later by adding a single logging.disable(logging.CRITICAL) call. 

Log messages are intended for the programmer, not the user. 
'''

'''
For messages that the user will want to see, like File not found or Invalid input, please enter a number, 
you should use a print() call. You don’t want to deprive the user of useful information after you’ve disabled log messages.
'''

'''5 log levels
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

>>> logging.debug('Some debugging details.')
#? The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
2019-05-18 19:04:26,901 - DEBUG - Some debugging details.

>>> logging.info('The logging module is working.') 
#? Used to record information on general events in your program or confirm that things are working at their point in the program.
2019-05-18 19:04:35,569 - INFO - The logging module is working. 

>>> logging.warning('An error message is about to be logged.') 
#? Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
2019-05-18 19:04:56,843 - WARNING - An error message is about to be logged.

>>> logging.error('An error has occurred.')
#? Used to record an error that caused the program to fail to do something.
2019-05-18 19:05:07,737 - ERROR - An error has occurred.

>>> logging.critical('The program is unable to recover!')
#? The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.
2019-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!
'''


'''
- continue -> Clicking the Continue button will cause the program to execute normally until it terminates or reaches a breakpoint.

- step in -> If the next line of code is a function call, the debugger will “step into” that function and jump to the first line of code of that function.

- step over -> However, if the next line of code is a function call, the Step Over button will “step over” the code in the function. 
The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns. 

- step out -> Clicking the Step Out button will cause the debugger to execute lines of code at full speed until it returns from the current function.

- breakpoints -> A breakpoint can be set on a specific line of code and forces the debugger to pause whenever the program execution reaches that line.
When you set the breakpoint on the code in the if statement, the debugger breaks only when the execution enters the if clause. 
'''



