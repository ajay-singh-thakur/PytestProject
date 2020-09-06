import pytest
import time
from PageObjects.loginPage import LoginPage
from PageObjects.addCustPage import AddCust
from PageObjects.searchCustPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readproperty import ReadConfig


class Test_005SearchCustByName:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regresssion
    def test_SearchCustbyName(self, setup):
        self.logger.info(self.logger.info("********************** Test_004 Search Cust By Name **********************"))
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setuserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickonlogin()

        self.addCust = AddCust(self.driver)
        self.addCust.clickOnCustomers()
        self.addCust.clickOnCustomersMenu()

        srhCust = SearchCustomer(self.driver)
        srhCust.setFirstName("Steve")
        srhCust.setLastName("Gates")
        srhCust.clickOnSearchButton()
        time.sleep(5)
        status = srhCust.searchByName("Steve Gates")

        if status == True:
            assert True
            self.logger.info("************** Test 004 Search Cust By Name Passed ********************")
        else:
            self.logger.error("************** Test 004 Search Cust By Name Failed ********************")
            assert False
        self.driver.close()
        self.logger.info("************** Test 004 Search Cust By Name Finished ********************")
