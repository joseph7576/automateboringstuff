import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

if len(sys.argv) == 1:
    print("Please provide email and text")
    exit()
    

browser = webdriver.Firefox()

signin_url = 'https://accounts.google.com/signin'

myemail = 'abstestingemail@gmail.com'
myemail_pass = 'AutomateBoringStuff1234'

to_email = sys.argv[1]
text = ' '.join(sys.argv[2:])

logging.info(f'Email Recipient: {to_email}')
logging.info(f'Email Text: {text}')

browser.get(signin_url)
email_elem = browser.find_element(By.NAME, 'identifier')
email_elem.send_keys(myemail)
next_key = browser.find_element(By.ID, 'identifierNext')
next_key.click()

# pass_elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'Passwd')))
time.sleep(5)

pass_elem = browser.find_element(By.NAME, 'Passwd')
pass_elem.send_keys(myemail_pass)
time.sleep(1)
# nex_key = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
next_key = browser.find_element(By.ID, 'passwordNext')
next_key.click()

gmail_url = 'https://mail.google.com/mail/u/0/'
browser.get(gmail_url)

#TODO: complete this.
