Feature: Display trip details

  Scenario: Successfully retrieve and display trip details - Main Success Scenario
    Given the passenger with email "mark@mail.com" and password "password" signs into the application
    When the passenger accesses the Trip Display page to view trip information
    Then the passenger should see the trip details

  Scenario: Failed to retrieve and display trip details - Error Flow
    Given the passenger with email "jane@mail.com" and password "password" signs into the application
    When the passenger accesses the Trip Display page to view trip information
    Then the passenger should not see any trip details