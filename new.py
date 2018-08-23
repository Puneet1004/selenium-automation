from selenium import webdriver
import time
import pickle
driver = webdriver.Chrome('/Users/Puneet Kumar/AnacondaProjects/chromedriver.exe')
driver.get('https://www.google.com')
cookies = pickle.load(open("facebook.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(2)
i = 1000
for n in range(i):
    driver.get('http://bnb18.ieeedtu.com/index.html')
    login = driver.find_element_by_partial_link_text("Facebook")
    login.click()
    time.sleep(100)
