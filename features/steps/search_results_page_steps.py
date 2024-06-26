from selenium.webdriver.common.by import By
from behave import then

SEARCH_RESULT_HEADER = (By.CSS_SELECTOR, "[class*='h-text-bs h-display-flex']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    # actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    # assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'
    context.app.search_results_page.verify_search_results(expected_item)


@then('Verify that URL has {partial_url}')
def verify_search_page_url(context,partial_url):
    # context.wait.until(EC.url_contains(partial_url), message=f'URL does not contain {partial_url}')
    context.app.search_result_page.verify_partial_url(partial_url)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)