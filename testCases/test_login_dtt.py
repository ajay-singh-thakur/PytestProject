import pytest
from selenium import webdriver
from PageObjects.loginPage import LoginPage
from testCases import conftest
import time
from utilities.readproperty import ReadConfig
from utilities.customLogger import LogGen
from pytest_html import hooks
from utilities import XLUtily


class Test_02_Login_DTT:
    base_url = ReadConfig.getApplicationURL()
    path=r"E:\SeleniumFramework\HybridFramework\PytestProject\testData\LoginTestData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regresssion
    # @pytest.mark.ajay
    def test_ddt_login_002(self, setup):
        self.logger.info("********************** test_ddt_login_002 ***********************")
        self.logger.info("********************** Verifying DDT Login Test **********************")
        self.driver = setup
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        self.row = XLUtily.getRowCount(self.path, 'Sheet2')
        print("No of ROws in a sheet : ", self.row)

        lst_status = []
        for r in range(2, self.row+1):

            self.user = XLUtily.readData(self.path, 'Sheet2', r, 1)
            self.password = XLUtily.readData(self.path, 'Sheet2', r, 2)
            self.exp = XLUtily.readData(self.path, 'Sheet2', r, 3)

            self.lp.setuserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickonlogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"


            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("************* Test Passed **************")
                    self.lp.clickonlogout()
                    lst_status.append('Pass')
                elif self.exp == "Fail":
                    self.logger.error("************* Test Failed **************")
                    self.lp.clickonlogout()
                    lst_status.append('Fail')
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.error("************* Test Failed **************")
                    lst_status.append('Fail')
                elif self.exp == "Fail":
                    self.logger.info("************* Test Passed **************")
                    lst_status.append('Pass')
        print("Status : ", lst_status)
        if 'Fail' not in lst_status:
            self.logger.info("************* Login Test DDT is Passed **************")
            self.driver.close()
            assert True
        else:
            self.logger.error("************* Login Test DDT is Failed **************")
            self.driver.close()
            assert False
        self.logger.info("************* End Of Login DDT Test **************")
        self.logger.info("************* test_ddt_login_002 Completed **************")