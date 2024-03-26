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
driver.get('https://www.target.com/')

sleep(4)
# Click Signin Button
driver.find_element(By.XPATH, '//*[@id="headerPrimary"]/a[4]/span').click()

sleep(4)

# click Sign in button again
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(4)
# Verify target page opened
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div/h1/span')
print('Test Passed')

