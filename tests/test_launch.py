from pages.base_page import BasePage
from utils.config import Config
import time

#pytest tests\test_launch.py
#pytest tests\test_launch.py::test_launch_test_browser --alluredir=allure-results
#allure serve allure-results
def test_launch_test_browser(page):
    base_page = BasePage(page)
    base_page.navigate(Config.BASE_URL)
    time.sleep(5)