import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.mark.usefixtures("setup", "log_on_failure")
class TestLogin:
    @allure.severity(allure.severity_level.MINOR)
    def test_search_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, 'Login').click()
        # allure.attach(self.driver.get_screenshot_as_png(),name="search_with_valid_credentials",attachment_type=AttachmentType.PNG)
        # link1 = driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
        # assert link1 == True
        self.driver.quit()
