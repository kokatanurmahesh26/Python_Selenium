from selenium import webdriver
from selenium.webdriver import ActionChains #to perform virtual mouse actions
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try :
    driver.get("https://demo.guru99.com/test/drag_drop.html")
    driver.maximize_window()
    time.sleep(3)

    source = driver.find_element(By.XPATH,"//*[@id = 'fourth']/a")
    target = driver.find_element(By.XPATH, "//*[@id = 'amt7']/li")
    mouse_actions = ActionChains(driver)
    mouse_actions.drag_and_drop(source, target)
    time.sleep(5)
    mouse_actions.perform()
    time.sleep(5)
    print("Drag n drop action successful")
    
except Exception :
    print("error")

finally :
    driver.quit()
