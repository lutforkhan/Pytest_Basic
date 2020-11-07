import allure
from behave import Step
from selenium import webdriver
from selenium.webdriver import firefox
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
from selenium.webdriver.support.ui import Select
from time import sleep
import pytest
class Test_Class:
    # @Epic
    # @Features
    # @Stories / @ Story
    # @Severity(SeverityLevel.BLOCKER)
    # @Description("In this cool test we will check cool thing")
    # @allure.step
    # @Step("this is the first step tetst khan")
    # # @Attachment
    # @Link
    @allure.description("First test descption in allure framework")
    def test_khan1(self):
        print("Hi Khan")

    @allure.step("this is the first step of Fatema test")
    def test_fatema(self):
        print("Hi Fatema")
    @pytest.fixture
    @Step("this is the step of fixture")
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\\drivers\\chromedriver.exe")
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        sleep(2)
        self.driver.maximize_window()
        yield
        self.driver.close()

    @pytest.mark.sanity
    @allure.step("this is the sanity testing")
    @allure.severity(severity_level="Hotfix")
    def test_selectRadioButton(self,setUp):
        self.driver.find_element_by_xpath("//*[@id=\"radio-btn-example\"]/fieldset/label[1]/input").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"radio-btn-example\"]/fieldset/label[2]/input").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"radio-btn-example\"]/fieldset/label[3]/input").click()
        sleep(1)

    @pytest.mark.regression
    @allure.link("www.google.com")
    @allure.testcase("www.google.com","TestCase_001")
    def test_selectOptionButton(self, setUp):
        self.driver.find_element_by_xpath("//*[@id=\"checkBoxOption1\"]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"checkBoxOption2\"]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"checkBoxOption3\"]").click()
        sleep(1)

    @pytest.mark.regression
    def test_selectDropDownList(self, setUp):
        ele=self.driver.find_element_by_xpath("//*[@id='dropdown-class-example']")
        obj=Select(ele)
        obj.select_by_index(0)
        sleep(1)
        obj.select_by_index(1)
        sleep(1)
        



