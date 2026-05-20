from selenium import webdriver
from selenium.webdriver.chrome.service import Service #Service is a class to start the driver service
#communication btwn selenium and browser driver
service = Service(excecutable_path = r"C:\Drivers\chromedrive-wind64\chromedriver.exe")
driver = webdriver.chrome(service)
driver.get("https://google.com")