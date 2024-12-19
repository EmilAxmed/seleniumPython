import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


#Hanlding allert,in this site it is not working bur if you look "allert.py" same method handle allerts
#allerts=driver.switch_to.alert.accept()


#give location of our chrome driver
service=Service("./chromedriver.exe")

#this is our baseUrl
url="https://useinsider.com/careers/quality-assurance/"


driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)
sleep(1)

# Accept the cookies
Acceptcookies = driver.find_element(by=By.XPATH, value="//a[@id='wt-cli-accept-all-btn']")
Acceptcookies.click()
sleep(4)

#See ALL QA Jobs
allQA=driver.find_element(by=By.XPATH,value="//a[@class='btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50']")
allQA.click()