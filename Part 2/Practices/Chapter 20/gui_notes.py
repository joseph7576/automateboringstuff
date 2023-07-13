''' Graphical User Interface Automation - GUI automation

Some companies sell innovative (and pricey) “automation solutions,” usually marketed as robotic process automation (RPA).

On linux u need dis :D
- sudo apt-get install scrot
- sudo apt-get install python3-tk
- sudo apt-get install python3-dev

'''

import pyautogui

''' Pauses and fails Safes HEHEHE :D

Quickly slide the mouse to one of the four corners of the screen.
Every PyAutoGUI function call has a 10th-of-a-second delay after performing its action to give you enough time to move the mouse to a corner. 

log out/shutdown :(
    ctrl + alt + del
    

Your resolution is how many pixels wide and tall your screen is. If your screen’s resolution is set to 1920×1080, 
then the coordinate for the upper-left corner will be (0, 0), and the coordinate for the bottom-right corner will be (1919, 1079).
'''

print(pyautogui.size()) #? obtain the screen resolation

width, height = pyautogui.size()

'''
Named tuples have numeric indexes, like regular tuples, and attribute names, like objects: both wh[0] and wh.width evaluate to the width of the screen.
(All of the duration keyword arguments in PyAutoGUI functions are optional.)

'''

# for i in range(10):
#     pyautogui.moveTo(1920 + 200,100, duration=0.25) # absolute location
#     pyautogui.moveTo(1920 + 100,100, duration=0.25)
#     pyautogui.moveTo(1920 + 200,200, duration=0.25)
#     pyautogui.moveTo(1920 + 100,200, duration=0.25)

# for i in range(2):
#     pyautogui.move(100,0, duration=0.25) # relative mouse location
#     pyautogui.move(0,100, duration=0.25)
#     pyautogui.move(-100,0, duration=0.25)
#     pyautogui.move(0,-100, duration=0.25)

mPosX, mPosY = pyautogui.position() #? mouse pos
print('mouse pos x', mPosX)
print('mouse pos y', mPosY)

pyautogui.click(2279, 80) #? full left mouse click at that pos / it's a wrapper around mouseDown and mouseUp

'''
As a further convenience, the pyautogui.doubleClick() function will perform two clicks with the left mouse button,
while the pyautogui.rightClick() and pyautogui.middleClick() functions will perform a click with the right and middle mouse buttons, respectively.
'''


im = pyautogui.screenshot()

'''
You can obtain the RGB color value of a particular pixel on the screen with the pixel() function.
'''

#! it's looks like this thing is not working on wayland -> should work on X11 but I'm not trying this out with my os :(
#! I think it's better for me to work on this in windows :(((
    

''' can check pixel to see if it should be click or not!
import pyautogui
pyautogui.pixel((50, 200))
(130, 135, 144)

pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
True

pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))
False
'''

''' it can also locate image on screen! 

>>> import pyautogui
>>> b = pyautogui.locateOnScreen('submit.png')
>>> b
Box(left=643, top=745, width=70, height=29)

>>> b[0]
643

>>> b.left
643
'''


'''
>>> list(pyautogui.locateAllOnScreen('submit.png'))
[(643, 745, 70, 29), (1007, 801, 70, 29)]
'''

''' you can click that tuple! or image!
>>> pyautogui.click((643, 745, 70, 29))
>>> pyautogui.click('submit.png')
'''

'''
try:
    location = pyautogui.locateOnScreen('submit.png')
except:
    print('Image could not be found.')
    
#! -> Since you can’t be sure that your program will always find the image, it’s a good idea to use the try and except statements when calling locateOnScreen().
'''

''' Active Window - works only on windows? :(
    
>>> import pyautogui
>>> fw = pyautogui.getActiveWindow()
>>> fw
Win32Window(hWnd=2034368)

>>> str(fw)
'<Win32Window left="500", top="300", width="2070", height="1208", title="Mu 1.0.1 – test1.py">'

>>> fw.title
'Mu 1.0.1 – test1.py'

>>> fw.size
(2070, 1208)

>>> fw.left, fw.top, fw.right, fw.bottom
(500, 300, 2070, 1208)

>>> fw.topleft
(256, 144)

>>> fw.area
2500560

>>> pyautogui.click(fw.left + 10, fw.top + 20)
'''

'''
- pyautogui.getAllWindows() Returns a list of Window objects for every visible window on the screen.
- pyautogui.getWindowsAt(x, y) Returns a list of Window objects for every visible window that includes the point (x, y).
- pyautogui.getWindowsWithTitle(title) Returns a list of Window objects for every visible window that includes the string title in its title bar.
- pyautogui.getActiveWindow() Returns the Window object for the window that is currently receiving keyboard focus.
- PyAutoGUI also has a pyautogui.getAllTitles() function, which returns a list of strings of every visible window.
'''

# you can also manipulate windows :D

'''
>>> pyautogui.click(100, 200); pyautogui.write('Hello, world!')
#? Notice how placing two commands on the same line, separated by a semicolon, 
#? keeps the interactive shell from prompting you for input between running the two instructions. 
#? This prevents you from accidentally bringing a new window into focus between the click() and write() calls, which would mess up the example.
'''

# >>> pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

'''
>>> pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')
'''

'''
pyautogui.hotkey('ctrl', 'c')
-> 
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')
'''

'''General Tips
- Use the same screen resolution each time you run the script so that the position of windows doesn’t change.
- The application window that your script clicks should be maximized so that its buttons and menus are in the same place each time you run the script.
- Add generous pauses while waiting for content to load; you don’t want your script to begin clicking before the application is ready.
- Use locateOnScreen() to find buttons and menus to click, rather than relying on XY coordinates. 
    If your script can’t find the thing it needs to click, stop the program rather than let it continue blindly clicking.
- Use getWindowsWithTitle() to ensure that the application window you think your script is clicking on exists, 
    and use the activate() method to put that window in the foreground.
- Use the logging module from Chapter 11 to keep a log file of what your script has done. 
    This way, if you have to stop your script halfway through a process, you can change it to pick up from where it left off.
- Add as many checks as you can to your script. Think about how it could fail if an unexpected pop-up window
    appears or if your computer loses its internet connection.
- You may want to supervise the script when it first begins to ensure that it’s working correctly.

You might also want to put a pause at the start of your script so the user can set up the window the script will click on.
PyAutoGUI has a sleep() function that acts identically to time.sleep() (it just frees you from having to also add import time to your scripts). 
There is also a countdown() function that prints numbers counting down to give the user a visual indication that the script will continue soon. 

>>> import pyautogui
>>> pyautogui.sleep(3) # Pauses the program for 3 seconds.
>>> pyautogui.countdown(10) # Counts down over 10 seconds.
10 9 8 7 6 5 4 3 2 1

>>> print('Starting in ', end=''); pyautogui.countdown(3)
Starting in 3 2 1
'''

''' It Can fucking send pop up messages!

- pyautogui.alert(text) Displays text and has a single OK button.
- pyautogui.confirm(text) Displays text and has OK and Cancel buttons, returning either 'OK' or 'Cancel' depending on the button clicked.
- pyautogui.prompt(text) Displays text and has a text field for the user to type in, which it returns as a string.
- pyautogui.password(text) Is the same as prompt(), but displays asterisks so the user can enter sensitive information such as a password.
'''