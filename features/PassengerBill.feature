Feature: Passenger Bill
    As a student passenger,
    I would like to view all my previous bills,
    so that I am aware of how much I spent on McPool.

    Scenario: Unsuccessful display of Passenger Bill
        Given I am on the Signup page
        Given I am an existing user with email samiad2766@gmail.com and password mamama
        Given I am logged in with email samiad2766@gmail.com and password mamama
        Given I have no trip that I created
        When I select to go to the passenger bill page
        Then I should not be able to see any new bill

    Scenario: Successful display of Passenger Bill
        Given I am on the Signup page
        Given I am an existing user with email samiad2789@gmail.com and password mamama
        Given I am logged in with email samiad2789@gmail.com and password mamama
        Given I have one trip that I created
        When I select to go to the passenger bill page
        Then I should be able to see the information corresponding to my trip in the passenger bill page