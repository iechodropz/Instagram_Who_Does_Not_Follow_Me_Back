from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def login(driver, username, password):
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(5)

    try:
        mfa_field = driver.find_element(By.NAME, "verificationCode")
    except NoSuchElementException:
        return
    
    mfa = input("Enter MFA Code: ")
    mfa_field.send_keys(mfa)

    confirm_button = driver.find_element(By.XPATH, "//button[@type='button']")
    confirm_button.click()

    time.sleep(5)
