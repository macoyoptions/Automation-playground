import time

from selenium.webdriver.support.wait import WebDriverWait
from LoginLocators.LoginLocator_test import LoginLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def email_address(self, email):
        enter_email_address = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ENTER_EMAIL_ADDRESS))
        enter_email_address.send_keys(email)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.ENTER_PASSWORD))
        enter_password.send_keys(password)

    def remember_check_box(self):
        remember_check_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.REMEMBER_CHECK_BOX))
        remember_check_box.click()

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocators.CLICK_SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(5)