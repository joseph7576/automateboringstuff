#! python3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True) # this works on windows -> play the default application for alarm.wav file :(


''' More Ideas :D

- Use time.sleep() to give the user a chance to press CTRL-C to cancel an action, such as deleting files.
    Your program can print a “Press CTRL-C to cancel” message and then handle any KeyboardInterrupt exceptions with try and except statements.
- For a long-term countdown, you can use timedelta objects to measure the number of days, hours, minutes,
    and seconds until some point (a birthday? an anniversary?) in the future.

'''