import allure

from Web.Locators.AccessoriesLocators import *
from selenium.webdriver.common.by import By

class Accessories(LocatorsAccessories):
    def __init__(self,driver):
        self.driver = driver
        self.driver.get("https://atid.store/product-category/accessories/")
        self.logo_className = LocatorsAccessories.logo_className
        self.search = LocatorsAccessories.search
        self.search_filedClasName = LocatorsAccessories.search_filedClasName
        self.search_resultXpath = LocatorsAccessories.search_resultXpath

    @allure.step
    def logo_text(self):
        self.driver.find_element(By.CLASS_NAME,self.logo_className).click()

    @allure.step
    def search_product_field(self):
        self.driver.find_element(By.CSS_SELECTOR,self.search).click()

    @allure.step
    def enter_an_product(self):
        self.driver.find_element(By.CLASS_NAME,self.search_filedClasName).send_keys("NIKE")

    @allure.step
    def search_result_product(self):
        return self.driver.find_element(By.XPATH,self.search_resultXpath).get_attribute("innerText")

    def enter_an_product_exist(self):
        self.driver.find_element(By.CLASS_NAME,self.search_filedClasName).send_keys("ATID Blue Shoes")

    def search_result_product_exist(self):
        return self.driver.find_element(By.CLASS_NAME,self.search_result_txt_).get_attribute("innerText")

