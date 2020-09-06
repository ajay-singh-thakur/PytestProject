# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# import time


class SearchCustomer:

    textbox_searchEmail_xpath = "//input[@id='SearchEmail']"
    textbox_searchFirstName_xpath = "//input[@id='SearchFirstName']"
    textbox_searchLastName_xpath = "//input[@id='SearchLastName']"
    button_searchCust_xpath = "//button[@id='search-customers']"
    grd_tableGrid_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    # grd_tableGrid_xpath = "//div[@class='dataTables_scroll']"
    tableRow_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.textbox_searchEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_searchEmail_xpath).send_keys(email)

    def setFirstName(self, FirstName):
        self.driver.find_element_by_xpath(self.textbox_searchFirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_searchFirstName_xpath).send_keys(FirstName)

    def setLastName(self, LastName):
        self.driver.find_element_by_xpath(self.textbox_searchLastName_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_searchLastName_xpath).send_keys(LastName)

    def clickOnSearchButton(self):
        self.driver.find_element_by_xpath(self.button_searchCust_xpath).click()

    def getNoOfRows(self):
        ln = len(self.driver.find_elements_by_xpath(self.tableRow_xpath))
        return ln

    def getNoOfColumn(self):
        ln = len(self.driver.find_elements_by_xpath(self.tableColumn_xpath))
        return ln

    def searchCustByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailID = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailID == email:
                flag = True
                break
        return flag

    def searchByName(self, name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            fname = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if fname == name:
                flag = True
                break
        return flag


