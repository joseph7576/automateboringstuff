from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

playUrl = 'https://play2048.co/'

browser = webdriver.Firefox()
browser.get(playUrl)

time.sleep(5)

fuckingBtn = browser.find_element(By.ID, 'ez-accept-all')
fuckingBtn.click()

time.sleep(1)

htmlElem = browser.find_element(By.TAG_NAME, 'html')

time.sleep(1)

while True:
    for key in [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]:
        htmlElem.send_keys(key)
        time.sleep(0.5)
        
# TODO: it has bugs!