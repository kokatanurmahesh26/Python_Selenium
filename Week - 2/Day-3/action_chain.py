from selenium import webdriver
from selenium.webdriver import ActionChains #to perform virtual mouse actions
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try :
    driver.get("https://python.org/")
    time.sleep(3)
    community_menu = driver.find_element(By.LINK_TEXT, "Community")
    mouse_actions = ActionChains(driver) #this line connect virtual mouse to our open browser window and saves into mouse_action variable
    mouse_actions.move_to_element(community_menu) #moving virtual mouse to community menu
    time.sleep(3)
    mouse_actions.perform() #
    time.sleep(3)
    print("Hover action successful")
except Exception :
    print("error")

finally :
    driver.quit()
