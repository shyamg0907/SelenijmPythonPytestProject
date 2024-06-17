import time

import allure
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup", "log_on_failure")
class TestSearch:
    def test_search_for_a_valid_products(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        # link1 = driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
        # assert link1 == True
        self.driver.quit()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_for_an_invalid_products(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        # link1 = driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
        expected_text = "There is no product that matches the search criteria."
        # text_invalid_search = driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
        # print(text_invalid_search)
        # assert text_invalid_search == expected_text
        self.driver.quit()
