from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

#give location of our chrome driver
service=Service("./chromedriver.exe")

#Here is our baseUrl
url="https://vinothqaacademy.com/alert-and-popup/"
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get(url)
#In here we are starting allert use this code
confirmBox=driver.find_element(by=By.NAME,value="confirmalertbox")
confirmBox.click()
sleep(3)

#Handling allerts pop ups
allerts=driver.switch_to.alert.accept()
sleep(4)
