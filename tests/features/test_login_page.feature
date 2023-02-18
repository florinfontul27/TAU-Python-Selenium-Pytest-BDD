Feature: Test login functionality
  Scenario: Test log in successfully
    Given open the login page
    When the user type username "tomsmith"
    And the user name type password "SuperSecretPassword!"
    And the user click login button
    Then the welcome message appears on page
    And the user is on the secure page
    And "You logged into a secure area!" success message is displayed

  Scenario Outline: check error message with wrong credentials
      Given open the login page
      When the user type username "<username>"
      And the user type password "<password>"
      And the user click login button
      Then "<error>" error message is displayed
      And the user is on the login page


    Examples: Username and passwords and message error
       | username| password| error |
       | tomsmith |   dsfdf | Your password is invalid! cbvcnbnn|
       | fdsfd    |   SuperSecretPassword!  | Your username is invalid! |
       | TOMSMITH   |  SuperSecretPassword!  | Your username is invalid! |
