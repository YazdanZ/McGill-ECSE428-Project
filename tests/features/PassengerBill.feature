Feature: Passenger Bill
    As a student passenger,
    I would like to view all my previous bills,
    so that I am aware of how much I spent on McPool.

    Scenario: Successful display of Passenger Bill
        Given I am on the Signup page
        Given I am an existing user with email samiad2788@gmail.com and password mamama
        Given I am logged in with email samiad2788@gmail.com and password mamama
        Given I have two trips that I created
        When I select to go to the passenger bill page
        Then I should be able to see the bills for the two trips I created

# Scenario: Unsuccessful display of Passenger Bill
#     Given I am an existing user
#     Given I am logged in
#     Given that I have no trip that I created
#     When I select to go to the passenger bill page
#     Then I should not be able to see any bill