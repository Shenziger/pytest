from selenium.webdriver.common.by import By
from octest.locators.MainPage import MainPage


def test_logo(driver, url_param):
    # url = request.config.getoption("--url")
    # url = url_param
    driver.get(url_param)
    driver.find_element_by_id('logo')
    assert driver.title == "Your Store"


def test_slideshow(driver, url_param):
    driver.get(url_param)
    # driver.find_element(By.ID, "slideshow0").click()
    driver.find_element_by_css_selector(MainPage.promoblock).click()
    driver.find_element(By.CLASS_NAME, "breadcrumb")


def test_menu(driver, url_param):
    driver.get(url_param)
    driver.find_elements_by_link_text('Desktops')
    driver.find_elements_by_link_text('Tablets')
    driver.find_elements_by_link_text('Cameras')


def test_footer(driver, url_param):
    driver.get(url_param)
    driver.find_element_by_css_selector('footer')


def test_search_form(driver, url_param):
    driver.get(url_param)
    driver.find_elements_by_class_name('form-control')

