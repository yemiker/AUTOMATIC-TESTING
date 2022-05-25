from selenium.webdriver.common.by import By
from Web.Pages.AboutUsPage import AboutUs
from Web.Base.base import Base
import pytest

"""About Us Tests"""

@pytest.mark.usefixtures('set_up')
class Tests_AboutUsPage(Base):
    def test_Buttons_success(self):
        driver = self.driver
        about = AboutUs(driver)
        about.MenuBar()
        link_number=0
        #Loop on buttons
        while link_number < 7:
        #Li class name
            element=self.driver.find_elements(By.CLASS_NAME, "menu-link")
            element[link_number].click()
            link_number = link_number + 1
        try:
            assert about.MenuBar_txt_() == about.menuBar_txt_result
        except AssertionError:
            print('Error!')
            driver.get_screenshot_as_png()
            driver.save_screenshot("button text.png")

    @pytest.mark.regression
    def test_Description(self):
        driver = self.driver
        about = AboutUs(driver)
        try:
            assert about.txt_page() == about.txt_result
        except AssertionError:
            print('Error!')
            driver.get_screenshot_as_png()
            driver.save_screenshot("Description text.png")

    def test_title(self):
        driver = self.driver
        title = AboutUs(driver)
        try:
            assert title.txt_titlee() == "About Us"
        except AssertionError:
            print('Error!')
            driver.get_screenshot_as_png()
            driver.save_screenshot('title text.png')

    def test_links(self):
        driver = self.driver
        links = AboutUs(driver)
        try:
            assert links.txt_linkss() == links.txt_links_result
        except AssertionError:
            print('Error!')
            driver.get_screenshot_as_png()
            driver.save_screenshot('links text.png')

    def test_team(self):
        driver = self.driver
        team = AboutUs(driver)
        try:
            assert team.txt_team_() == team.txt_team_result
        except AssertionError:
            print('Error! ')
            driver.get_screenshot_as_png()
            driver.save_screenshot('team text.png')

    def test_lower_page(self):
        driver = self.driver
        text = AboutUs(driver)
        try:
            assert text.txt_lower_page_() == text.txt_lower_page
        except AssertionError:
            print('Error! ')
            driver.get_screenshot_as_png()
            driver.save_screenshot('team text.png')


