import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from task2 import driver

#Hanlding allert,in this site it is not working bur if you look "allert.py" same method handle allerts
#allerts=driver.switch_to.alert.accept()

#give location of our chrome driver
service=Service("./chromedriver.exe")

#set method to do not use double code
def openPage(url):
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(url)
    sleep(2)
    driver.quit()


    #Task1=>check Insider home page is opened or not(without assert)
url="https://useinsider.com/"
#send get request to api
response=requests.get(url)
if(response.status_code==200):
    openPage(url)
    # Accept the cookies
    Acceptcookies = driver.find_element(by=By.XPATH, value="//a[@id='wt-cli-accept-all-btn']")
    Acceptcookies.click()
else:
    print(f"We apologize,but {url} seems to be having some issues,and status code is",response.status_code)


#check Insider home page is opened or not(with assert)
url = "https://useinsider.com/"
try:
    openPage(url)
except AssertionError:
    assert response.status_code != 200
