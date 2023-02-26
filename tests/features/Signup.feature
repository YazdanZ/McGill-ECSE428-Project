Feature: Sign up for an account
    As a user, I want to create an account so that I can use the services of McPool

    Scenario: Successful sign up
        Given I am on the sign-up page
        When I fill in my name, email, mcgill id, password, and driver status
        And I click the 'Submit' button
        Then I should see a success message



    Scenario: Email already exists
        Given I am on the sign-up page
        Given an account exists in the system with email 'johndoe@yahoo.com'
        When I attempt to create an account with email 'johndoe@yahoo.com'
        And I click the 'Submit' button
        Then I should see an error message indicating email already exists in the system


    Scenario: McGill ID already exists
        Given I am on the sign-up page
        Given an account exists in the system with mcgill id '24356'
        When I attempt to create an account with mcgill id '24356'
        And I click the 'Submit' button
        Then I should see an error message indicating mcgill id already exists in the system



    Scenario: Invalid email provided
        Given I am on the sign-up page
        When I attempt to create an account with an invalid email address
        And I click the 'Submit' button
        Then I should see an error message indicating that the email address is invalid
