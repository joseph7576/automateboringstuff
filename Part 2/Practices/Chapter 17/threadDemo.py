import threading, time

print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake Up!')
    
threadObj = threading.Thread(target=takeANap) # pass reference - not calling the function bruh
threadObj.start() # create new thread and start the executing the target function in the new thread

print('End of Program.')