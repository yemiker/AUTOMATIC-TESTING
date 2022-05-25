from selenium.webdriver.support.select import Select

from main_ATID_college_store_web import *
def init():
    driver = webdriver.Chrome("../Driver/chrome_driver/chromedriver.exe")
    driver.get("https://atid.store/about/")
    driver.maximize_window()
    return driver

#testing UI
def test_menu_bar_lower_page():
    driver = init()
    value = driver.find_element(By.XPATH,"//body/div[@id='page']/footer[@id='colophon']/div[1]").get_attribute('innerText')
    assert value == "Quick Links\nHome\nAbout\nCart\nContact Us\nFor Her\nWomen Jeans\nTops and Shirts\nWomen Jackets\nHeels and Flats\nWomen Accessories\nFor Him\nMen Jeans\nMen Shirts\nMen Shoes\nMen Accessories\nMen Jackets"


def test_Links():
    driver = init()
    value = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]").get_attribute("innerText")
    assert value == "Follow Us\nFacebook-f\n \nTwitter\n \nInstagram\n \nGoogle-plus-g"




def test_menu_bar():
    driver = init()
    value = driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]").get_attribute('innerText')
    assert value == ' "HOME\nSTORE\nMEN\nWOMEN\nACCESSORIES\nABOUT\nCONTACT US\nSearch\n0.00 ₪ 0" '

def test_title():
    driver = init()
    value = driver.find_element(By.XPATH,"//h1[contains(text(),'About Us')]").get_attribute('innerText')
    assert value == "About Us"

def test_Description():
    driver = init()
    value = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert value == "Who We Are\n\nATID Demo Store was created by ATID College dedicated employees. This is a complete demo site for practicing QA & Test Automation methodologies. Don't think for a second you can actually buy here something cause you can't ! This Demo Store contains software bugs which were put intentionally and your job is to locate them Good luck falks, Yoni Flenner - ATID College"

def test_team():
    driver = init()
    value = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[3] ").get_attribute("innerText")
    assert value == "A Few Words About\nOur Team\n\nWe have the best team ever everybody who is somebody wants to work with us, so we can afford cherry-picking them, one by one...\n\nYoni Flenner\n\nFounder - CEO\n\nAlbert Einstein\n\nCOO\n\nSteve Jobs\n\nMarketing Head\n\nBill Gates\n\nLead Developer\n\nKim Kardashian\n\nIntern Designer\n\nMadonna\n\nHead of Fun"

def test_lower_page():
    driver = init()
    value = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[5]").get_attribute("innerText")
    assert value ==  "Worldwide Shipping\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Quality\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Offers\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nSecure Payments\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo."

def test_accessibility():
    driver = init()
    value = driver.find_element(By.XPATH,"//body[1]/nav[1]/div[1]/a[1]").get_attribute("innerText")
    assert value == "Open toolbar"

#testing functional

def test_click_menu_bar():
    driver = init()

    driver.find_elements(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]")
    n = driver.find_elements(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]")
    p = 1
    while p < 5:
        n = driver.find_elements(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]")
        driver.find_elements(By.XPATH,"//main[1]/div[1]/ul[1]")
        n[p].click()
        p = p + 1
    # menu_bar = driver.find_elements(By.TAG_NAME,"div")
    # a = ['HOME','STORE','MEN','WOMEN','ACCESSORIES','ABOUT','CONTACT US']
    # for elements in menu_bar:
    #     if menu_bar[0] == a[0]:
    #         elements.click()
    #
    # driver.quit()









def test():

    driver = init()
    driver.get("https://atid.store/store/")
    select = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    select.select_by_index(2)
    sleep(3)

def test2():
    driver = init()
    driver.get("https://atid.store/store/")
    select = Select(driver.find_element(By.XPATH,'//main[1]/div[1]/form[1]/select[1]'))
    select.select_by_index(2)
    sleep(3)

    products = driver.find_elements(By.XPATH,'//main[1]/div[1]/ul[1]/li')
    products[4].click()
    sleep(3)







