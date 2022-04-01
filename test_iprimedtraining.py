import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
@pytest.fixture()
def setUp():
    global driver,movie,YOI,director,distributer,producer
    movie = input("enter the name of movie")
    YOI = input("enter the year of release")
    director = input("enter the name of director")
    distributer = input("enter the name of the distributer of movie")
    producer = input("enter the name of the producer of movie")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(1)
    driver.close()
def test_Moviedetails(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(1)
    driver.find_element_by_name("mname").send_keys(movie)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(YOI)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(director)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(distributer)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(1)
    driver.find_element_by_name("mlang").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()