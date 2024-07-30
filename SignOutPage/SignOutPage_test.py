from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SignOutLocator.SignOutLocator_test import SignOutLocator


class SignOutPage:

    def __init__(self, driver):
        self.driver = driver

    def sign_out(self):
        click_sign_out = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SignOutLocator.CLICK_SIGN_OUT))
        click_sign_out.click()
