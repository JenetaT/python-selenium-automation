from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Cart icon')
def Click_on_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(4)

@then('Verify “Your cart is empty” message is shown')
def verify_cart_status(context):
    actual_text = context.driver.find_element(By.XPATH, "//*[@id='cart-container']").text
    assert 'Your cart is empty' in actual_text, f'Error! Text Your cart is empty not in {actual_text}'


