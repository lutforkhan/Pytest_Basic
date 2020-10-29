from selenium import webdriver
import allure
import pytest
import sys
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

class TestQAClickHome:
    def test_Checkbox(self):
        self.driver=webdriver.Chrome(executable_path=".\Drivers")
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        sleep(5)



