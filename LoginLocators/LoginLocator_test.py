from selenium.webdriver.common.by import By


class LoginLocators:
    ENTER_EMAIL_ADDRESS = (By.ID, "email-id")
    ENTER_PASSWORD = (By.ID, "password")
    REMEMBER_CHECK_BOX = (By.ID, "remember")
    CLICK_SUBMIT_BUTTON = (By.ID, "submit-id")
