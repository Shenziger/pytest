from selenium.webdriver.common.by import By
from locators import MainPage
from selenium.webdriver.common.action_chains import ActionChains
from octest.conftest import url_param


def test_logo(driver):
#    url = request.config.getoption("--url")
#    url = url_param
#    driver.get(url)
    driver[0].find_element_by_id('logo')
    assert driver[0].title == "Your Store"


def test_slideshow(driver):
#    driver.get(url_param)
    driver[0].find_element(By.ID, "slideshow0").click()
    driver[0].find_element(By.CLASS_NAME, "breadcrumb")


def test_menu(driver):
    driver[0].find_elements_by_link_text('Desktops')
    driver[0].find_elements_by_link_text('Tablets')
    driver[0].find_elements_by_link_text('Cameras')


def test_footer(driver):
    driver[0].find_element_by_css_selector('footer')


def test_search_form(driver):
    driver[0].find_elements_by_class_name('form-control')

