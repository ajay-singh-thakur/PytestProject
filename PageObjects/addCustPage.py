from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class AddCust:

    link_customer_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    link_customer_menu_item_xpath = "//span[@class='menu-item-title'][text()='Customers']"
    btn_addCustomer_xpath = "//a[@class='btn bg-blue']"
    textbox_email_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    textbox_firstName_xpath = "//input[@id='FirstName']"
    textbox_lastName_xpath = "//input[@id='LastName']"
    rdBtn_gendermale_id = "Gender_Male"
    rdBtn_genderFemale_id = "Gender_Female"
    textbox_DOB_xpath = "//input[@id='DateOfBirth']"
    textbox_companyName_xpath = "//input[@id='Company']"
    chkbox_taxExempt_xmpath = "//input[@id='IsTaxExempt']"
    # chkbox_customerroles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    chkbox_customerroles_xpath = "//div[10]//div[2]//div[1]//div[1]//div[1]"
    lstoption_Administration_xpath = "//option[contains(text(),'Administrators')]"
    lstoption_Guests_xpath = "//option[contains(text(),'Guests')]"
    lstoption_Registered_xpath = "//option[contains(text(),'Registered')]"
    lstoption_Vendor_xpath = "//option[contains(text(),'Vendors')]"
    lstoption_Vendors_xpath = "//*[@id='VendorId']"
    textbox_admincommment_xpath = "//textarea[@id='AdminComment']"
    btn_savebutton_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomers(self):
        self.driver.find_element_by_xpath(self.link_customer_menu_xpath).click()

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.link_customer_menu_item_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btn_addCustomer_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def setFirstName(self, firstName):
        self.driver.find_element_by_xpath(self.textbox_firstName_xpath).send_keys(firstName)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.textbox_lastName_xpath).send_keys(lastname)

    def setCompanyName(self, company):
        self.driver.find_element_by_xpath(self.textbox_companyName_xpath).send_keys(company)

    def setDOB(self, dob):
        self.driver.find_element_by_xpath(self.textbox_DOB_xpath).send_keys(dob)

    def selectGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdBtn_gendermale_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdBtn_genderFemale_id).click()
        else:
            self.driver.find_element_by_id(self.rdBtn_gendermaleid).click()

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.chkbox_customerroles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.lstoption_Registered_xpath)
        elif role == "Administrators":
            self.driver.find_element_by_xpath(self.lstoption_Administration_xpath)
        elif role == "Guests":
            #here user can be Reistered or Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            time.sleep(3)
            self.listitem = self.driver.find_element_by_xpath(self.lstoption_Guests_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstoption_Vendor_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstoption_Guests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectManagerOfVendor(self, vendor):
        drp = Select(self.driver.find_element_by_xpath(self.lstoption_Vendors_xpath))
        drp.select_by_visible_text(vendor)

    def setAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.textbox_admincommment_xpath).send_keys(comment)

    def clickOnSavebutton(self):
        self.driver.find_element_by_xpath(self.btn_savebutton_xpath).click()