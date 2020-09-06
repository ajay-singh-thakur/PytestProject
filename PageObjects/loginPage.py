from selenium import webdriver


class LoginPage:

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_submit_xpath = "//input[@class='button-1 login-button']"
    link_logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setuserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickonlogin(self):
        self.driver.find_element_by_xpath(self.button_submit_xpath).click()

    def clickonlogout(self):
        self.driver.find_element_by_link_text(self.link_logout_link_text).click()

