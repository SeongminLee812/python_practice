from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests

id = input('아이디를 입력하세요 : ')
pw = input('비밀번호를 입력하세요 : ')


url = "https://kyobobook.co.kr/index.laf?gclid=CjwKCAjw-8qVBhANEiwAfjXLrkgUwqbrUHcTiuzBfaSPXTZ11U3vp0Oje4cdINlFwlhBA6keOVHF-xoCLwwQAvD_BwE"

service = Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(url)
sleep(5)

login = driver.find_element(By.ID, 'gnbLoginInfoList').find_element(By.TAG_NAME, 'a')
login.click()
sleep(5)


idspan = driver.find_element(By.NAME, 'memid')
pwspan = driver.find_element(By.NAME, 'pw')

idspan.send_keys(id)
pwspan.send_keys(pw)
sleep(3)

idspan.send_keys(Keys.RETURN)

sleep(5)

check_url = 'http://www.kyobobook.co.kr/event/dailyCheckSpci.laf?orderClick=c1j'
driver.get(check_url)

sleep(5)

driver.quit()
