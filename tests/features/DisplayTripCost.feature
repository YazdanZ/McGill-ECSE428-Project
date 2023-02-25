Feature: View the cost of a specific trip

Scenario Outline: Existing trip cost is displayed
Given A trip with trip_id 12345 exists in the database
When The displayTripCost page is opened with trip_id 12345 parameter passed through the URL
Then The trip_id, total cost in CAD, number of passengers, available seats, cost per passenger, trip length, estimated fuel consumption, and estimated C02 saved for the trip with ID 12345 is displayed
And A link to return to the trip display page is displayed
When The link to return to the trip display page is selected
Then The trip display page regarding trip 12345 is displayed