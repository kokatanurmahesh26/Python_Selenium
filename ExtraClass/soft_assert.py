from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_hard_assert(driver):
    driver.get("https://google.com")
    time.sleep(3)
    errors = []

    if driver.title != "Wrong" :
        errors.append("title mismatch")
    if driver.current_url != "https://google.com" :
        errors.append("Invalid url")
    print(errors)
    driver.close()
driver = webdriver.Chrome()
test_hard_assert(driver)

