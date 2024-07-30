import pytest
from selenium import webdriver

from LoginPage.LoginPage_test import LoginPage
from NewCustomerPage.NewCustomerPage_test import NewCustomerPage
from SignOutPage.SignOutPage_test import SignOutPage


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("https://automationplayground.com/crm/login.html")
    return login_page


def test_login_page_automation_playground(login):
    login.email_address("standard_user@gmail.com")
    login.enter_password("secret_sauce")
    login.remember_check_box()
    login.click_submit_button()


def test_new_customer_page(login):
    new_customer = NewCustomerPage(login.driver)
    new_customer = NewCustomerPage(login.driver)
    new_customer.email("oshodi@gmail.com")
    new_customer.firstname("kemi")
    new_customer.lastname("Adeola")
    new_customer.city("Akure")
    new_customer.state()
    new_customer.gender()
    new_customer.promotional_list()
    new_customer.submit()


def test_sign_out(login):
    sign_out = SignOutPage(login.driver)
    sign_out.sign_out()
