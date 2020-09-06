from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\seleniumDrivers\chromedriver.exe")
        print('Launching Chrome Browser')
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\seleniumDrivers\geckodriver.exe")
        print('Launching Firefox Browser')
    elif browser == 'IE':
        driver = webdriver.Firefox(executable_path="C:\seleniumDrivers\IEDriverServer.exe")
        print('Launching IE Browser')
    else:
        print('Wrong Browser Provided ----------------')
    return driver




def pytest_addoption(parser):  # This will Get the Value from CLI Hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return a browser value to setup method
    return request.config.getoption("--browser")


################# HTML Report #####################

#Hook for  adding environment info HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Pytest Framework Test'
    config._metadata['Module  Name'] = 'Customer'
    config._metadata['Tester'] = 'Ajay'


# Hoook for  delete/Modify Environment info to HTML Report

def pytest_metadata(metadata):
    metadata.pop("Java Home", None)
    metadata.pop("Plugins", None)