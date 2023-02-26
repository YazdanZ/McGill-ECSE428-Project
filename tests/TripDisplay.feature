Feature: Display trip details

  Scenario: Successfully retrieve and display trip details - Main Success Scenario
    Given the passenger with email "mark@mail.com" is signed into the McPool Website
    And there exists a trip with the following details
      |trip_id |distance_km |driver_name |vehicle_description |fuel_consumption |seats |pickup_address |dropoff_address  |cost |duration   |
      |2       |20          |John Smith  |Honda Civic         |30               |4     |123 Main St    |456 Secondary St |$50  |30 minutes |
    And the passenger with email "mark@mail.com" is assigned to trip with trip_id = 2
    When the passenger accesses the Trip Display page to view trip information
    Then the passenger should see the following trip details:
      |Driver            |John Smith       |
      |Vehicle           |Honda Civic      |
      |Pickup Location   |123 Main St      |
      |Dropoff Location  |456 Secondary St |
      |Distance          |20 kilometers    |
      |Cost              |$50              |
      |Duration          |30 minutes       |

  Scenario: Failed to retrieve and display trip details - 
    Given the passenger with email "jane@mail.com" is signed into the McPool Website
    And the passenger "jane@mail.com" is not assigned to any trips
    When the passenger accesses the Trip Display page to view trip information
    Then the passenger should see the error message "You are not assigned to any trips"