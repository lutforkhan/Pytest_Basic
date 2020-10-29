
from selenium import webdriver
from selenium.webdriver import firefox
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
from time import sleep
import pytest
class Test_Class:

    def test_khan1(self):
        print("Hi Khan")


    def test_fatema(self):
        print("Hi Fatema")
    @pytest.fixture
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=".\\drivers\\chromedriver.exe")
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        sleep(2)
        self.driver.maximize_window()
        yield
        self.driver.close()

    @pytest.mark.sanity
    def test_selectRadioButton(self,setUp):
        self.driver.find_element_by_xpath("//*[@id=\"radio-btn-example\"]/fieldset/label[1]/input").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"radio-btn-example\"]/fieldset/label[2]/input").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"radio-btn-example\"]/fieldset/label[3]/input").click()
        sleep(1)

    def test_selectOptionButton(self, setUp):
        self.driver.find_element_by_xpath("//*[@id=\"checkBoxOption1\"]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"checkBoxOption2\"]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"checkBoxOption3\"]").click()
        sleep(1)

        # // Select
        # List
        # By
        # selectList = By.id("dropdown-class-example");
        # // Select
        # option
        # buttons
        # By
        # optionButton1 = By.xpath("");
        # By
        # optionButton2 = By.xpath("//*[@id=\"checkBoxOption2\"]");
        # By
        # optionButton3 = By.xpath("//*[@id=\"checkBoxOption3\"]");
        #
        #





