import pytest
import sys
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def pytest_addoption(parser):
    parser.addoption('--url', '-U', default='http://localhost/opencart/', action='store',
                     help='Url to make request to', required=False)
    parser.addoption('--browser', '-B', default='chrome', action='store',
                     help='Browser name: chrome or firefox', required=False)


@pytest.fixture()
def url_param(request):
    return request.config.getoption('--url')


@pytest.fixture()
def browser_param(request):
    return request.config.getoption('--browser')


@pytest.fixture()
def driver(request, browser_param):
#    url = request.config.getoption("--url")
#    browser = request.config.getoption("--browser")
    browser = browser_param
    if browser == 'firefox':
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': 300000, 'pageLoad': 300000, 'script': 30000}
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        options = Options()
#        options.binary = FirefoxBinary("E:\\seleniumdriver\\geckodriver.exe")
        binary = FirefoxBinary("E:\\seleniumdriver\\geckodriver.exe")
        wd = webdriver.Firefox(firefox_profile=profile, desired_capabilities=capabilities, options=options,
                               executable_path="E:\\seleniumdriver\\geckodriver.exe",
                               firefox_binary=binary)
        wd.maximize_window()
        print(wd.capabilities)
    elif browser == 'chrome':
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        wd = webdriver.Chrome(options=options, desired_capabilities=capabilities,
                              executable_path="E:\\seleniumdriver\\chromedriver.exe")
        wd.fullscreen_window()
#        print(wd.capabilities)
    else:
        raise Exception(f"{request.param} is not supported!")
#        print('Unsupported browser!')
#        sys.exit(1)
    wd.implicitly_wait(30000)
    wd.set_page_load_timeout(1000)
#    yield wd
#    wd.quit()
    request.addfinalizer(wd.quit)
##     wd.get(url_param)
#    wd.get(request.config.getoption("--url"))

    return wd
