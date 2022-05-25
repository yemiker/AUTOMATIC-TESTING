from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#driverChrom
email = 'yemikeradonia@walla.com'
password = 'ahruah123'

driver = webdriver.Chrome("chrome_driver/chromedriver.exe")
driver.get("https://he-il.facebook.com")

driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "pass").send_keys(password)
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

#------------------------------------------------------------------------------------------------------#
#driveFirefox

driver = webdriver.Firefox(executable_path=r"geckodriver/geckodriver.exe")

driver.get("http://www.youtube.com")

#------------------------------------------------------------------------------------------------------#
##driveMicrosoft
driver = webdriver.Edge("Microsoft_driver/msedgedriver.exe")

driver.get("https://www.facebook.com/login/?__tn__=*F")