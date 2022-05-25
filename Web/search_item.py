from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def init():
    driver = webdriver.Chrome("../Driver/chrome_driver/chromedriver.exe")
    driver.get("https://atid.store/")
    return driver



def test_search_products_in_store():
    driver = init()
    search = 'test'

    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
    driver.find_element(By.ID,"wc-block-search__input-1").send_keys(search)
    driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
    value = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/p[1]").get_attribute("innerText")
    assert value == "No products were found matching your selection"
    sleep(5)

def test_search_products_in_men():
    driver = init()
    search2 = 'ATID Blue Shoes'
    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]").click()
    driver.find_element(By.ID,"wc-block-search__input-1").send_keys(search2)
    driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
    value = driver.find_element(By.XPATH,"//main[1]/div[1]/p[1]").get_attribute("innerText")
    assert value == "No products were found matching your selection"
    sleep(5)


def test_search_products_in_women():
    driver = init()
    search3 = 'Anchor Bracelet'
    driver.find_element(By.XPATH, "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]").click()
    driver.find_element(By.ID,"wc-block-search__input-1").send_keys(search3)
    driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
    value = driver.find_element(By.XPATH,"//p[contains(text(),'No products were found matching your selection.')]").get_attribute("innerText")
    assert value == "No products were found matching your selection"
    sleep(5)

test_search_products_in_store()
test_search_products_in_women()
test_search_products_in_men()


def test_check_if_the_Anchor_Bracelet_valid():
    driver = init()
    search_product_name = "Anchor Bracelet"
    search_bar = 'Anchor Bracelet'

    driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()
    driver.find_element(By.ID,"wc-block-search__input-1").send_keys(search_bar)
    driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
    value1 = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/h1[1]").get_attribute("innerText")
    assert value1 == search_product_name
    sleep(5)

    value3 = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[2]/p[1]").get_attribute("innerText")
    assert value3 == 'Nam nec tellus a odio tincidunt auctor a ornare odio. Sed non mauris vitae erat consequat auctor eu in elit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris in erat justo. Nullam ac urna eu felis dapibus condimentum sit amet a augue. Sed non neque elit sed.'









