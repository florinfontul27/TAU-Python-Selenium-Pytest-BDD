from time import sleep
from pytest_bdd import scenarios, when, then, given, parsers
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

#Scenario
scenarios('../features/test_login_page.feature')

@given('open the login page')
def open_page(browser):
    login_page = LoginPage(browser)
    login_page.load_page()

@when(parsers.cfparse('the user type username "{username}"'))
def input_username(browser, username):
    login_page = LoginPage(browser)
    login_page.insert_username_field(username)

@when(parsers.cfparse('the user type password "{password}"'))
def input_password(browser, password):
    login_page = LoginPage(browser)
    login_page.insert_password_field(password)

@when('the user click login button')
def click_login(browser):
    login_page = LoginPage(browser)
    login_page.click_login_button()

@then('the welcome message appears on page')
def check_welcome_message(browser):
    secure_page = SecurePage(browser)
    assert secure_page.get_welcome_text(browser) == 'Welcome to the Secure Area. When you are done click logout below.', "Welcome message is not ok"

@then(parsers.cfparse('"{message}" success message is displayed'))
@then(parsers.cfparse('"{message}" error message is displayed'))
def check_error_message(browser, message):
    login_page = LoginPage(browser)
    assert message in login_page.get_flash_message(), "Flash message is not ok"

@then("the user is on the login page")
def check_url(browser):
    login_page = LoginPage(browser)
    assert login_page.URL == login_page.get_current_url()

@then("the user is on the secure page")
def check_url(browser):
    secure_page = SecurePage(browser)
    assert secure_page.URL == secure_page.get_current_url()


@then(parsers.cfparse('"{message}" success message is displayed'))
def check_flash_message(browser, message):
    secure_page = SecurePage(browser)
    assert message in secure_page.get_flash_message(), "Flash message is not ok"