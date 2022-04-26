from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import *
import time
driver = webdriver.Chrome()
driver.get("https://mytoolstown.com/autoliker/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

driver.find_element(By.ID, "username").send_keys("arbeen_stha")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchbtn")))
driver.find_element(By.ID, "searchbtn").click()
WebDriverWait(driver, 10).until(EC.url_to_be("https://mytoolstown.com/autoliker/dashboard/"))
driver.find_elements(By.TAG_NAME, "a")[7].click()
WebDriverWait(driver, 10).until(EC.url_to_be("https://mytoolstown.com/autoliker/earn-instagram-followers-likes/"))
driver.implicitly_wait(10)
info = driver.find_element(By.ID, "showText").find_elements(By.TAG_NAME, "b")
action = info[0].text
instaId = info[1].text
driver2 = webdriver.Chrome()
if action == "Liking":
    print("Liking")
    driver2.get("https://instagram.com")
elif action == "Following":
    print("Following")
    driver2.get("https://instagram.com")
print(action, instaId)
# click verify button at the end 
# driver.find_element(By.ID, "verifybtn").click()
