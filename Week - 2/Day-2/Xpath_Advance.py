from selenium import webdriver #importing the webdriver
from selenium.webdriver.common.keys import Keys #keys class provide keys into the keyboard
from selenium.webdriver.common.by import By #By class to locate element
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
try :
    driver.get("https://testautomationpractice.blogspot.com/")   
    #Maximize browser
    driver.maximize_window()
    time.sleep(5)

    #contains() - matches the element 
    name_field = driver.find_element(By.XPATH, "//input[contains(@id, 'name')]")
    name_field.send_keys("Mahesh")
    time.sleep(5)
    #start_with() - match beggining of attribute
    email_field = driver.find_element(By.XPATH, "//input[starts-with(@id, 'email')]")
    email_field.send_keys("test@gmail.com")
    time.sleep(5)

    #text() - exact visible text match
    wiki_link = driver.find_element(By.XPATH, "//a[text() = 'GUI Elements']")
    print(wiki_link.text)
    time.sleep(5)

    #normalize-space() - removes unnecccessary spaces
    header = driver.find_element(By.XPATH, "//h1[normalize-space() = 'Automation Testing Practice']")
    print(header.text)
    time.sleep(5)

    # header1 = driver.find_element(By.XPATH, "//h1[@class='title']")
    # print(header1.get_attribute("h1"))
    # time.sleep(5)

    #parent 
    parent_xpath = driver.find_element(By.XPATH, "//input[@id = 'email']/parent::div")
    print(parent_xpath.text)
    time.sleep(5)

    #Ancestor
    ancestor_xpath1 = driver.find_element(By.XPATH, "//p[contains(text(), 'Section 1')]/ancestor::div[@class = 'widget-content']")
    ancestor_xpath = driver.find_element(By.XPATH, "//input[@id = 'email']/ancestor::div[@class='post-body entry-content']")

    print(header.text)
    time.sleep(5)


    #descendant
    descendatnt_ele = driver.find_element(By.XPATH, "//div[@id= 'Wikipedia1']/descendant::input[@class = 'wikipedia-search-button']")

#child - //select[@id = 'colors']/child::option[@value = "blue"]




finally :
    driver.quit()