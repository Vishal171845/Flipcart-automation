import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
@pytest.fixture()
def setUp():
    global email,password,webdriver
    email = input("enter your facebookemail")
    password = input("enter your facebook password")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(2)
    driver.close()
def test_searchProducts(setUp):
    driver.get("https://www.facebook.com/login/")
    time.sleep(1)
    driver.find_element_by_name("email").send_keys(email)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("login").click()
