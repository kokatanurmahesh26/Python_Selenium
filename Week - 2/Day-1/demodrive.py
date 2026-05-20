from selenium import webdriver
driver = webdriver.Chrome() 
# driver = webdriver.Edge() #Edge browser
driver.get("https://google.com") #
driver.maximize_window()
print(driver.title)
driver.close() #close the current session
driver.quit() #close the all sessions


