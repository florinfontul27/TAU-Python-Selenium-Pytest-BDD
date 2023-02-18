from pytest_bdd import scenarios, when, then, given, parsers
from pages.login_page import LoginPage
from pages.add_remove_elements_page import AddRemoveElementsPage

#Scenario
scenarios('../features/test_add_remove_elements_page.feature')

@given('open the add remove elements page')
def add_remove_page(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.load_page()

@when('the user click add button')
def click_add_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.clickAddButton()

@when('the user click delete button')
def click_delete_button(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page.clickDeleteButton()

@then('is delete button displayed')
def is_delete_button_displayed(browser):
    add_remove_page = AddRemoveElementsPage(browser)
    add_remove_page


