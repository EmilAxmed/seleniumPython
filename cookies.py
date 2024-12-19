import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert


#Hanlding allert,in this site it is not working bur if you look "allert.py" same method handle allert
#allerts=driver.switch_to.alert.accept()

#give location of our chrome driver
service=Service("./chromedriver.exe")

#Here is our baseUrl
url = "https://useinsider.com/"

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(5)

#Accept cookies
Acceptcookies=driver.find_element(by=By.XPATH,value="//a[@id='wt-cli-accept-all-btn']")
Acceptcookies.click()
sleep(5)