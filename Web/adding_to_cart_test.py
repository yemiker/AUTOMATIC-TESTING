from main_ATID_college_store_web import *
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def init():
    driver = webdriver.Chrome("../Driver/chrome_driver/chromedriver.exe")
    driver.maximize_window()
    return driver

def test_adding_product_home_page():
    driver = init()
    driver.get("https://atid.store")

    add_cart_button = "//button[contains(text(),'Add to cart')]"
    add_cart =  "// span[contains(text(), '2')]"
    product_li = "//main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]"
    product_2_li = "//main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[3]"

    driver.find_element(By.XPATH,product_li).click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,add_cart_button)))
    driver.find_element(By.XPATH,add_cart_button).click()
    driver.back()
    driver.back()
    driver.find_element(By.XPATH,product_2_li).click()
    driver.find_element(By.XPATH,add_cart_button).click()
    driver.find_element(By.XPATH,add_cart).click()

    Shoes = driver.find_element(By.XPATH,"//a[contains(text(),'ATID Yellow Shoes')]").get_attribute("innerText")
    assert Shoes == "ATID Yellow Shoes"

    Shoes_price = driver.find_element(By.XPATH,"//tbody/tr[1]/td[6]").get_attribute("innerText").split(".")
    assert Shoes_price[0] == "120"

    Jeans = driver.find_element(By.XPATH, "//a[contains(text(),'Dark Brown Jeans')]").get_attribute("innerText")
    assert Jeans == "Dark Brown Jeans"

    Jeans_price = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[6]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert Jeans_price[0] == "150"


    sumTotal = int(Shoes_price[0]) + int(Jeans_price[0])

    total = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]").get_attribute("innerText").split(".")
    assert int(total[0]) == sumTotal







def test_adding_product_store_page():
    driver = init()
    driver.get("https://atid.store/store/")
    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[2]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()
    driver.back()
    driver.back()
    sleep(1)
    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[3]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()

    driver.find_element(By.XPATH,"//span[contains(text(),'2')]").click()
    shoes = driver.find_element(By.XPATH, "//a[contains(text(),'ATID Black Shoes')]").get_attribute("innerText")
    assert shoes == "ATID Black Shoes"

    shoes_price = driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[4]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert shoes_price[0] == "61"

    shoes_blue = driver.find_element(By.XPATH, "//a[contains(text(),'ATID Blue Shoes')]").get_attribute("innerText")
    assert shoes_blue == "ATID Blue Shoes"

    shoes_blue_price = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[4]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert shoes_blue_price[0] == "80"

    sumTotal = int(shoes_price[0]) + int(shoes_blue_price[0])
    total = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]").get_attribute("innerText").split(".")
    assert int(total[0] )== sumTotal




def test_adding_product_men_page():
    driver = init()
    driver.get("https://atid.store/product-category/men/")
    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[3]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()
    driver.back()
    driver.back()
    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[8]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()

    driver.find_element(By.XPATH,"//span[contains(text(),'2')]").click()
    tshirt= driver.find_element(By.XPATH, "//a[contains(text(),'ATID Green Tshirt')]").get_attribute("innerText")
    assert tshirt == "ATID Green Tshirt"

    tshirt_price = driver.find_element(By.XPATH,"//tbody/tr[1]/td[4]").get_attribute("innerText").split(".")
    assert tshirt_price[0] == "190"

    tshirt_blue = driver.find_element(By.XPATH, "//a[contains(text(),'Blue Tshirt')]").get_attribute("innerText")
    assert tshirt_blue == "Blue Tshirt"

    tshirt_blue_price= driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[4]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert tshirt_blue_price[0] == "150"


    sumTotal=int(tshirt_price[0])+int(tshirt_blue_price[0])

    total = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/strong[1]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert int(total[0]) == sumTotal



def test_adding_product_women_page():
    driver = init()
    driver.get("https://atid.store/product-category/women/")
    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[3]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()
    driver.back()
    driver.back()
    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[4]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()

    driver.find_element(By.XPATH,"//span[contains(text(),'2')]").click()
    jeans = driver.find_element(By.XPATH, "//a[contains(text(),'Basic Gray Jeans')]").get_attribute("innerText")
    assert jeans == "Basic Gray Jeans"

    jeans_price = driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[4]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert jeans_price[0] == "100"

    handbag = driver.find_element(By.XPATH, "//a[contains(text(),'Black Over-the-shoulder Handbag')]").get_attribute("innerText")
    assert handbag == "Black Over-the-shoulder Handbag"

    handbag_price = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[4]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert handbag_price[0] == "85"


    sum_total = int(jeans_price[0]) + int(handbag_price[0])

    total = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/strong[1]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert int(total[0]) == sum_total


def test_adding_product_accessories_page():
    driver = init()
    driver.get("https://atid.store/product-category/accessories/")
    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[3]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()
    driver.back()
    driver.back()
    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[4]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()

    driver.find_element(By.XPATH,"//span[contains(text(),'2')]").click()
    bracelet = driver.find_element(By.XPATH, "//a[contains(text(),'Boho Bangle Bracelet')]").get_attribute("innerText")
    assert bracelet == "Boho Bangle Bracelet"

    bracelet_price = driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[4]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert bracelet_price[0] == "45"

    chain = driver.find_element(By.XPATH, "//a[contains(text(),'Bright Gold Purse With Chain')]").get_attribute("innerText")
    assert chain == "Bright Gold Purse With Chain"

    chain_price = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[4]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert chain_price[0] == "80"


    sum_total = int(bracelet[0]) + int(chain[0])
    value5 = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/strong[1]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert int(value5[0]) == sum_total


def test_adding_product_about_page():
    driver = init()
    driver.get("https://atid.store/product-category/accessories/")
    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[3]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()
    driver.back()
    driver.back()

    driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]/li[4]").click()
    driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]").click()

    driver.find_element(By.XPATH,"//span[contains(text(),'2')]").click()
    bracelet = driver.find_element(By.XPATH, "//a[contains(text(),'Boho Bangle Bracelet')]").get_attribute("innerText")
    assert bracelet == "Boho Bangle Bracelet"

    bracelet_price = driver.find_element(By.XPATH,"//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[1]/td[4]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert bracelet_price[0] == "45"

    chain = driver.find_element(By.XPATH, "//a[contains(text(),'Bright Gold Purse With Chain')]").get_attribute("innerText")
    assert chain == "Bright Gold Purse With Chain"

    chain_price = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[4]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert chain_price[0] == "80"


    sum_total = int(bracelet_price[0]) + int(chain_price[0])

    total = driver.find_element(By.XPATH, "//main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/strong[1]/span[1]/bdi[1]").get_attribute("innerText").split(".")
    assert int(total[0]) == sum_total















