import time

print(time.time()) # This number is called an epoch timestamp.

'''
The Unix epoch is a time reference commonly used in programming: 12 AM on January 1, 1970, Coordinated Universal Time (UTC). 
Epoch timestamps can be used to profile code, that is, measure how long a piece of code takes to run.
'''


'''
Another way to profile your code is to use the cProfile.run() function, which provides a much more
informative level of detail than the simple time.time() technique.
The cProfile.run() function is explained at https://docs.python.org/3/library/profile.html.
'''



print(time.ctime())

'''
The time.sleep() function will block—that is, it will not return and release your program to 
execute other code—until after the number of seconds you passed to time.sleep() has elapsed.
'''

import datetime # -> do time operation in more convenient way :D

datetime.timedelta # -> represents a duration of thime rather than a moment in time, arithmetic baby


print(datetime.datetime.strftime(datetime.datetime.now(), '%d/%m/%Y, %H:%M:%S')) # -> (The f in the name of the strftime() function stands for format.)
#? strptime(time_string, format) -> reverse of strftime, (The p in the name of the strptime() function stands for parse.)



import threading # -> hell yeah bruh

# Normally a program terminates when the last line of code in the file has run (or the sys.exit() function is called). 
# A Python program will not terminate until all its threads have terminated.

#? threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
#? this will be start like print('Cats', 'Dogs', 'Frogs', sep=' & ')

#  to avoid concurrency issues, never let multiple threads read or write the same variables. 
# When you create a new Thread object, make sure its target function uses only local variables in that function.

# Calling a Thread object’s join() method will block until that thread has finished.

''' import subprocess

Your Python program can start other programs on your computer with the Popen() function in the built-in subprocess module. 
(The P in the name of the Popen() function stands for process.) 

The return value is a Popen object, which has two useful methods: poll() and wait().
You can think of the poll() method as asking your driver “Are we there yet?” over and over until you arrive. 
The poll() method will return None if the process is still running at the time poll() is called. If the program has terminated, 
it will return the process’s integer exit code. An exit code is used to indicate whether the process
terminated without errors (an exit code of 0) or whether an error caused the process to terminate (a nonzero exit code—generally 1,
but it may vary depending on the program).

The wait() method is like waiting until the driver has arrived at your destination. 
The wait() method will block until the launched process has terminated.
This is helpful if you want your program to pause until the user finishes with the other program.
The return value of wait() is the process’s integer exit code.
'''

'''
Task Scheduler on Windows, launchd on macOS, or the cron scheduler on Linux. 

However, use the time.sleep() function if you just need your program to pause briefly.
Or instead of using the operating system’s scheduler, your code can loop until a certain date and time, calling time.sleep(1) each time through the loop.
'''





