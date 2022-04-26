from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

driver = webdriver.Chrome()
driver.get("https://mytoolstown.com/autoliker/")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
driver.find_element(By.ID, "username").send_keys("arbeen_stha")
driver2 = webdriver.Chrome()
driver2.get("https://instagram.com/")
cookies =[
    {
        "domain": ".instagram.com",
        "expirationDate": 1660824802.545611,
        "hostOnly": False,
        "httpOnly": False,
        "name": "ig_nrcb",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "1"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1643611991.206365,
        "hostOnly": False,
        "httpOnly": True,
        "name": "shbts",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "\"1643007191\\0541577799598\\0541674543191:01f703ebbd4b62c345574c9ae50865efe52e729136120844fcac213e0381bbc5abee0871\""
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1650868380.507861,
        "hostOnly": False,
        "httpOnly": False,
        "name": "ds_user_id",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "1577799598"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1643611991.206353,
        "hostOnly": False,
        "httpOnly": True,
        "name": "shbid",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "\"4723\\0541577799598\\0541674543191:01f75c25d138dad17c9d353e5258f0647125191d9f991f7e185c306eaefd0640c3343a87\""
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1674541980.507811,
        "hostOnly": False,
        "httpOnly": False,
        "name": "csrftoken",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "mfNa42bKCVxGMfJDrbwuOeXoE5GrfhQM"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1692360802.545568,
        "hostOnly": False,
        "httpOnly": True,
        "name": "ig_did",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "5D95DA5D-B4BA-4798-9011-049884CF6AFB"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1643622102.451375,
        "hostOnly": False,
        "httpOnly": True,
        "name": "ig_direct_region_hint",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "\"CLN\\0541577799598\\0541674553302:01f7c95f1db013daca2011e7d459b9efe4c3b878875a11fbec61f6e821cd398deec5a896\""
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1692360805.242302,
        "hostOnly": False,
        "httpOnly": False,
        "name": "mid",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "YRz5ZAALAAF7YqPoQlb9LY1Ta95F"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1674543191.206392,
        "hostOnly": False,
        "httpOnly": True,
        "name": "sessionid",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "1577799598%3ASzFNtRJ4YrjlVE%3A7"
    },
    {
        "domain": ".instagram.com",
        "expirationDate": 1674627181,
        "hostOnly": False,
        "httpOnly": False,
        "name": "fbm_124024574287414",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "None",
        "value": "base_domain=.instagram.com"
    },
    {
        "domain": ".instagram.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "fbsr_124024574287414",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": True,
        "storeId": "None",
        "value": "WE1zPtN-k0SW7NT8RsU0ZQry30kojoDYFvoV-QHJ4rQ.eyJ1c2VyX2lkIjoiMTAwMDAzMTAwOTQ1MTg5IiwiY29kZSI6IkFRRDBnWHlGQ0pSQUhWclgzeDlKNjl4U0VIUWdsVk40MFhkemxYWnVkV3IzdldqeEFRa0dCVUZNMndScV9xbkFTek1BUkNlZFFwak9Yc05qbVhMZEs4NTFWenlxTmFmWU5JejRFOXd5U21vTHl2UmY2d0E2SjZIYzhVdFVqOE94MWJJXzBaazB5eGMtUlVOVkxRTXA5ejFkS0syWFZrZ2RyYlpERW1fOWw0dzNYVFo3VzRzRjEzVHJhQmNLR3hrTU5lbGhHX3JicmVLM3NCdnQ1cEoxNzFJR3VjRDZobDBHeG1GVmRjRmxFcFU2QUpQaE1XOG9tVm9ZS3dzNW5ZRjBqOVJRTW1hVkI0QTNvSTUydGFGMFlLRDhVSzNwUmlxVG5BVTlzNHhYTFBfaFVtT242aTFZM0twNXhFV2l3dkJzNW03aUJfUS1NU1BjOTEyYnp3eXA3UWpQIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUM0WkJsWkM5R01xWkJOR2hySklTRUQySlVzTkxoUjBVclFDZmVNb0tuUG5rcHJFN3R4bUp4R0tOQWtLakdXZGZpYUFTZXp2TTA3ZUFrRElrTE11ZXhPdWlxUTBWTjc0MHFKRGo5dk4xdmhVVTNzNHU3V21uTHd2dFBVN3FGRDl5OTdhWkNuR0hCRjVWM09aQTAwOTg3MG9CQlhDUG9waFNxaFpBMkhHMkdobk9PNkpyQ1hxSVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NDMwOTIzODF9"
    },
    {
        "domain": ".instagram.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "rur",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": True,
        "storeId": "None",
        "value": "\"NAO\\0541577799598\\0541674628380:01f74ec2f891b508dfba4562a837f39b5831c21d12e3d882fa71a9bb8e2308b62bd23d73\""
    }
]

for cookie in cookies:
    driver2.add_cookie(cookie)
x = input("Waiting for manual data to be entered. Enter YES when done.")
print("done")
def doIT():
    time.sleep(5)
    info = driver.find_element(By.ID, "showText").find_elements(By.TAG_NAME, "b")
    driver.implicitly_wait(10)
    action = info[0].text
    instaId = info[1].text
    print(action, instaId)
    time.sleep(2)
    driver.find_element(By.ID, "actionbtn").click()
    if action == "Liking":
        try:
            myString = driver.find_element(By.ID, "actionbtn").get_attribute("onclick")
            a = re.search("(?P<url>https?://[^\s]+)", myString).group("url")
            url = "/".join(a.split("/", 5)[:5])
            print(type(url))
            print(url)
            driver2.get(url)
            driver2.find_element(By.CLASS_NAME, "fr66n").click()
            driver.implicitly_wait(10)
            time.sleep(3)
            driver.find_element(By.ID, "verifybtn").click() 
            time.sleep(4)
            driver2.find_element(By.CLASS_NAME, "fr66n").click()
        
        except:
            driver.refresh()
            doIT()
    elif action == "Following":
        try:
            driver2.get("https://instagram.com/"+instaId)
            driver.implicitly_wait(10)
            driver2.find_element(By.CLASS_NAME, "yZn4P").click()
            driver.implicitly_wait(10)
            time.sleep(3)
            driver.find_element(By.ID, "verifybtn").click() 
            # time.sleep(6)
            # driver2.find_element(By.xpath("//button[@class='_5f5mN    -fzfL     _6VtSN     yZn4P']")).click()
            # time.sleep(2)
            # driver2.find_element(By.xpath("//button[@class='-aOOlW -Cab_']")).click()
            driver.implicitly_wait(10)
            
        except:
            driver.refresh()
            doIT()
    
    doIT()
doIT()

# click verify button at the end 

# driver2.quit()