from selenium.webdriver.common.by import By


class NewCustomerLocator:
    CLICK_NEW_CUSTOMER = (By.ID, "new-customer")
    ENTER_EMAIL = (By.ID, "EmailAddress")
    ENTER_FIRSTNAME = (By.ID, "FirstName")
    ENTER_LASTNAME = (By.ID, "LastName")
    ENTER_CITY = (By.ID, "City")
    CLICK_STATE = (By.NAME, "state")
    CLICK_GENDER = (By.NAME, "gender")
    CLICK_PROMOTIONAL_LIST = (By.NAME, "promo-name")
    CLICK_SUBMIT = (By.XPATH, "/html/body/section/div/div/div/div/form/button")