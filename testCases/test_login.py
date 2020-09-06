import pytest
from selenium import webdriver
from PageObjects.loginPage import LoginPage
from testCases import conftest
import time
from utilities.readproperty import ReadConfig
from utilities.customLogger import LogGen
from pytest_html import hooks


class Test_01_Login:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_homepage(self, setup):
        self.logger.info("********************** Test_01_Login **********************")
        self.logger.info("********************** Verify Home Page Title **********************")
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********************** Home Page Title is passed **********************")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_homepage2.png")
            self.driver.close()
            self.logger.error("********************** Home Page Title is failed **********************")
            assert False

    # @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********************** Verifying Login Test**********************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setuserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickonlogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.lp.clickonlogout()
            time.sleep(2)
            self.driver.close()
            self.logger.info("********************** Test Login passed **********************")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_login1.png")
            self.driver.close()
            self.logger.error("********************** Test Login Failed **********************")
            assert False
