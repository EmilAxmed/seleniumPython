import time
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Hanlding allert,in this site it is not working bur if you look "allert.py" same method handle allerts
#allerts=driver.switch_to.alert.accept()


#give location of our chrome driver
service=Service("./chromedriver.exe")

#Here is our baseUrl
url = "https://useinsider.com/"

driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(5)

# Accept the cookies
Acceptcookies = driver.find_element(by=By.XPATH, value="//a[@id='wt-cli-accept-all-btn']")
Acceptcookies.click()


#Select “Company” menu in navigation bar
company_btn=driver.find_element(by=By.XPATH,value="//body/nav[@id='navigation']/div[@class='container-fluid']/div[@id='navbarNavDropdown']/ul[@class='navbar-nav']/li[6]/a[1]")
company_btn.click()
driver.implicitly_wait(5)

#Select careers module
carrier_btn=driver.find_element(by=By.XPATH,value="//a[normalize-space()='Careers']")
carrier_btn.click()

#Check it is in Carrier section
if "https://useinsider.com/careers/"==driver.current_url:
     print("You are carrier module")
sleep(5)

#Check location blocks open in Site
location=driver.find_element(by=By.CSS_SELECTOR,value=" #career-our-location > div > div > div > div.col-12.col-md-6 > h3 ")
print(location.text)


#Check Teams blocks open in Site
teams=driver.find_element(by=By.CSS_SELECTOR,value="#career-find-our-calling > div > div > div.col-12.mb-xl-5.py-xl-4.py-2.text-center > h3")
print(teams.text)

#Check Life at Insider blocks open in Site
lifeAtInsider=driver.find_element(by=By.CSS_SELECTOR,value=" body > div.elementor.elementor-22610 > section.elementor-section.elementor-top-section.elementor-element.elementor-element-a8e7b90.elementor-section-full_width.elementor-section-height-default.elementor-section-height-default > div > div > div > div.elementor-element.elementor-element-21cea83.elementor-widget.elementor-widget-heading > div > h2")
print(lifeAtInsider.text)
