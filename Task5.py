import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

#Hanlding allert,in this site it is not working bur if you look "allert.py" same method handle allerts
#allerts=driver.switch_to.alert.accept()

#give location of our chrome driver
service=Service("./chromedriver.exe")

url = "https://useinsider.com/careers/open-positions/?department=qualityassurance"
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(5)

#Accept the cookies
acceptCookies=driver.find_element(by=By.XPATH,value="//a[@id='wt-cli-accept-all-btn']")
acceptCookies.click()

#Filter jobs by Location
locationFilter=driver.find_element(by=By.ID,value="filter-by-location")
select=Select(locationFilter)
select.select_by_visible_text('Istanbul, Turkey')
driver.implicitly_wait(10)
#I sent you a video,as you see manually i want to goto the url department changing automaticly.So my automation case did fail.Because this modul have bug
#But generaly i know how to do that task,imagine we can click on view role and we cant take using this method: driver.current_url
#this method: driver.current_url  give to below redirec url

url="https://jobs.lever.co/useinsider/6013cc18-8219-4587-a78c-9325c137b436"

if'lever'in url:
    print("You click on View Role and this action redirects us to Lever")

