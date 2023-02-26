Feature: Sign up for an account
    As a user, I want to create an account so that I can use the services of McPool

    Scenario: Successful sign up
        Given I am on the sign-up page
        When I fill in my name, email, mcgill id, password, and driver status
        And I click the 'Submit' button
        Then I should see a success message



#    Scenario: Invalid email provided
#        Given I am on the sign-up page
#        And I provide an invalid email address
#        And I click the "Submit" button
#        Then I should see an error message indicating that the email address is invalid
