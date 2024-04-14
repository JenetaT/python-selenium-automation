from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify “Your cart is empty” message is shown')
def verify_cart_status(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1xmf98v-0']").text
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f'Error! {expected_text} not found in {actual_text}'


@when('Add item to cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor88084798']").click()
    sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor88084798.styles__StyledBaseButtonInternal-sc-ysboml-0.styles__ButtonPrimary-sc-5fh6rr-0.hCWYcY.bEdlr").click()
    sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, "[class*='StyledBaseButtonInternal-sc-ysboml-0 styles__ButtonPrimary-sc-5fh6rr-0 hCWYcY bEdlr']").click()


@then('Navigate to cart page')
def navigate_to_cart(context):
    context.driver.get("https://www.target.com/cart")


@then('Verify item in cart')
def verify_item_in_cart(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles__CartSummarySpan-sc-odscpb-3']")
    assert '1 item' in actual_text, (f'Error! Text subtotal not in {actual_text}')