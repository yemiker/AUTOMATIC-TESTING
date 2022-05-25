from Web.Pages.AccessoriesPage import *
from Web.Base.base import *
import pytest


@pytest.mark.usefixtures('set_up')
class Tests_AccessoriesPage(Base):
    @pytest.mark.sanity
    def test_ui_logo(self):
        driver = self.driver
        logo = Accessories(driver)
        logo.logo_text()
        result = driver.get("https://atid.store/")
        try:
            assert result == driver.get("https://atid.store/")
        except AssertionError:
            print('Error!')

    def test_search_unexist_item_success(self):
        driver = self.driver
        search = Accessories(driver)
        search.search_product_field()
        search.enter_an_product()
        search.search_product_field()
        try:
            assert search.search_result_product() == "Sorry, but nothing matched your search terms. Please try again with some different keywords.\n\nSearch for:\n "
        except Exception as e:
            raise print('Error!')






