Feature: Test Add Remove Elements functionality

    Scenario: Check logout button
        Given the user is logged in
        When the user click on logout button
        Then "You logged out of the secure area!" success message is displayed