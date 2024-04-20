from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[class*='styles__StyledBaseButtonInternal-sc-ysboml-0 styles__ButtonPrimary-sc-5fh6rr-0 brTHah bEdlr']")
SIDE_NAV_TO_CART_BTN = (By.CSS_SELECTOR, "[class*='styles__StyledBaseButtonInternal-sc-ysboml-0 styles__ButtonPrimary-sc-5fh6rr-0 hCWYcY bEdlr']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[class*='h-margin-l-default']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test*='cartItem-title']")


@ then('Verify “Your cart is empty” message is shown')
def verify_cart_status(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc-1xmf98v-0']").text
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f'Error! {expected_text} not found in {actual_text}'


@when('Click on Add to Cart button')   # Always clicks on the first item
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.wait.until(
        EC.presence_of_element_located(ADD_TO_CART_BTN),
        message='Add to cart button not present'
    )
# add multiple to cart
#     add_cart_buttons = context.driver.find_elements(*ADD_TO_CART_BTN).click()
#     for btn in add_cart_buttons[:5]:
#         btn.click()
#         add_cart_buttons[4].click() # will only addd 5th


@when('store product name')
def store_product_name(context):
    context.wait.until(
        EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not present on page'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when('Confirm Add to cart button from side nav')
def confirm_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_TO_CART_BTN).click()
    context.wait.until(
        EC.presence_of_element_located(SIDE_NAV_TO_CART_BTN),
        message='Side nav, Add to cart button did not disappear'
    )


@then('Open cart page')
def navigate_to_cart(context):
    context.driver.get("https://www.target.com/cart")


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f"Expected {amount} items but got {cart_summary}"


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE)
    assert context.product_name in actual_name, f"Expected {context.product_name} is not in {actual_name}"