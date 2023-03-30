Feature: Add a driver's schedule
    As a driver, I want add my schedule to a trip so that passengers know my availabilities for a trip

    Scenario: Successful adding of driver's schedule
        Given I am on the add-driver-schedule page
        When I fill in the start date, start time, and trip id
        And I click the Submit button
        Then I should see a success message