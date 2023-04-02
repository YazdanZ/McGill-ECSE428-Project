Feature: Home Button
    As a user, I want to be able
    to return to the home page from any other page.

Scenario Outline: Successful use of home button
      Given I am not on the home page
      When I use the home button
      Then I should be sent back to the home page