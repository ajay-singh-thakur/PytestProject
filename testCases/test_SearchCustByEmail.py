import pytest
import time
from PageObjects.loginPage import LoginPage
from PageObjects.addCustPage import AddCust
from PageObjects.searchCustPage import SearchCustomer
from utilities.readproperty import ReadConfig
from utilities.customLogger import LogGen


class Test_004SearchCustByEmail:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()


    @pytest.mark.regresssion
    def test_searchCUstomer(self, setup):
        self.logger.info("****************** Test004 Search Customer By Email ***********************")
        self.logger.info("********************** Verify Home Page Title **********************")
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
        self.logger.info("*************** Searching Customer By Email ID ****************")
        searchCust = SearchCustomer(self.driver)
        searchCust.setEmail("admin@yourStore.com")
        searchCust.clickOnSearchButton()
        time.sleep(5)
        self.status = searchCust.searchCustByEmail("admin@yourStore.com")
        if self.status == True:
            assert True
            self.logger.info("***************** Search Cust By Email Test Passed ******************")
        else:
            self.logger.error("***************** Search Cust By Email Test Failed ******************")
            assert False
        self.driver.close()

        self.logger.info("***************** Test 004 Search Cust By Email Test Finished ******************")