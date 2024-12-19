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

url = "https://useinsider.com/careers/quality-assurance/"
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(5)

# Accept the cookies
Acceptcookies = driver.find_element(by=By.XPATH, value="//a[@id='wt-cli-accept-all-btn']")
Acceptcookies.click()


#See All QA jobs module
allJobButton=driver.find_element(by=By.CSS_SELECTOR,value="#page-head > div > div > div.col-12.col-lg-7.order-2.order-lg-1 > div > div > a")
allJobButton.click()


#Filter jobs by Location
locationFilter=driver.find_element(by=By.ID,value="filter-by-location")
select=Select(locationFilter)
select.select_by_visible_text('Istanbul, Turkey')
sleep(10)

#Filter jobs by Departament
#I sent you a video,as you see manually i want to goto the url department changing automaticly.So my automation case did fail.Because this modul have bug
