from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Verify Sign in form opened')
def verify_signin_form(context):
   actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']").text
   assert 'Sign into your Target account' in actual_text, (f'Error! Text Sign into your Target account not in {actual_text}')