Feature: Login
    As a user
    I want to be able to log in
    So that I can access my account

    Scenario: Successful login
        Given I am on the Login page
        When I enter an existing email address and password
        And I click the Submit button
        Then I should be redirected to the UserInfo page

    Scenario: Unsuccessful login
        Given I am on the Login page
        When I enter a non-existing email address and password
        And I click the Submit button
        Then An Error Message should be displayed