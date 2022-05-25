from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver

# def init():
#     driver = webdriver.Chrome("../Driver/chrome_driver/chromedriver.exe")
#     driver.get("https://demoblaze.com/index.html")
#     driver.maximize_window()
#     return driver
#
#
# def test():
#     driver = init()
#     driver.find_element(By.CLASS_NAME,"row")

def init():
    driver = webdriver.Chrome("../Driver/chrome_driver/chromedriver.exe")
    driver.get("https://atid.store/about/")
    driver.maximize_window()
    return driver

def test_Description():
    driver = init()
    value = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]").get_attribute("innerText")
    sleep(3)
    assert value == "Who We Are\n\nATID Demo Store was created by ATID College dedicated employees. This is a complete demo site for practicing QA & Test Automation methodologies. Don't think for a second you can actually buy here something cause you can't ! This Demo Store contains software bugs which were put intentionally and your job is to locate them Good luck falks, Yoni Flenner - ATID College"

def test_Links():
    driver = init()
    value = driver.find_element(By.XPATH,"//main[1]//div[1]/div[1]/div[1]/section[4]/div[2]").get_attribute("innerText")
    assert value == "Follow Us\nFacebook-f\n \nTwitter\n \nInstagram\n \nGoogle-plus-g"