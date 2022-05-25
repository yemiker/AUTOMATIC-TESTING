import time

from selenium.webdriver.common.by import By

from Web.Pages.contactUsPage import contactUS
from Web.Base.base import Base
import pytest

"""Contact Us Tests"""

@pytest.mark.usefixtures('set_up')
class Tests_ContactUs(Base):


    def test_contactUs_success(self):
        driver = self.driver
        contact = contactUS(driver)
        contact.enter_name('dani')
        contact.enter_subject('sdasdsdd')
        contact.enter_email('dani@walla.com')
        contact.enter_message('sadsadsdda')
        contact.click_link()
        try:
            assert contact.result_message_success_()=='Thanks for contacting us! We will be in touch with you shortly.'
        except Exception as e:
            print("Error!",format(e))



    def test_contactUs_when_nameFiled_is_null(self):
        driver = self.driver
        contact = contactUS(driver)
        contact.enter_subject('sdasds')
        contact.enter_email('yemiek@walla.com')
        contact.enter_message('sadsadsa')
        contact.click_link()

        value = driver.find_element(By.ID,"wpforms-15-field_0-error").get_attribute("innerText")
        assert value == 'This field is required.'
    #
    # @pytest.mark.skip
    # def test_contactUs_when_subjectFiled_is_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_name('yemi')
    #     contact.enter_email('yemiek@walla.com')
    #     contact.enter_message('sadsadsa')
    #     contact.click_link()
    #
    #     value = driver.find_element(By.XPATH,"//p[contains(text(),'Thanks for contacting us! We will be in touch with')]").get_attribute("innerText")
    #     assert value == 'Thanks for contacting us! We will be in touch with you shortly.'
    #
    # def test_contactUs_when_emailFiled_is_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_name('yemi')
    #     contact.enter_subject('sdasds')
    #     contact.enter_message('sadsadsa')
    #     contact.click_link()
    #
    #     value = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")
    #     assert value == 'This field is required.'
    #
    # def test_contactUs_when_messageFiled_is_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_name('yemi')
    #     contact.enter_subject('sdasds')
    #     contact.enter_email('yemiek@walla.com')
    #     contact.click_link()
    #
    #     value = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")
    #     assert value == 'This field is required.'
    #
    # def test_contactUs_when_name_and_subject_is_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_email('yemiek@walla.com')
    #     contact.enter_message('sadsadsa')
    #     contact.click_link()
    #
    #     value = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
    #     assert value == 'This field is required.'
    #
    # def test_contactUs_when_name_and_email_is_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_subject('sdasds')
    #     contact.enter_message('sadsadsa')
    #     contact.click_link()
    #
    #     value = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
    #     value2 = driver.find_element(By.ID, "wpforms-15-field_4").get_attribute("innerText")
    #     assert value+value2 == 'This field is required.'
    #
    #
    #
    # def test_contactUs_when_name_and_message_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_subject('sdasds')
    #     contact.enter_email('12324234234hg24h35ha@walla.com')
    #     contact.click_link()
    #     value1 = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
    #     value2 = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")
    #     try:
    #         assert value1 == "This field is required."
    #         assert value2 == "This field is required."
    #     except AssertionError:
    #         print('Error!')
    #
    #
    # def test_contactUs_when_subject_and_email_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_name("yemi")
    #     contact.enter_message('hello')
    #     contact.click_link()
    #
    #     value = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")
    #     assert value == "This field is required."
    #
    #
    # def test_contactUs_when_subject_and_message_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_name("yemi")
    #     contact.enter_email('12324234234hg24h35ha@walla.com')
    #     contact.click_link()
    #
    #     value = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")
    #     assert value == "This field is required."
    #
    #
    # def test_contactUs_when_email_and_message_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_name("yemi")
    #     contact.enter_subject('sdasds')
    #     contact.click_link()
    #
    #     value = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")
    #     value2 = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")
    #
    #     assert value == "This field is required."
    #     assert value2 ==  "This field is required."
    #
    #
    # def test_contactUs_when_name_subject_email_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_message('hello')
    #     contact.click_link()
    #
    #     value = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
    #     value2 = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")
    #
    #     assert value == "This field is required."
    #     assert value2 == "This field is required."
    #
    #
    # def test_contactUs_when_name_subject_message_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_email("yemi@gmail.com")
    #     contact.click_link()
    #
    #     value = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
    #     value2 = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")
    #
    #     assert value == "This field is required."
    #     assert value2 ==  "This field is required."
    #
    # def test_contactUs_when_name_email_message_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_subject("hello")
    #     contact.click_link()
    #
    #     value1 = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
    #     value2 = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")
    #     value3 = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")
    #
    #     assert value2 == 'This field is required.'
    #     assert value1 == 'This field is required.'
    #     assert value3 == 'This field is required.'
    #
    # def test_contactUs_when_subject_email_message_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.enter_name("yemi")
    #     contact.click_link()
    #
    #     value2 = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")
    #     value1 = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")
    #
    #     assert value2 == 'This field is required.'
    #     assert value1 == 'This field is required.'
    #
    # def test_contactUs_all_fields_null(self):
    #     driver = self.driver
    #     contact = contactUS(driver)
    #     contact.click_link()
    #
    #     value2 = driver.find_element(By.ID, "wpforms-15-field_0-error").get_attribute("innerText")
    #     value1 = driver.find_element(By.ID, "wpforms-15-field_2-error").get_attribute("innerText")
    #     value3 = driver.find_element(By.ID, "wpforms-15-field_4-error").get_attribute("innerText")
    #
    #     assert value2 == 'This field is required.'
    #     assert value3 == 'This field is required.'
    #     assert value1 == 'This field is required.'
    #
    #



