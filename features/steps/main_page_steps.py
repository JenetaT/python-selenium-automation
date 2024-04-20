from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
CLICK_SIGN_IN = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when("Search for {item}")
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)


@when('Click on Cart icon')
def Click_on_cart(context):
    context.driver.find_element(*CART_ICON).click()
    context.wait.until(
        EC.presence_of_element_located(CART_ICON),
        message='Cart icon not present'
    )


@when('Click Sign In')
def Click_sign_in(context):
    context.driver.find_element(*CLICK_SIGN_IN).click()
    context.wait.until(
        EC.presence_of_element_located(CLICK_SIGN_IN),
        message='Sign in button not present'
    )
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()


@then('Verify header in shown')
def verify_header_shown(context):
    context.driver.find_element(*HEADER)


@then('Verify header has 6 links')
def verify_header_links(context):
    links = context.driver.find_elements(*HEADER_LINKS)
    #print(links)
    assert len(links) == 6, f'Expected 6 links but got {len(links)}'

# @then('Verify header has {expected_amount} links')
# def verify_header_links(context, expected_amount):
#     expected_amount = int(expected_amount)
#     links = context.driver.find_elements(*HEADER_LINKS)
#     print(links)
#     assert len(links) == expected_amount, (f' Expected {expected_amount} links but got {len(links)}')

 # to print all names:
 # for link in links:
 #    print(link.text)

    all_text = [link.text for link in links]
    print(all_text)