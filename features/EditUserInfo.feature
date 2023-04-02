Feature: EditUserInfo
    As a user,
    I want to be able to edit my account 
    information so that it can be kept up to date.

    Scenario: Successfully Update Account Information 
        Given The user is on the EditUserInfo page
        When The user fills in the required fields
        And The user selects the Submit button
        Then The system successfully updates the account information

    Scenario: Unsuccessful Information Update
        Given The user is on the EditUserInfo page
        When The user selects the Submit button
        Then The system fails to update the account information

