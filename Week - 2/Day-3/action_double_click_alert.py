from selenium import webdriver
from selenium.webdriver import ActionChains #to perform virtual mouse actions
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try :
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")
    driver.maximize_window()
    time.sleep(3)
    double_click = driver.find_element(By.XPATH, "//button[contains(text(), 'Double-Click Me')]")
    mouse_actions = ActionChains(driver) #this line connect virtual mouse to our open browser window and saves into mouse_action variable
    mouse_actions.double_click(double_click) #moving virtual mouse to community menu
    time.sleep(3)
    mouse_actions.perform() #
    time.sleep(3)
    print("double click action successful")

    #Alert
    driver.switch_to.alert.accept()
    time.sleep(3)
    
except Exception :
    print("error")

finally :
    driver.quit()

# driver.get("https://guru99.com/")
# time.sleep(5)

# source = driver.find_element(By.ID,"fourth")
# target = driver.find_element(By.ID, "amt7")
# mouse_actions = ActionChains(driver)
# mouse_actions.drag_and_drop(source, target).perform()

# time.sleep(5)
