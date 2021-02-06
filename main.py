from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
import time 

driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com/")

# if certain elements do not appear in 10 seconds, just stop
wait = WebDriverWait(driver, 10)

def search(ticker):
    searchEl = driver.find_element_by_id("yfin-usr-qry")
    searchEl.send_keys(ticker)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modules_linkItem__2NK9M")))
    searchEl.send_keys(Keys.ENTER)

search("GME")

time.sleep(3)
driver.quit()