from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests

PATH = r"C:\Users\asus\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

# login
time.sleep(2)
username=driver.find_element_by_css_selector("input[name='username']")
password=driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("your username")
password.send_keys("your password")
login = driver.find_element_by_css_selector("button[type='submit']").click()

#save your login info?
time.sleep(3)
notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
#turn on notif
time.sleep(3)
notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()


#searchbox
time.sleep(3)
searchbox=driver.find_element_by_css_selector("input[placeholder='Search']")
searchbox.clear()
searchbox.send_keys("username u want to search")
time.sleep(2)
searchbox.send_keys(Keys.ENTER)
time.sleep(2)
searchbox.send_keys(Keys.ENTER)

#scroll
scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
match=False
while(match==False):
    last_count = scrolldown
    time.sleep(3)
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    if last_count==scrolldown:
        match=True

time.sleep(6)