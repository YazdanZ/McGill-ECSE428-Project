Feature: View trips created as a driver

  Scenario: Display trips assigned to a driver with one or more trips - Main Success Flow
    Given I am logged in as a driver with email "driver1@gmail.com" and password "password"
    When I go to the "ViewTripsAsDriver" page
    Then I should see a list of my created trips

   Scenario: Cancel a trip created by the driver - Alternate Flow
     Given I am logged in as a driver with email "driver2@gmail.com" and password "password"
     When I go to the "ViewTripsAsDriver" page
     And I click the "Cancel" button for the first trip
     Then the trip should be deleted from the list

   Scenario: Display trips assigned to a driver with no trips - Main Success Flow
     Given I am logged in as a driver with email "driver3@gmail.com" and password "password"
     When I go to the "ViewTripsAsDriver" page
     Then I should see no trips listed on the page