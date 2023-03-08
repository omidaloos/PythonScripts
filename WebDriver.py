from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random
print(user_agent)

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])


driver = webdriver.Chrome('chromedriver', options=options) #must add chromedriver to $PATH

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("omid test")
elem.send_keys(Keys.RETURN)

