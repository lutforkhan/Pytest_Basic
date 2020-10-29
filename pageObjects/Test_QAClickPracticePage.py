# from selenium import webdriver
# import pytest
#
# class PracticePage:
#     webdriver driver
#     rdioButton_radio1_xpath="//*[@id=\"radio-btn-example\"]/fieldset/label[1]/input"
#     rdioButton_radio2_xpath = "//*[@id=\"radio-btn-example\"]/fieldset/label[2]/input"
#     rdioButton_radio3_xpath = "//*[@id=\"radio-btn-example\"]/fieldset/label[3]/input"
#     def __init__(self):
#         self.driver=webdriver.ChromeDriver()
#
#     def setRadioButton1(self):
#         self.driver.f
#
#
#
#

from selenium import webdriver
import sys
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome()
    sleep(5)
    print("Hi Khan")
    # chrome_driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
    # chrome_driver.maximize_window()
    # chrome_driver.find_element_by_name("li1").click()
    # chrome_driver.find_element_by_name("li2").click()
    # title = "Sample page — lambdatest.com"
    # assert title == chrome_driver.title
    # sample_text = "Happy Testing at LambdaTest"
    # email_text_field = chrome_driver.find_element_by_id("sampletodotext")
    # email_text_field.send_keys(sample_text)
    # sleep(5)
    # chrome_driver.find_element_by_id("addbutton").click()
    # sleep(5)
    # output_str = chrome_driver.find_element_by_name("li6").text
    # sys.stderr.write(output_str)
    # sleep(2)
    # chrome_driver.close()
    #
