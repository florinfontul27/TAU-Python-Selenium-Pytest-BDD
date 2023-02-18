from pytest_bdd import scenarios, when, then, given, parsers
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

#Scenario
scenarios('../features/test_secure_page.feature')

@given("the user is logged in")
def login(browser):
    login_page = LoginPage(browser)
    secure_page = SecurePage(browser)
    login_page.login("tomsmith", "SuperSecretPassword!")
    secure_page.wait_for_logout_button()

@then(parsers.cfparse('"{message}" success message is displayed'))
def check_flash_message(browser, message):
    secure_page = SecurePage(browser)
    assert message in secure_page.get_flash_message(), "Flash message is not ok"

@when("the user click on logout button")
def click_logout_button(browser):
    secure_page = SecurePage(browser)
    login_page = LoginPage(browser)
    secure_page.click_logout_button()
    login_page.wait_for_login_button()