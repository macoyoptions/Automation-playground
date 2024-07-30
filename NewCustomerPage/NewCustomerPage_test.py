from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from NewCustomerLocator.NewCustomerLocator_test import NewCustomerLocator


class NewCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def new_customer(self):
        new_customer = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.CLICK_NEW_CUSTOMER))
        new_customer.click()

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_EMAIL))
        enter_email.send_keys(email)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_FIRSTNAME))
        enter_firstname.send_keys(firstname)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_LASTNAME))
        enter_lastname.send_keys(lastname)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.ENTER_CITY))
        enter_city.send_keys(city)

    def state(self):
        click_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.CLICK_STATE))
        click_state.click()

    def gender(self):
        click_gender = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.CLICK_GENDER))
        click_gender.click()

    def promotional_list(self):
        click_promotional_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.CLICK_PROMOTIONAL_LIST))
        click_promotional_list.click()

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLocator.CLICK_SUBMIT))
        click_submit.click()
