import random
import string
import pytest
from selenium import webdriver
from PageObjects.loginPage import LoginPage
from PageObjects.addCustPage import AddCust
from utilities.customLogger import LogGen
from utilities.readproperty import ReadConfig


class Test_03_add_customer:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*********************** Test_03_add_customer Started *******************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setuserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickonlogin()
        self.logger.info("**************** Logged In Successfully *****************")
        self.logger.info("************ Started Add Customer Test **************")

        self.addcust = AddCust(self.driver)
        self.addcust.clickOnCustomers()
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnAddNew()

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test111")
        self.addcust.setFirstName("Ajay")
        self.addcust.setLastname("Thakur")
        self.addcust.selectGender("Male")
        self.addcust.setDOB("01/05/1989")
        self.addcust.setCompanyName("AutomationQA")
        self.addcust.setAdminComment("This is for testing ..")
        self.addcust.setCustomerRoles("Vendors")
        self.addcust.selectManagerOfVendor("Vendor 1")
        self.addcust.clickOnSavebutton()

        self.logger.info("************  Saving Customer Info **************")
        self.logger.info("*************  Add Customer Validation Started ***************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("************* Add Customer test Passed ****************")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_addCustomer.png")
            self.logger.error("**************** Add Customer Failed *****************")
            assert True

        self.driver.close()
        self.logger.info("*************** Ending Test_03_add_customer test ****************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
