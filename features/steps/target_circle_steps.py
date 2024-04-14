from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CELLS = (By.CSS_SELECTOR, "[class*='CellItemContainer']")

@given('Open Target Circle page')
def open_circle_page(context):
    context.driver.get("https://www.target.com/circle")

@then('Verify circle page opened')
def verify_circle_page_opened(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='style__DashboardCircleLogo-sc-16xc6k0-0']")

@then('Verify page has 10 benefit cells')
def verify_circle_benefit_cells(context):
    context.driver.find_element(*BENEFIT_CELLS)
    cells = context.driver.find_elements(*BENEFIT_CELLS)
    assert len(cells) == 10, f'Expected 10 links but got {len(cells)}'