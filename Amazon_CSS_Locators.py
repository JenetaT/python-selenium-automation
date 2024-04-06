from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?openid')

# logo by class  $$(".a-icon.a-icon-logo")
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

# Create account by Class $$(".a-spacing-small")
driver.find_element(By.CSS_SELECTOR, ".a-spacing-small")

# Customer name $$("#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Email ID $$("#ap_email")
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# First password entry $$("#ap_password")
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Password must be 6 characters
driver.find_element(By.CSS_SELECTOR, "")

# Re-Enter Password $$("#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# Create Amazon Account $$("#continue")
driver.find_element(By.CSS_SELECTOR, "#continue")

# Conditions $$("#legalTextRow")
driver.find_element(By.CSS_SELECTOR, "#legalTextRow")

# Privacy $$("#legalTextRow")
driver.find_element(By.CSS_SELECTOR, "#legalTextRow")

# Sign In $$(".a-link-emphasis")
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")