from selenium import webdriver
from selenium.webdriver import ActionChains #to perform virtual mouse actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
try :
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.maximize_window()
    time.sleep(3)
    wait = WebDriverWait(driver, 10)

    disabled_field = wait.until(EC.presence_of_element_located((By.NAME, "my-disabled")))
    assert disabled_field.is_displayed() == True, "Error : disabled field is missing!"
    print("The fields is disabled")
    time.sleep(3)
    
# except AssertionError :
#     print("Assertion failed")    
except Exception as e :
    print(f"Exception : ", {e})

finally :
    driver.quit()
