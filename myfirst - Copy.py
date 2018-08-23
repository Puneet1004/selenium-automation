from selenium import webdriver
import time
import json
import
driver = webdriver.Chrome('/Users/Puneet Kumar/AnacondaProjects/chromedriver.exe')
driver.get("https://gmail.com")
time.sleep(20)
json.dump('driver.get_cookies()', open('cookies.json', 'wb'))
find = driver.find_element_by_id("input-chatlist-search")
find.send_keys("raj")
select = driver.find_element_by_class_name("chat-body")
select.click()
n = 2
time.sleep(2)
type_message = driver.find_element_by_class_name("pluggable-input pluggable-input-compose")
send = driver.find_element_by_class_name("compose-btn-send")
for i in range(n):
    type_message.send_keys("this is whatsapp automation")
    send.click()
    time.sleep(1)
type_message.send_keys("thats all")
send.click()