from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.google.com")

driver.maximize_window()

wait=WebDriverWait(driver,10)
serach_box= wait.until(EC.presence_of_element_located((By.NAME,"q")))

#serach_box=driver.find_element(By.NAME,"q")
serach_box.send_keys("w3 school html tags")
serach_box.send_keys(Keys.RETURN)
time.sleep(100)
driver.quit()