from selenium import webdriver
from selenium.webdriver import ActionChains #to perform virtual mouse actions
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try :
    driver.get("https://selenium.dev")
    driver.maximize_window()
    time.sleep(3)

    main_header = driver.find_element(By.TAG_NAME, "h1")
    assert "Selenium automates browsers" in main_header.text
    print("Text validation passed for : ", main_header.text)
    time.sleep(3)
    assert main_header.is_displayed() == True
    print("visibility validation passed for : ", main_header.is_displayed())
    time.sleep(3)
    # assert main_header.get_attribute("class") == "h1"
    # print("Attribute validation passed for : ", main_header.get_attribute)
    # time.sleep(3)

    button_click = driver.find_element(By.TAG_NAME, "button")
    assert button_click.is_enabled() == True
    print("Enable validation passed for : ", button_click.is_enabled())
    time.sleep(3)
    button_click.click()
    
# except AssertionError :
#     print("Assertion failed")    
except Exception as e :
    print(f"Exception : ", {e})

finally :
    driver.quit()
