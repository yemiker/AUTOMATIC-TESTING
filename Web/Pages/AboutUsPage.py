from Web.Locators.AboutLocators import *
from selenium.webdriver.common.by import By
import allure


class AboutUs(LocatorsAboutUs):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://atid.store/about/")
        self.menuBar_UL_ID = LocatorsAboutUs.menuBar_UL_ID
        self.menuBar_xpath = LocatorsAboutUs.menuBar_xpath
        self.txt_page_ = LocatorsAboutUs.txt_page_
        self.txt_title = LocatorsAboutUs.txt_title
        self.txt_links = LocatorsAboutUs.txt_links
        self.txt_team = LocatorsAboutUs.txt_team
        self.txt_team_result = LocatorsAboutUs.txt_team_result

    @allure.step
    def MenuBar(self):
        self.driver.find_element(By.ID, self.menuBar_UL_ID)

    def MenuBar_txt_(self):
        return self.driver.find_element(By.XPATH,self.menuBar_xpath).get_attribute("innerText")

    @allure.step
    def txt_page(self):
        return self.driver.find_element(By.XPATH, self.txt_page_).get_attribute("innerText")

    def txt_titlee(self):
        return self.driver.find_element(By.TAG_NAME,self.txt_title).get_attribute("innerText")

    def txt_linkss(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.txt_links).get_attribute("innerText")

    def txt_team_(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.txt_team).get_attribute("innerText")

    def txt_lower_page_(self):
        return self.driver.find_element(By.CSS_SELECTOR,self.element_lower_page).get_attribute("innerText")


