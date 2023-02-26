Feature: Calculate pickup to school distance
    As an administrative user, I want to calculate the distance between the pickup and drop-off locations for a given trip,
    so that I can provide useful information to the users, such as cost per passenger, estimated fuel consumption, and estimated CO2 emission saved.

    Scenario: Normal flow - Display the pickup to destination distance
        Given a user is signed in as a passenger or driver
        When the user opens a trip
        Then the system should display the distance between the pickup location and destination
        And the system should calculate and display the cost per passenger, estimated fuel consumption, and estimated CO2 emission saved.

    Scenario: Error flow - Invalid pickup location
        Given a user is signed in as a passenger or driver
        And the pickup location for a given trip is not found
        When the user opens the trip
        Then the system should display the distance and all related information as NaN.

