from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

user_email = input("Please enter your email: ")
user_password = input("Please enter your password: ")

url = "https://www.trendyol.com/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

try:
    # Close Pop-ups
    popup_close = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "modal-close"))
    )
    popup_close.click()
    time.sleep(random.uniform(1, 2))

    # Click the "Login" link
    login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "link-text"))
    )
    login.click()
    time.sleep(random.uniform(1, 2))  # Random wait time

    # Enter email in the email field
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-email"))
    )
    email_field.send_keys(user_email)
    time.sleep(random.uniform(2, 3))

    # Enter password in the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-password-input"))
    )
    password_field.send_keys(user_password)
    time.sleep(random.uniform(2, 3))

    # Click the login button
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit"))
    )
    button.click()
    time.sleep(random.uniform(3, 4))

    # Login Status
    try:
        error_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "error-box-wrapper"))
        )
        print("Error: Login failed.")
    except Exception as e:
        print("Success: Login successful.")

except Exception as e:
    print(e)
finally:
    driver.close()  # Close the browser
