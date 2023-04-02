Feature: Calculate distance between two points using map

Scenario: Calculate distance between two points successfully
    Given I am on the map page
    When I enter "Montréal-Pierre Elliott Trudeau International Airport (YUL), 975 rue Roméo-Vachon Nord, Dorval, Quebec H4Y 1H1, Canada" as point A address
    When I enter "845 Sherbrooke O Rue, Montréal, Quebec H3A 0G4, Canada" as point B address
    Then the distance between point A and point B of "19.1km" should be displayed

Scenario: Calculate distance between two points with invalid addresses
   When I enter "Invalid Address" as point A address
   When I enter "Invalid Address" as point B address
   Then an error message should be displayed

Scenario: Calculate distance between two points with missing addresses
   Given I am on the maps page
   When I enter "845 Sherbrooke O Rue, Montréal, Quebec H3A 0G4, Canada" as point A address
   When I leave point B address blank
   Then an error message should be displayed
