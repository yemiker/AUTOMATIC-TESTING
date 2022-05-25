import allure

from Web.Locators.ContactLocators import ContactUsLocators
from  selenium.webdriver.common.by import By

class contactUS:

    def __init__(self,driver):
        self.driver = driver
        self.driver.get("https://atid.store/contact-us/")
        self.name_txtbox_ID = ContactUsLocators.name_txtbox_ID
        self.subject_txtbox_ID = ContactUsLocators.subject_txtbox_ID
        self.email_txtbox_ID = ContactUsLocators.email_txtbox_ID
        self.message_txtbox_ID = ContactUsLocators.message_txtbox_ID
        self.click_link_txtbox_ID = ContactUsLocators.click_link_txtbox_ID
        self.result_txtbox_ID = ContactUsLocators.result_txt_ID
        self.result2_txtbox_ID = ContactUsLocators.result2_txt_ID
        self.result_message_success = ContactUsLocators.result_message_success

    @allure.step
    def enter_name(self,name):
        self.driver.find_element(By.ID,self.name_txtbox_ID).send_keys(name)

    @allure.step
    def enter_subject(self,subject):
        self.driver.find_element(By.ID,self.subject_txtbox_ID).send_keys(subject)

    @allure.step
    def enter_email(self,email):
        self.driver.find_element(By.ID,self.email_txtbox_ID).send_keys(email)

    @allure.step
    def enter_message(self,message):
        self.driver.find_element(By.ID,self.message_txtbox_ID).send_keys(message)

    @allure.step
    def click_link(self):
        self.driver.find_element(By.ID,self.click_link_txtbox_ID).click()

    @allure.step
    def result(self):
          self.driver.find_element(By.ID,self.result_txtbox_ID).get_attribute("innerText")

    @allure.step
    def result2(self):
        self.driver.find_element(By.ID,self.result2_txtbox_ID).get_attribute("innerText")

    def result_message_success_(self):
        return self.driver.find_element(By.XPATH,self.result_message_success).get_attribute("innerText")







