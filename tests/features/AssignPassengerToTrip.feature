Feature: Assign a passenger to a trip
    As a passenger
    I want to be able to pick a trip
    So that I can get the trip that I want

Scenario: Successful assignment of passenger to a trip
      Given I am on the available trips page
      When I enter an existing email address under the trip that I picked
      And I click the Submit button
      Then I should be assigned to the trip that I picked