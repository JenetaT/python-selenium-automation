from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Sign In')
def Click_sign_in(context):
    context.driver.find_element(By.XPATH, '//*[@id="headerPrimary"]/a[4]/span').click()
    sleep(4)
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

@then('Verify Sign in form opened')
def verify_signin_form(context):
   actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']").text
   assert 'Sign into your Target account' in actual_text, (f'Error! Text Sign into your Target account not in {actual_text}')