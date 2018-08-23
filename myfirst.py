from selenium import webdriver
import time
import pickle
driver = webdriver.Chrome('/Users/Puneet Kumar/AnacondaProjects/chromedriver.exe')
driver.get("https://www.google.com")
cookies = pickle.load(open("facebook.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(6)
driver.get("https://www.facebook.com")
