Feature: Display Available Trips
      As a passenger
      I want to be able to see all the available trips
      So that I can pick a trips

      Scenario: Successful display available trips
          Given There are available trips created
          When I fetch the available trips data
          Then I should get the first trip data

      Scenario: Successful display available trips
          Given There are available trips created
          When I go to the available trips page
          Then I should be able to see all of the available trips 
     